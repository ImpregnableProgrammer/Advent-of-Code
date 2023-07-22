
def Part1(ages):
    ages = [*map(int, ages.split(','))]
    for i in range(80):
        new = []
        for j in range(len(ages)):
            if ages[j] < 1:
                ages[j] = 6
                new.append(8)
            else:
                ages[j] -= 1
        ages += new
    return len(ages)

Sample = "3,4,3,1,2"
Input = open("Inputs/Day_06", 'r').read()
print(Part1(Input))
