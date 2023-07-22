def first_part():
    return max([sum(map(int, i.split("\n"))) for i in open("Inputs/Day_01.txt", "r").read()[:-1].split("\n\n")])

def second_part():
    return sum(sorted([sum(map(int, i.split("\n"))) for i in open("Inputs/Day_01.txt", "r").read()[:-1].split("\n\n")])[-3:])

print(first_part())
print(second_part())

