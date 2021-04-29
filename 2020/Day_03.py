def solution1(Map, dx=3, dy=1):
    rows, cols = len(Map), len(Map[0])
    x, y, trees = 0, 0, 0
    while y < rows:
        if Map[y][x] == '#': 
            trees += 1
        x = (x + dx) % cols
        y += dy
    return trees

def solution2(Map):
    slopes = zip([1,3,5,7,1], [1,1,1,1,2])
    prod = 1
    for dx, dy in slopes:
        prod *= solution1(Map, dx, dy)
    return prod

Map = '''..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#'''.split('\n')

Map = open("Inputs/Day_03.txt", "r").read().split('\n')

print(solution1(Map))
print(solution2(Map))

