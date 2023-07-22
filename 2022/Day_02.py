def first_part(rounds):
    D = {"A": {"X": (1, 3), "Y": (2, 6), "Z": (3, 0)},
        "B": {"X": (1, 0), "Y": (2, 3), "Z": (3, 6)},
        "C": {"X": (1, 6), "Y": (2, 0), "Z": (3, 3)}}
    pnts = 0
    for rnd in rounds:
        a = rnd.split(" ")[0]
        b = rnd.split(" ")[1]
        pnts += sum(D[a][b])
    return pnts

def second_part(rounds):
    D = {"A": {"X": (3, 0), "Y": (1, 3), "Z": (2, 6)},
        "B": {"X": (1, 0), "Y": (2, 3), "Z": (3, 6)},
        "C": {"X": (2, 0), "Y": (3, 3), "Z": (1, 6)}}
    pnts = 0
    for rnd in rounds:
        a = rnd.split(" ")[0]
        b = rnd.split(" ")[1]
        pnts += sum(D[a][b])
    return pnts

Input = open("Inputs/Day_02.txt", "r").read().split("\n")[:-1]
print(first_part(Input))
print(second_part(Input))


