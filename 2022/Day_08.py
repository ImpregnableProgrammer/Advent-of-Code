def first_part(grid):
    h = len(grid)
    w = len(grid[0])
    visible = lambda r, c: all(grid[i][c] < grid[r][c] for i in range(r)) or all(grid[i][c] < grid[r][c] for i in range(r+1, h)) or all(grid[r][i] < grid[r][c] for i in range(c)) or all(grid[r][i] < grid[r][c] for i in range(c+1, w))
    count = 0
    for r in range(1, h-1):
        for c in range(1, w-1):
            count += visible(r, c)
    return count + 2*h + 2*w - 4

def second_part(grid):
    h = len(grid)
    w = len(grid[0])
    f = lambda l: 1 in l and l.index(1)+1 or len(l)
    score = lambda r, c: f([grid[i][c] >= grid[r][c] for i in range(r)][::-1]) * f([grid[r][c] <= grid[i][c] for i in range(r+1, h)]) * f([grid[r][i] >= grid[r][c] for i in range(c)][::-1]) * f([grid[r][c] <= grid[r][i] for i in range(c+1, w)]) 
    return max(score(r, c) for c in range(w) for r in range(h))

Input = open("Inputs/Day_08.txt").read().split("\n")[:-1]
# Input = '''30373
# 25512
# 65332
# 33549
# 35390'''.split("\n")
print(first_part(Input))
print(second_part(Input))
