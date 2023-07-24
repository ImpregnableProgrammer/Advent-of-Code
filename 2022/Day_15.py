def first_part(sensors, row):
    max, min = 0, 0
    for sensor in sensors:
        sensor = sensor.split(' ')
        x1, y1 = map(int, (sensor[2][2:-1], sensor[3][2:-1]))
        x2, y2 = map(int, (sensor[8][2:-1], sensor[9][2:]))
        # |row-y1| - |x2-x1| - |y2-y1| <= x-x1 <= |x2-x1| + |y2-y1| - |row-y1|
        c = abs(x2 - x1) + abs(y2 - y1) - abs(row - y1)
        a, b = x1 - c, x1 + c
        if b > max: max = b
        if a < min: min = a
    # print((min, max))
    return max - min

# merge overlapping intervals in `intvls`
# @param `intvls` in the format [(a1, b1), (a2, b2), ...]
# merge overlapping intervals like (1, 3), (2, 6) into (1, 6)
# this was pretty difficult to figure out, but I got it eventually like always
def merge_overlaps(intvls):
    # const overlapping = True
    no_overlap = 0 # keep track of runs of intervals with no overlap with the others
    while no_overlap < len(intvls):
        a, b = intvls.pop(0)
        no_overlap += 1
        new_intvls = list()
        while len(intvls):
            c, d = intvls.pop(0)
            if d >= a and c <= b:
                if c < a: a = c
                if d > b: b = d
                no_overlap = 0 # there was an overlap, so reset the count
            else:
                new_intvls.append((c, d))
        new_intvls.append((a, b))
        intvls = new_intvls
    return intvls

# Find and return integers not covered by intervals in `intvls`
# For instance, find_gaps([(1, 2), (6, 8), (11, 13)]) == (3, 4, 5, 9, 10)
# This assumes the intervals are already sorted in order bn <= a(n+1)
# This also finds gaps in the ranges (min, a1) and (bn, max)
# Assumes: len(intvls) > 0
def find_gaps(min, intvls, max):
    assert len(intvls) > 0, "Empty interval list!"
    integers = tuple(range(min, intvls[0][0]))
    for i in range(len(intvls)-1):
        _, b = intvls[i]
        c, _ = intvls[i+1]
        integers += tuple(range(b+1, c))
    integers += tuple(range(intvls[-1][1]+1, max+1))
    return integers

# 7/24/23 at 10:45 AM: Gottem!! :D
def second_part(sensors, pos_min, pos_max):
    # |y-y1| + |x-x1| <= |y2-y1| + |x2-x1|
    # let y=row be given, then solve for x in inequality
    gaps = dict() # Mapping of {row: integers of missing values}
    for row in range(pos_min, pos_max+1):
        row_ranges = list()
        for sensor in sensors:
            sensor = sensor.split(' ')
            x1, y1 = map(int, (sensor[2][2:-1], sensor[3][2:-1]))
            x2, y2 = map(int, (sensor[8][2:-1], sensor[9][2:]))
            # |row-y1| - |x2-x1| - |y2-y1| <= x-x1 <= |x2-x1| + |y2-y1| - |row-y1|
            c = abs(x2-x1) + abs(y2-y1) - abs(row-y1)
            a, b = x1-c, x1+c
            if b > a: row_ranges.append((a, b)) # find non-overlaps between ranges for each row
        merged = sorted(merge_overlaps(row_ranges), key=lambda a: a[1])
        gap = find_gaps(pos_min, merged, pos_max)
        if len(gap) > 0:
            gaps[row] = gap
    return [gaps[i][0] * 4000000 + i for i in gaps if len(gaps[i]) > 0]

Sample = '''Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3'''.split('\n')
Input = open("Inputs/Day_15.txt").read().split('\n')
print(first_part(Sample, 10)) # 26
print(first_part(Input, 2000000))
print(second_part(Sample, 0, 20)) # [56000011]
print(second_part(Input, 0, 4000000))