def first_part(instr):
    cycle = 1
    X = 1
    strength = 0
    adding = 0
    val = 0
    i = 0
    while i < len(instr):
        inst = instr[i].split(" ")
        if (cycle - 20) % 40 < 1 and cycle <= 220:
            strength += cycle * X
        if adding > 0:
            X += val
            adding = 0
        elif inst[0] == "addx":
            val = int(inst[1])
            adding = 1
            i -= 1
        cycle += 1
        i += 1
    return strength

def second_part(instr):
    cycle = 1
    X = 1
    screen = [['.' for _ in range(40)] for _ in range(6)]
    adding = 0
    val = 0
    i = 0
    pos = 0
    while i < len(instr):
        inst = instr[i].split(" ")
        if pos % 40 in [X-1, X, X+1]:
            screen[pos // 40][pos % 40] = "#"
        if adding > 0:
            X += val
            adding = 0
        elif inst[0] == "addx":
            val = int(inst[1])
            adding = 1
            i -= 1
        cycle += 1
        i += 1
        pos = (pos + 1) % 240
    return '\n'.join(''.join(line) for line in screen)

Input = open("Inputs/Day_10.txt").read().split("\n")[:-1]

# Input = '''addx 15
# addx -11
# addx 6
# addx -3
# addx 5
# addx -1
# addx -8
# addx 13
# addx 4
# noop
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx -35
# addx 1
# addx 24
# addx -19
# addx 1
# addx 16
# addx -11
# noop
# noop
# addx 21
# addx -15
# noop
# noop
# addx -3
# addx 9
# addx 1
# addx -3
# addx 8
# addx 1
# addx 5
# noop
# noop
# noop
# noop
# noop
# addx -36
# noop
# addx 1
# addx 7
# noop
# noop
# noop
# addx 2
# addx 6
# noop
# noop
# noop
# noop
# noop
# addx 1
# noop
# noop
# addx 7
# addx 1
# noop
# addx -13
# addx 13
# addx 7
# noop
# addx 1
# addx -33
# noop
# noop
# noop
# addx 2
# noop
# noop
# noop
# addx 8
# noop
# addx -1
# addx 2
# addx 1
# noop
# addx 17
# addx -9
# addx 1
# addx 1
# addx -3
# addx 11
# noop
# noop
# addx 1
# noop
# addx 1
# noop
# noop
# addx -13
# addx -19
# addx 1
# addx 3
# addx 26
# addx -30
# addx 12
# addx -1
# addx 3
# addx 1
# noop
# noop
# noop
# addx -9
# addx 18
# addx 1
# addx 2
# noop
# noop
# addx 9
# noop
# noop
# noop
# addx -1
# addx 2
# addx -37
# addx 1
# addx 3
# noop
# addx 15
# addx -21
# addx 22
# addx -6
# addx 1
# noop
# addx 2
# addx 1
# noop
# addx -10
# noop
# noop
# addx 20
# addx 1
# addx 2
# addx 2
# addx -6
# addx -11
# noop
# noop
# noop'''.split("\n")

# Input = '''noop
# addx 3
# addx -5'''.split("\n")

print(first_part(Input))
print(second_part(Input))