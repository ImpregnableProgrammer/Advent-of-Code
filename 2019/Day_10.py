
def Asteroid_Coords(Map):
    Coords = []
    for i in range(len(Map)):
        for j in range(len(Map[0])):
            if Map[i][j] == '#':
                Coords.append((j, i))
    return Coords

import random
def Random_Map(w, h, n):
    assert n <= w * h
    Map = []
    for k in range(h):
        Map.append(['.'] * w)
    xCoords = random.sample([*range(w)] * h, n)
    yCoords = random.sample([*range(h)] * w, n)
    Coords = [*zip(xCoords, yCoords)]
    for x, y in Coords:
        Map[y][x] = '#'
    return '\n'.join(''.join(l) for l in Map)

def First_Part(Map):
    Coords = {i:0 for i in Asteroid_Coords(Map)}
    for x, y in Coords:
        slopes = set()
        for x1, y1 in Coords:
            if (x1, y1) != (x, y):
                slopes.add(((y1 - y)/(x1 - x) if x1 != x else 'inf', y1 > y, x1 > x))
        Coords[(x, y)] = len(slopes)
    return max(Coords.items(), key = lambda t:t[1])

def Second_Part(Map, n):
    xBest, yBest = First_Part(Map)[0]
    Coords = Asteroid_Coords(Map)
    slope_dict = dict()
    for x, y in Coords:
        if (x, y) != (xBest, yBest):
            Entry = ((y - yBest)/(x - xBest) if x != xBest else 1e99 if y > yBest else -1e99, y >= yBest, x >= xBest)
            slope_dict[Entry] = slope_dict.setdefault(Entry, []) + [(x, y)]
    for e in slope_dict:
        slope_dict[e] = sorted(slope_dict[e], key = lambda f: ((f[0] - xBest)**2 + (f[1] - yBest)**2)**.5)
    Groupings = [(0, 1), (1, 1), (1, 0), (0, 0)]
    Groups = [sorted([(s, xG, yG) for s, xG, yG in slope_dict.keys() if (xG, yG) == G], key = lambda h: h[0]) for G in Groupings]
    coord_groups = [slope_dict[m] for G in Groups for m in G]
    max_len, m = len(max(coord_groups, key = len)), 0
    for k in range(max_len):
        for c in coord_groups:
            if k < len(c):
                m += 1
                if m == n:
                    x, y = c[k]
                    return x * 100 + y
    return coord_groups
    
import time
def Animate(Map):
    xB, yB = First_Part(Map)[0]
    coord_groups = Second_Part(Map, 0)
    print(coord_groups)
    Map = [list(l) for l in Map]
    Map[yB][xB] = 'X'
    max_len = len(max(coord_groups, key = len))
    for k in range(max_len):
        for c in coord_groups:
            if k < len(c):
                x, y = c[k]
                Map[y][x] = '*'
                Map1 = [p[:] for p in Map[:]]
                slope1 = (y - yB) / (x - xB) if x != xB else 'inf'
                for a in range(xB, x + (-1) ** (x < xB), (-1) ** (x < xB)):
                    for b in range(yB, y + (-1) ** (y < yB), (-1) ** (y < yB)):
                        slope2 = (b - yB) / (a - xB) if a != xB else 'inf'
                        if slope2 == slope1 and (a, b) not in ((xB, yB), (x, y)):
                            Map[b][a] = 'O'
                print('\n'.join(''.join(l) for l in Map))
                Map1[y][x] = '.'
                Map = Map1
                time.sleep(.1)
                print("\033[2J")
        
# (3, 4), 8
Map1 = """.#..#
.....
#####
....#
...##""".split('\n')

# (5, 8), 33
Map2 = """......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####""".split('\n')

# (11, 13), 210
Map3 = """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##""".split('\n')

MapM = open("Inputs/Day_10.txt", "r").read().split('\n')[:-1]

print(First_Part(MapM))
print(Second_Part(MapM, 200))

# Animate the meteors getting obliterated on a random map (in ASCII)!
#MapR = Random_Map(60, 60, 100).split('\n')
#Animate(MapR)
