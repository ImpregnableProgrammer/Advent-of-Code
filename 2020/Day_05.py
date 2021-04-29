def sol1(passes):
    ids = set()
    for Pass in passes.split('\n'):
        row_min, row_max = 0, 127
        for i in Pass[:7]:
            row_min = (row_min + row_max) // 2 if i == 'B' else row_min
            row_max = (row_min + row_max) // 2 if i == 'F' else row_max
        col_min, col_max = 0, 7
        for i in Pass[-3:]:
            col_min = (col_min + col_max) // 2 if i == 'R' else col_min
            col_max = (col_min + col_max) // 2 if i == 'L' else col_max
        ids.add(row_max * 8 + col_max)
    return max(ids)

samp_passes = '''BFFFBBFRRR'''
passes = open("Inputs/Day_05.txt", 'r').read()

print(sol1(passes))