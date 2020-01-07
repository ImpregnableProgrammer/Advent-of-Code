def First_Part(masses):
    return sum(int(mass) // 3 - 2 for mass in masses)

def Second_Part(masses):
    fuel = lambda mass, s = 0: fuel(mass // 3 - 2, s + mass // 3 - 2) if mass // 3 - 2 > 0 else s
    return sum(fuel(mass) for mass in map(int, masses))

with open("Inputs/Day_01.txt", "r") as Input:
    Input = Input.read().split("\n")[:-1]
    print(First_Part(Input))
    print(Second_Part(Input))
