def solution1(pwds):
    n = 0
    for line in pwds:
        count, letter, pwd = line.split(' ')
        a, b = map(int, count.split('-'))
        letter = letter[0]
        n += a <= pwd.count(letter) <= b
    return n

def solution2(pwds):
    n = 0
    for line in pwds:
        count, letter, pwd = line.split(' ')
        a, b = map(int, count.split('-'))
        letter = letter[0]
        n += (pwd[a-1] == letter) ^ (pwd[b-1] == letter)
    return n

pwds = '''1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc'''.split('\n')

pwds = open("Inputs/Day_02.txt", "r").read().split('\n')

print(solution1(pwds))
print(solution2(pwds))

