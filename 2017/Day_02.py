
# First Part

def First_Part(s):
    Sum = 0
    for row in s.split("\n"):
        Values = list(map(int, row.split("\t")))
        Sum += max(Values) - min(Values)
    return Sum

Input = open("Inputs/Day_02_Spreadsheet", "r")
print(First_Part(Input.read()))


# Second Part

def Second_Part(s):
    Sum = 0
    for row in s.split("\n"):
        Values = list(map(int, row.split("\t")))
        for i in range(len(Values)):
            for j in range(i+1, len(Values)):
                Max = max(Values[i], Values[j])
                Min = min(Values[i], Values[j])
                if not Max / Min % 1:
                    Sum += int(Max / Min)
    return Sum

Input = open("Inputs/Day_02_Spreadsheet", "r")
print(Second_Part(Input.read()))
