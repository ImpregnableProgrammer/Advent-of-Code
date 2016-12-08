# Part One
First_Part=lambda f:''.join([sorted('abcdefghijklmnopqrstuvwxyz',key=[q[l]for q in f.split('\n')].count)[-1]for l in range(8)])

# Part Two
Second_Part=lambda f,g=lambda b,l:[q[l]for q in b.split('\n')]:''.join([sorted(set(g(f,l)),key=g(f,l).count)[0]for l in range(8)])
