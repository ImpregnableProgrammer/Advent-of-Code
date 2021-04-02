
def Solution(report, cmax, n = 2020, c = 0, prod=1):
    if n < 0 or c > cmax:
        return None
    elif n > 0:
        for i in range(len(report)):
            p = Solution(report[i+1:], cmax, n - report[i], c + 1, prod * report[i])
            if p != None: return p
        return None
    return prod

e = '''1721
979
366
299
675
1456'''

e = open("Inputs/Day_01.txt", "r").read()

# First part
print(Solution([*map(int, e.split('\n'))], 2))

# Second part
print(Solution([*map(int, e.split('\n'))], 3))
    


