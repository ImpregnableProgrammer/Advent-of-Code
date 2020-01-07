def First_Part(paths):
    coords_sets = tuple()
    for path in paths:
        i, j = 0, 0
        coords = set()
        for move in path:
            s = int(move[1:])
            c = move[0]
            if c == "R":
                for a in range(j + 1, j + s + 1):
                    coords.add((i, a))
                j += s
            elif c == "D":
                for a in range(i + 1, i + s + 1):
                    coords.add((a, j))
                i += s
            elif c == "L":
                for a in range(j - s, j):
                    coords.add((i, a))
                j -= s
            else:
                for a in range(i - s, i):
                    coords.add((a, j))
                i -= s
        coords_sets += (coords,)
    a, b = coords_sets
    sum_abs = lambda l: sum(abs(i) for i in l)
    return sum_abs(min(a & b, key = sum_abs))

def Second_Part(paths):
    coords_sets = tuple()
    for path in paths:
        i, j = 0, 0
        coords = dict()
        steps = 0
        for move in path:
            s = int(move[1:])
            c = move[0]
            if c == "R":
                for a in range(j, j + s):
                    steps += 1
                    coords.setdefault((i, a + 1), steps)
                j += s
            elif c == "D":
                for a in range(i, i + s):
                    steps += 1
                    coords.setdefault((a + 1, j), steps)
                i += s
            elif c == "L":
                for a in range(j, j - s, -1):
                    steps += 1
                    coords.setdefault((i, a - 1), steps)
                j -= s
            else:
                for a in range(i, i - s, -1):
                    steps += 1
                    coords.setdefault((a - 1, j), steps)
                i -= s
        coords_sets += (coords,)
    a, b = coords_sets
    return min(a[g] + b[g] for g in a.keys() & b.keys())

# Small test cases
paths = [i.split(",") for i in """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83""".split("\n")]

paths = ["R8,U5,L5,D3".split(','), "U7,R6,D4,L4".split(',')]

# Main test case
with open("Inputs/Day_03.txt", "r") as Input:
    paths = [path.split(",") for path in Input.read().split("\n")][:-1]
    print(First_Part(paths))
    print(Second_Part(paths))

