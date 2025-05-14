import numpy as np


def parse_input(lines):
    array = np.ndarray((0, 2), dtype=np.uint32)
    for line in lines:
        array = np.append(array, [[*map(int, line.split("   "))]], axis=0)
    return array


def part_one(lines):
    array = parse_input(lines)
    return np.sum(np.diff(np.sort(array, axis=0)))


def part_two(lines):
    array = parse_input(lines)
    return sum(i * np.count_nonzero(i == array[:, 1]) for i in np.unique(array[:, 0]))


INPUT = """3   4
4   3
2   5
1   3
3   9
3   3""".split(
    "\n"
)
INPUT = open("Inputs/Day_01.txt").read().split("\n")
print(part_one(INPUT))
print(part_two(INPUT))

# Fancy matrix in Fira Code font!
A = """
⎧1 2 5⎫   ⎧1 3 5⎫
⎨2 3 6⎬ x ⎨2 3 6⎬
⎩3 4 7⎭   ⎩3 9 7⎭
"""
