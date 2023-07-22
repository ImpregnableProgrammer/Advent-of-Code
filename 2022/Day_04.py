def first_part(pairs):
    n = 0
    for pair in pairs:
        (a, b) = map(int, pair.split(",")[0].split("-"))
        (c, d) = map(int, pair.split(",")[1].split("-"))
        n += a <= c <= d <= b or c <= a <= b <= d
    return n

def second_part(pairs):
    n = 0
    for pair in pairs:
        (a, b) = map(int, pair.split(",")[0].split("-"))
        (c, d) = map(int, pair.split(",")[1].split("-"))
        n += a <= c <= d <= b or c <= a <= b <= d or c <= a <= d <= b or a <= c <= b <= d
    return n

Input = open("Inputs/Day_04.txt", "r").read().split('\n')[:-1]
print(first_part(Input))
print(second_part(Input))