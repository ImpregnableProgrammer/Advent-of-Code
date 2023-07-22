# Recursive - work backwards from end point
def first_part(grid, curr):
    l = []
    elev = lambda c: "a" if c == "S" else "z" if c == "E" else c
    for (x, y) in curr:
        if grid[x][y] == "S":
            return 0
        for (dx, dy) in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            if 0 <= x+dx < len(grid) and 0 <= y+dy < len(grid[0]) and ord(elev(grid[x][y])) - ord(elev(grid[x+dx][y+dy])) <= 1 and (x+dx, y+dy) not in l: 
                l.append((x + dx, y + dy))
    return 1 + first_part(grid, l)

# Iterative - work backwards from end point
def first_part_iter(grid, x, y):
    curr = [(x, y)]
    elev = lambda c: "a" if c == "S" else "z" if c == "E" else c
    steps = 0
    while True:
        l = []
        for (x, y) in curr:
            if grid[x][y] == "S":
                return steps
            for (dx, dy) in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                if 0 <= x+dx < len(grid) and 0 <= y+dy < len(grid[0]) and ord(elev(grid[x][y])) - ord(elev(grid[x+dx][y+dy])) <= 1 and (x+dx, y+dy) not in l: 
                    l.append((x + dx, y + dy))
        curr = l
        steps += 1

def second_part(grid, curr):
    l = []
    elev = lambda c: "a" if c == "S" else "z" if c == "E" else c
    for (x, y) in curr:
        if elev(grid[x][y]) == "a":
            return 0
        for (dx, dy) in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            if 0 <= x+dx < len(grid) and 0 <= y+dy < len(grid[0]) and ord(elev(grid[x][y])) - ord(elev(grid[x+dx][y+dy])) <= 1 and (x+dx, y+dy) not in l:
                l.append((x + dx, y + dy))
    return 1 + second_part(grid, l)

Input = open("Inputs/Day_11.txt").read().split("\n")[:-1]
# Input = '''Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi'''.split("\n")
x = sum([i if "E" in Input[i] else 0 for i in range(len(Input))])
y = Input[x].index("E")
print(first_part(Input, [(x, y)]))
print(first_part_iter(Input, x, y)) # Not much faster than recursive version, which makes sense
print(second_part(Input, [(x, y)]))