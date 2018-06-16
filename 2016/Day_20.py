
# First Part

def Lowest_Unblocked(Blocked):
    MIN = 0
    MinOld = -1
    while MIN != MinOld:
        MinOld = MIN        
        for Range in Blocked.split("\n"):
            min, max = map(int, Range.split("-"))
            if min <= MIN and max >= MIN:
                MIN = max + 1
    return MIN

Input = open("Large_Inputs/Day_20_Blocked_IPs", "r")

print(Lowest_Unblocked(Input.read()[:-1]))


# Second Part

def Number_Allowed(Blocked):
    Blocked = [tuple(map(int, i.split("-"))) for i in Blocked.split("\n")]
    Allowed = [(0, 2**32 - 1)]
    for m in range(len(Blocked)):
        n = 0
        while n < len(Allowed):
            mStart, mEnd = Blocked[m][0], Blocked[m][1]
            nStart, nEnd = Allowed[n][0], Allowed[n][1]
            if mStart <= nStart and mEnd >= nStart and mEnd <= nEnd:
                # Truncate tuple from left
                Allowed = Allowed[:n] + [(mEnd + 1, nEnd)] + Allowed[n+1:]
            elif mStart >= nStart and mEnd <= nEnd:
                # Split tuple into two through middle
                Allowed = Allowed[:n] + [(nStart, mStart - 1), (mEnd + 1, nEnd)] + Allowed[n+1:]
                n += 1
            elif mStart >= nStart and mStart <= nEnd and mEnd >= nEnd:
                # Truncate tuple from right
                Allowed = Allowed[:n] + [(nStart, mStart - 1)] + Allowed[n+1:]
            elif mStart <= nStart and mEnd >= nEnd:
                # Remove tuple
                Allowed = Allowed[:n] + Allowed[n+1:]
                n -= 1
            n += 1
    return sum(i[1] - i[0] + 1 for i in Allowed)

Input = open("Large_Inputs/Day_20_Blocked_IPs", "r")

print(Number_Allowed(Input.read()[:-1]))

# SAMPLE INPUT
# print(Number_Allowed('''5-8
# 0-2
# 4-7'''))

            
        
    
    
