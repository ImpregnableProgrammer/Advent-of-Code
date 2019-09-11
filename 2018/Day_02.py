
import re

def First_Part(ids):
    two = 0
    three = 0
    for ID in ids:
        if any(ID.count(i) == 2 for i in ID):
            two += 1
        if any(ID.count(i) == 3 for i in ID):
            three += 1
    return two * three

Input = open("Inputs/Day_02.txt", "r").read().split('\n')[:-1]
print(First_Part(Input))

def Second_Part(ids):
    for i in range(len(ids)):
        for j in range(i+1, len(ids)):
            if sum(map(lambda s: s[0] != s[1], zip(ids[i], ids[j]))) == 1:
                return ''.join(map(lambda i: i[0] * (i[0] == i[1]), zip(ids[i], ids[j])))

print(Second_Part(Input))
    
        
