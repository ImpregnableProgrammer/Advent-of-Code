
def First_Part(p):
    i = 0
    while i < len(p) - 1:
        if abs(ord(p[i]) - ord(p[i+1])) == 32:
            p = p[:i] + p[i+2:]
            i -= 2
        i += 1
    return len(p)

def Second_Part(p):
    chrs = set(map(str.lower, p))
    lens = []
    for char in chrs:
        pMod = ''.join(''.join(p.split(char)).split(char.upper()))
        lens += [First_Part(pMod)]
    return min(lens)

#polymer = "dabAcCaCBAcCcaDA"
#polymer = "abBA"
polymer = open("Inputs/Day_05.txt", "r").read()[:-1]
print("Initial Polymer length:", len(polymer))
print(First_Part(polymer))
print(Second_Part(polymer))    
