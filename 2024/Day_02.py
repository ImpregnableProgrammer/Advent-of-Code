def parse_input(lines):
    reports = []
    for line in lines:
        reports.append([*map(int, line.split())])
    return reports


def part_one(lines):
    reports = parse_input(lines)
    safe = 0
    for line in reports:
        length = len(line)
        safe += (
            all(line[i] > line[i - 1] for i in range(1, length))
            or all(line[i] < line[i - 1] for i in range(1, length))
        ) and all(1 <= abs(line[i] - line[i - 1]) <= 3 for i in range(1, length))
    return safe


INPUT = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""".split(
    "\n"
)
INPUT = open("Inputs/Day_02.txt").read().split("\n")
print(part_one(INPUT))
