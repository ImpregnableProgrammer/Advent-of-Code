def first_part(lines):
    D = dict()
    n = 0
    for line in lines:
        if line[1] == "1":
            break
        for i in range(0, len(line), 4):
            c = line[i+1]
            if 65 <= ord(c) <= 90:
                if i//4 in D:
                    D[i//4] += c
                else:
                    D[i//4] = c
        n += 1
    for i in range(n+2, len(lines)):
        print(D)
        (a, b, c) = map(int, lines[i].split(" ")[1::2])
        D[c-1] = D[b-1][:int(a)][::-1] + D[c-1]
        D[b-1] = D[b-1][int(a):]
    return ''.join(D[i][0] for i in sorted(D))

def second_part(lines):
    D = dict()
    n = 0
    for line in lines:
        if line[1] == "1":
            break
        for i in range(0, len(line), 4):
            c = line[i+1]
            if 65 <= ord(c) <= 90:
                if i//4 in D:
                    D[i//4] += c
                else:
                    D[i//4] = c
        n += 1
    for i in range(n+2, len(lines)):
        (a, b, c) = map(int, lines[i].split(" ")[1::2])
        D[c-1] = D[b-1][:int(a)] + D[c-1]
        D[b-1] = D[b-1][int(a):]
    return ''.join(D[i][0] for i in sorted(D))

Input = open("Inputs/Day_05.txt", "r").read().split('\n')[:-1]
# Input = '''    [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2'''.split('\n')
print(first_part(Input))
print(second_part(Input))
