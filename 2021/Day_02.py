
def Part1(course):
    x, y = 0, 0
    for pth in course:
        drct, amt = pth.split(' ')
        amt = int(amt)
        if drct == "forward":
            x += amt
        elif drct == "down":
            y += amt
        elif drct == "up":
            y -= amt
    return x * y

def Part2(course):
    aim, x, y = 0, 0, 0
    for pth in course:
        drct, amt = pth.split(' ')
        amt = int(amt)
        if drct == "forward":
            x += amt
            y += amt * aim
        elif drct == "down":
            aim += amt
        elif drct == "up":
            aim -= amt
    return x * y

Input = open("Inputs/Day_02", 'r').read()[:-1].split('\n')
print(Part1(Input))
print(Part2(Input))
