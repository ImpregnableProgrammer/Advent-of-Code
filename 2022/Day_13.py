# Comparison function - returns -1 for >, 0 for ==, and 1 for <
def cmp(l1, l2):
    if type(l1) == type(l2) == int:
        return 0 if l1 == l2 else 2 * (l1 < l2) - 1
    else:
        l1 = [l1] if type(l1) == int else l1
        l2 = [l2] if type(l2) == int else l2
        while len(l1) > 0 and len(l2) > 0:
            e1, l1 = l1[0], l1[1:]
            e2, l2 = l2[0], l2[1:]
            rv = cmp(e1, e2)
            if rv != 0:
                return rv
        return 0 if len(l1) == len(l2) else 2 * (len(l1) < len(l2)) -1

def first_part(packets):
    right = 0
    for i in range(1, len(packets) + 1):
        l1, l2 = map(eval, packets[i-1].split("\n"))
        if cmp(l1, l2) > 0:
            right += i
    return right 

# Insertion sort
def second_part(packets):
    L = [[[2]], [[6]]]
    for pair in packets: 
        l1, l2 = map(eval, pair.split("\n"))
        L.insert(sum(cmp(l1, e) < 0 for e in L), l1)
        L.insert(sum(cmp(l2, e) < 0 for e in L), l2)
    return (L.index([[2]]) + 1) * (L.index([[6]]) + 1)

Input = open("Inputs/Day_13.txt").read()[:-1].split("\n\n")
# Input = '''[1,1,3,1,1]
# [1,1,5,1,1]

# [[1],[2,3,4]]
# [[1],4]

# [9]
# [[8,7,6]]

# [[4,4],4,4]
# [[4,4],4,4,4]

# [7,7,7,7]
# [7,7,7]

# []
# [3]

# [[[]]]
# [[]]

# [1,[2,[3,[4,[5,6,7]]]],8,9]
# [1,[2,[3,[4,[5,6,0]]]],8,9]'''.split("\n\n")
print(first_part(Input))
print(second_part(Input))