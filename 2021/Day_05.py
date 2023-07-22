
def Part1(lines):
    Coords = dict()
    for line in lines:
        x, y = line.split(" -> ")
        x, y = x.split(','), y.split(',')
        if x[0] == y[0] or x[1] == y[1]:
            same = int(x[0] if x[0] == y[0] else x[1])
            xp, yp = map(int, (x[1], y[1]) if x[0] == y[0] else (x[0], y[0]))
            for lp in range(xp, yp+(-1)**(xp>yp), (-1)**(xp>yp)):
                Coord = (same, lp) if x[0] == y[0] else (lp, same)
                Coords[Coord] = 1 if Coord not in Coords else Coords[Coord] + 1
    return len([c for c in Coords if Coords[c] > 1])

# Initial attempt - Implemented wrong way
# NOT a double for-range loop
#def Part2(lines):
#   Coords = dict()
#    for line in lines:
#        x, y = line.split(" -> ")
#        x, y = [*map(int, x.split(','))], [*map(int, y.split(','))]
#        for xp in range(x[0], y[0]+(-1)**(x[0]>y[0]), (-1)**(x[0]>y[0])):
#            for yp in range(x[1], y[1]+(-1)**(x[1]>y[1]), (-1)**(x[1]>y[1])):
#                Coords[(xp, yp)] = 1 if (xp, yp) not in Coords else Coords[(xp, yp)] + 1
#    return len([c for c in Coords if Coords[c] > 1])

def Part2(lines):
    Coords = dict()
    for line in lines:
        x, y = line.split(" -> ")
        x, y = [*map(int, x.split(','))], [*map(int, y.split(','))]
        if x[0] == y[0] or x[1] == y[1]:
            same = int(x[0] if x[0] == y[0] else x[1])
            xp, yp = map(int, (x[1], y[1]) if x[0] == y[0] else (x[0], y[0]))
            for lp in range(xp, yp+(-1)**(xp>yp), (-1)**(xp>yp)):
                Coord = (same, lp) if x[0] == y[0] else (lp, same)
                Coords[Coord] = 1 if Coord not in Coords else Coords[Coord] + 1
        else:
            coords = zip(range(x[0], y[0]+(-1)**(x[0]>y[0]), (-1)**(x[0]>y[0])), range(x[1], y[1]+(-1)**(x[1]>y[1]), (-1)**(x[1]>y[1])))
            for crd in coords:
                Coords[crd] = 1 if crd not in Coords else Coords[crd] + 1
    return len([c for c in Coords if Coords[c] > 1])

Sample = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""".split('\n')
Input = open("Inputs/Day_05", 'r').read()[:-1].split('\n')
print(Part1(Input))
print(Part2(Input))
