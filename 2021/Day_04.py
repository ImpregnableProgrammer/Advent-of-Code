
def Part1(game):
    Nums = game[0].split(',')
    grids = []
    for i in range(1, len(game), 6):
        grid = []
        for j in range(i+1, i+6):
            grid.append(game[j].split())
        for n in range(len(grid[0])):
            line = []
            for j in range(5):
                line.append(grid[j][n])
            grid.append(line)
        grids.append(grid)
    for k in range(1, len(Nums)):
        curr = Nums[:k]
        for grid in grids:
            if any(all(i in curr for i in line) for line in grid):
                return sum(sum(int(i) for i in line if i not in curr) for line in grid[:5]) * int(curr[-1])


def Part2(game):
    Nums = game[0].split(',')
    grids = []
    for i in range(1, len(game), 6):
        grid = []
        for j in range(i+1, i+6):
            grid.append(game[j].split())
        for n in range(len(grid[0])):
            line = []
            for j in range(5):
                line.append(grid[j][n])
            grid.append(line)
        grids.append(grid)
    winners = []
    for k in range(1, len(Nums)):
        curr = Nums[:k]
        remove = []
        for grid in grids:
            if any(all(i in curr for i in line) for line in grid):
                winners.append((curr, grid))
                remove.append(grid)
        for winner in remove:
            grids.remove(winner)
    return sum(sum(int(i) for i in line if i not in winners[-1][0]) for line in winners[-1][1][:5]) * int(winners[-1][0][-1])

Sample = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7""".split('\n')

Input = open("Inputs/Day_04", 'r').read()[:-1].split('\n')
print(Part1(Input))
print(Part2(Input))
