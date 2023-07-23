# This works very well for 1000 iterations too...
def first_part(notes):
    D = dict()
    num_monkeys = len(notes)
    for monkey in notes:
        split = [line.strip() for line in monkey.split('\n')]
        D[int(split[0].split(' ')[1][:-1])] = {
            "items": split[1].split(": ")[1].split(", "),
            "op": split[2].split(" = ")[1],
            "test": int(split[3].split(' ')[3]),
            True: split[4].split(' ')[5],
            False: split[5].split(' ')[5],
            "inspect": 0
        }
    for _ in range(20):
        for k in range(num_monkeys):
            items = D[k]["items"]
            while len(items) > 0:
                item = items.pop(0)
                D[k]["inspect"] += 1
                new = eval(D[k]["op"].replace("old", item)) // 3
                next_monkey = int(D[k][new % D[k]['test'] < 1])
                D[next_monkey]["items"].append(str(new))
        # print("Sequence:", [D[k]["inspect"] for k in range(len(D.keys()))])
    sort = sorted((D[k]["inspect"] for k in D), reverse=True)
    return sort[0] * sort[1]

# Function to evaluate an expression given an operation
# for instance, f(2, '+', 3) == 5
f = lambda a, op, b: a * b if op == '*' else a + b

# Uses a lookup table for subexpression results
# Calculate expr (mod m) (where expr is in format (op, expr, expr)) by applying the laws of modular arithmetic
# expr is of type `tuple`` or `str``
# Welps, it's too freaking slow!!
# And even building eval expression strings results in errors with "too many nested parenthesis", what bullcrap...
# And replacing the nexted parenthesesis with nested evals results in issues with unbalanced nested quotation marks! UGH!!
def expr_mod(expr, m, Lookup):
    if type(expr) == tuple: # subexpr
        try:
            return Lookup[m][expr]
        except KeyError:
            Lookup[m][expr] = f(expr_mod(expr[0], m, Lookup), expr[1], expr_mod(expr[2], m, Lookup)) % m
            return Lookup[m][expr]
    else: # int
        return int(expr) % m

# Still too inefficient despite optimizations!!!! >:(
def second_part(notes):
    D = dict()
    Lookup = dict() # Use a lookup table to store intermediary results for subexpressions
    num_monkeys = len(notes)
    for monkey in notes:
        split = [line.strip() for line in monkey.split('\n')]
        D[int(split[0].split(' ')[1][:-1])] = {
            "items": tuple(map(int, split[1].split(": ")[1].split(", "))),
            "op": split[2].split(" = ")[1].split(' '),
            "test": split[3].split(' ')[3],
            True: split[4].split(' ')[5],
            False: split[5].split(' ')[5],
            "inspect": 0
        }
    for _ in range(1000):
        for k in range(num_monkeys):
            items = D[k]["items"]
            m = int(D[k]["test"])
            if m not in Lookup:
                Lookup[m] = dict()
            for item in items:
                D[k]["inspect"] += 1
                new = tuple(item if i == "old" else i for i in D[k]["op"]) # Build expression trees to avoid massive numbers
                if type(item) == int and item <= 1000000: # Limit depth of expressions by allowing numbers to grow
                    new = f(int(new[0]), new[1], int(new[2]))
                mod = expr_mod(new, m, Lookup)
                next_monkey = int(D[k][mod < 1])
                D[next_monkey]["items"] += (new,)
            D[k]["items"] = tuple() # tuples are immutable and are therefore more efficient then mutable lists
    sort = sorted((D[k]["inspect"] for k in D), reverse=True)
    return sort[0], sort[1]

# UGGGGGGHHHHHHH, still TOO DAMN SLOW!!!! >M<
def second_part_2(notes):
    D = dict()
    num_monkeys = len(notes)
    for monkey in notes:
        split = [line.strip() for line in monkey.split('\n')]
        D[int(split[0].split(' ')[1][:-1])] = {
            "items": tuple(map(int, split[1].split(": ")[1].split(", "))),
            "op": split[2].split(" = ")[1].split(' '),
            "test": split[3].split(' ')[3],
            True: split[4].split(' ')[5],
            False: split[5].split(' ')[5],
            "inspect": 0
        }
    for k in range(num_monkeys):
        for item in D[k]["items"]:
            curr_monkey = k
            curr_item = item
            for _ in range(20):
                D[curr_monkey]["inspect"] += 1
                new = (curr_item if i == "old" else i for i in D[curr_monkey]["op"])
                curr_item = f(int(next(new)), next(new), int(next(new)))
                curr_monkey = int(D[curr_monkey][curr_item % int(D[curr_monkey]["test"]) < 1])
    sort = sorted((D[k]["inspect"] for k in D.keys()), reverse=True)
    return sort[0], sort[1]

# iterative expression evaluation
# accepts `expr` in form ((op1, val1), (op2, val2), ...)
# where `op` is '*' or '+'
# This is expectedly much faster than the recursive version!!
def expr_mod_iter(a, expr, m):
    for op in expr:
        a = f(a % m, op[0], (a if op[1] == "old" else int(op[1])) % m)
    return a % m

# SOOOOO CLOSE, but alas, still wrong for the main input... :(
# UPDATE 7/23/23 @ 2 PM: HELL YEAH, I GOT IT, and it's BLOODY EFFICIENT!!!! :D
def second_part_3(notes):
    D = dict()
    lookup = dict() # lookup table for intermediary results
    num_monkeys = len(notes)
    tests = set() # contains all the divisibility test values for use in the lookup table
    for monkey in notes:
        split = [line.strip() for line in monkey.split('\n')]
        key = int(split[0].split(' ')[1][:-1])
        test = int(split[3].split(' ')[3])
        tests.add(test,)
        D[key] = {
            "items": list(map(lambda e: (int(e), key), split[1].split(": ")[1].split(", "))),
            "op": split[2].split(" = ")[1].split(' '),
            "test": test,
            True: split[4].split(' ')[5],
            False: split[5].split(' ')[5],
            "value": 0
        }
    for _ in range(10000):
        for k in range(num_monkeys):
            items = D[k]["items"]
            seen = set() # sets are more efficient than lists due to immutability and 
            D[k]["value"] += len(items)
            m = D[k]["test"]
            while len(items) > 0:
                item = items.pop()
                # account for duplicate items starting at the same monkey
                if item not in seen:
                    _, op, b = D[k]["op"]
                    if item not in lookup:
                        lookup[item] = dict()
                    for test in tests:
                        old = lookup[item][test] if test in lookup[item] else item[0]
                        lookup[item][test] = f(old, op, (old if b == "old" else int(b)) % test) % test 
                    seen.add(item)
                next_monkey = int(D[k][lookup[item][m] < 1])
                D[next_monkey]["items"].append(item)
    sort = sorted((D[k]["value"] for k in D), reverse=True)
    return sort[0] * sort[1]

Sample = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1""".split("\n\n")
Input = open("Inputs/Day_11.txt").read().split("\n\n")
print(first_part(Input))
print(second_part_3(Input)) # Ugh, the numbers just get way too big >n<