# huh, this ended up being easy enough to do...
def first_part(moves):
    head = tail = (0, 0)
    deltas = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}
    add = lambda p1, p2: (p1[0] + p2[0], p1[1] + p2[1])
    shifts = {(dx, dy) for dx in range(-1, 2) for dy in range(-1, 2)}
    visited = set() # set of vertices visited by the tail
    for move in moves:
        dir, dist = move.split(' ')
        for _ in range(int(dist)):
            head = add(head, deltas[dir])
            grid = {add(head, shift) for shift in shifts}
            if tail not in grid:
                if tail[1] != head[1]: # different row
                    if tail[1] < head[1]:
                        tail = add(tail, (0, 1))
                    else:
                        tail = add(tail, (0, -1))
                if tail[0] != head[0]: # different column
                    if tail[0] < head[0]:
                        tail = add(tail, (1, 0))
                    else:
                        tail = add(tail, (-1, 0))
            visited.add(tail)
    return len(visited)

# Heck yeah, I got this too!! :D
def second_part(moves):
    knots = [(0, 0)] * 10 # knots[0] is head, knots[9] is next
    deltas = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}
    add = lambda p1, p2: (p1[0] + p2[0], p1[1] + p2[1])
    shifts = {(dx, dy) for dx in range(-1, 2) for dy in range(-1, 2)}
    visited = set() # set of vertices visited by next
    for move in moves:
        dir, dist = move.split(' ')
        for _ in range(int(dist)):
            knots[0] = add(knots[0], deltas[dir])
            for knot in range(0, 9):
                curr = knots[knot]
                grid = {add(curr, shift) for shift in shifts}
                next = knots[knot + 1]
                if next not in grid:
                    if next[1] != curr[1]: # different row
                        if next[1] < curr[1]:
                            next = add(next, (0, 1))
                        else:
                            next = add(next, (0, -1))
                    if next[0] != curr[0]: # different column
                        if next[0] < curr[0]:
                            next = add(next, (1, 0))
                        else:
                            next = add(next, (-1, 0))
                    knots[knot + 1] = next
            visited.add(knots[9])
    return len(visited)

Sample = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''.split('\n')
Input = open("Inputs/Day_09.txt").read().split("\n")[:-1]
print(first_part(Input))
Sample2 = '''R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20'''.split('\n')
print(second_part((Input)))
