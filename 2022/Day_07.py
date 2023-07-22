def get_dirs(output):
    dirs = {"/" : dict()}
    curr = dirs
    prev = []
    for line in output:
        cmd = line.split(" ")
        if cmd[0] == "$":
            if cmd[1] == "cd":
                if cmd[2] == "..":
                    curr = prev[-1]
                    prev = prev[:-1]
                else:
                    prev += [curr]
                    curr = curr[cmd[2]]
            elif cmd[1] == "ls":
                continue
        else:
            if cmd[0] == "dir":
                curr[cmd[1]] = dict() # type: ignore
            else:
                curr[cmd[1]] = int(cmd[0])  # type: ignore
    return dirs

def first_part(output):
    dirs = get_dirs(output)
    size = lambda d: sum(d[i] if type(d[i]) == int else size(d[i]) for i in d)
    sizes = lambda d: sum([size(d) if size(d) <= 10**5 else 0] + [sizes(d[i]) if type(d[i]) != int else 0 for i in d])
    return sizes(dirs)

def second_part(output):
    dirs = get_dirs(output)
    size = lambda d: sum(d[i] if type(d[i]) == int else size(d[i]) for i in d)
    Max = 7*10**7
    free = Max - size(dirs)
    needed = 3*10**7 - free
    min_reqd = lambda d: min(([size(d)] if size(d) >= needed else []) + [min_reqd(d[i]) if type(d[i]) != int else Max for i in d])
    return min_reqd(dirs)

Input = open("Inputs/Day_07.txt").read().split("\n")[:-1]
# Input = '''$ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k'''.split("\n")
print(first_part(Input))
print(second_part(Input))
