
import re
def First_Part(Range):
    a, b = Range
    pwds = 0
    for c in map(str, range(a, b + 1)):
        if all(c[j] <= c[j+1] for j in range(len(c) - 1)) and re.search(r"(\d)\1", c):
            pwds += 1
    return pwds

# No strings - Too inefficient (takes too long)
def First_Part_No_Strings(Range):
    a, b = Range
    pwds = 0
    for c in range(a, b + 1):
        m = c
        pow_10 = 0
        while m > 0:
            m /= 10
            pow_10 += 1
        if all((c // (10 ** j)) % 10 >= (c // (10 ** (j + 1))) % 10 for j in range(pow_10)) and any((c // (10 ** j)) % 10 == (c // (10 ** (j + 1))) % 10 for j in range(pow_10)):
            pwds += 1
    return pwds

def Second_Part(Range):
    a, b = Range
    pwds = 0
    for c in map(str, range(a, b + 1)):
        m = re.findall(r"(\d)\1", c)
        if all(c[j] <= c[j+1] for j in range(len(c) - 1)) and any(re.search(r"" + q + "{2}", c) and not re.search(r"" + q + "{3,}", c) for q in m):
            pwds += 1
    return pwds
    
Input = list(map(int, "256310-732736".split("-")))

print(First_Part(Input))
print(Second_Part(Input))
