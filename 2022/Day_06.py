def first_part(stream):
    for i in range(len(stream)-4):
        if len(set(stream[i:i+4])) == 4:
            return i+4

def second_part(stream, d):
    for i in range(len(stream)-d):
        if len(set(stream[i:i+d])) == d:
            return i+d

Input = open("Inputs/Day_06.txt").read()
print(first_part(Input))
print(second_part(Input, 14))