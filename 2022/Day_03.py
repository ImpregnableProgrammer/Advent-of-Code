def first_part(sacks):
    p = 0
    for sack in sacks:
        f = sack[:len(sack)//2]
        s = sack[len(sack)//2:]
        c = set(f).intersection(s).pop()
        p += ord(c) - (38 if ord(c) < 97 else 96)
    return p

def second_part(sacks):
    p = 0
    for i in range(0, len(sacks), 3):
        c = set.intersection(*map(set, sacks[i:i+3])).pop()
        p += ord(c) - (38 if ord(c) < 97 else 96)
    return p

Input = open("Inputs/Day_03.txt").read().split("\n")[:-1]
print(first_part(Input))
print(second_part(Input))
