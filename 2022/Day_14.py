def move(curr, rocks):
    c1, c2 = curr
    moves = [(c1, c2+1), (c1-1, c2+1), (c1+1, c2+1)]
    for m in moves:
        if m not in rocks:
            return m
    return curr

def first_part(paths):
    rocks = set()
    diff = lambda p1, p2: {(x, y) 
    for y in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1) 
        for x in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1)}
    abyss = 0
    for path in paths:
        path = path.split(" -> ")
        curr = tuple(map(int, path[0].split(",")))
        for p in path[1:]:
            p = tuple(map(int, p.split(",")))
            rocks.update(diff(curr, p))
            if p[1] > abyss:
                abyss = p[1]
            curr = p
    sand = []
    curr = (500, 0)
    while True:
        while move(curr, rocks) != curr:
            curr = move(curr, rocks)
            if curr[1] > abyss:
                return len(sand)
        sand.append(curr)
        rocks.add(curr)
        curr = (500, 0)

def second_part(paths):
    rocks = set()
    diff = lambda p1, p2: {(x, y) 
    for y in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1) 
        for x in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1)}
    abyss = 0
    for path in paths:
        path = path.split(" -> ")
        curr = tuple(map(int, path[0].split(",")))
        for p in path[1:]:
            p = tuple(map(int, p.split(",")))
            rocks.update(diff(curr, p))
            if p[1] > abyss:
                abyss = p[1]
            curr = p
    sand = []
    curr = (500, 0)
    while True:
        while move(curr, rocks) != curr:
            curr = move(curr, rocks)
            if curr[1] + 1 == abyss + 2:
                break
        sand.append(curr)
        rocks.add(curr)
        if curr == (500, 0):
            return len(sand)
        curr = (500, 0)

Input = open("Inputs/Day_14.txt").read()[:-1].split("\n")
Sample = '''498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9'''.split("\n")
print(first_part(Input))
print(second_part(Input))