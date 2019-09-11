
getMonth = lambda g: int(g.split('-')[1])
getDay = lambda g: int(g.split('-')[2].split(' ')[0])
getHour = lambda g: int(g.split(' ')[1].split(':')[0])
getMin = lambda g: int(g.split(' ')[1].split(':')[1][:-1])
getGuard = lambda g: g.split(' ')[3][1:]
    
def sortRecords(records):
    Sorted = []
    records = sorted(records, key=getMonth)
    recsLen = len(records)
    mIndex = 0
    for i in range(1, recsLen + 1):
        currMonth = getMonth(records[i]) if i < recsLen else ""
        prevMonth = getMonth(records[i-1])
        if currMonth == "" or currMonth != prevMonth:
            monthRecs = sorted(records[mIndex:i], key=getDay)
            mRecsLen = len(monthRecs)
            mIndex = i
            dIndex = 0
            for j in range(1, mRecsLen + 1):
                currDay = getDay(monthRecs[j]) if j < mRecsLen else ""
                prevDay = getDay(monthRecs[j-1])
                if currDay == "" or currDay != prevDay:
                    dayRecs = sorted(monthRecs[dIndex:j], key=getHour)
                    dRecsLen = len(dayRecs)
                    dIndex = j
                    hIndex = 0
                    for k in range(1, dRecsLen + 1):
                        currHour = getHour(dayRecs[k]) if k < dRecsLen else ""
                        prevHour = getHour(dayRecs[k-1])
                        if currHour == "" or currHour != prevHour:
                            hourRecs = sorted(dayRecs[hIndex:k], key=getMin)
                            hIndex = k
                            Sorted += hourRecs
    return Sorted


def First_Part(records):
    records = sortRecords(records)
    Dict = {}
    CurrGuard = ""
    Min = 0
    for record in records:
        if "Guard" in record:
            CurrGuard = getGuard(record)
            if CurrGuard not in Dict:
                Dict[CurrGuard] = [0] * 60
        elif "asleep" in record:
           Min = getMin(record)
        elif "wakes" in record:
            currMin = getMin(record)
            Dict[CurrGuard] = Dict[CurrGuard][:Min] + [Dict[CurrGuard][i] + 1 for i in range(Min, currMin)] + Dict[CurrGuard][currMin:]
    bestGuard = max(Dict.keys(), key=lambda k:sum(Dict[k]))
    bestGuardMins = Dict[bestGuard]
    return int(bestGuard) * bestGuardMins.index(max(bestGuardMins)), Dict

def Second_Part(records):
    Dict = First_Part(records)[1]
    bestGuard = max(Dict.keys(), key=lambda k: max(Dict[k]))
    bestGuardMin = Dict[bestGuard].index(max(Dict[bestGuard]))
    return int(bestGuard) * bestGuardMin
    
# Sample Input
records = '''[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up'''.split('\n')

# My Unique Input
records = open("Inputs/Day_04.txt", "r").read()[:-1].split('\n')

print(First_Part(records)[0])
print(Second_Part(records))

