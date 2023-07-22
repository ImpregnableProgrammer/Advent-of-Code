# First Part

def Part1(depths):
    return sum(depths[i] > depths[i-1] for i in range(1, len(depths)))

def Part2(depths):
    return sum(sum(depths[i:i+3]) < sum(depths[i+1:i+4]) for i in range(len(depths) - 3))

Input = [*map(int, open("Inputs/Day_01", "r").read().split('\n')[:-1])]
print(Part1(Input)) #1681 
print(Part2(Input)) #1704
