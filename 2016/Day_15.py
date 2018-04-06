
import re

def Time(s):
  Discs = [tuple(map(int,re.findall("(?<=\[)\d+|\d+(?=\])",i.replace(" positions","]").replace("position ","[")))) for i in s.split("\n")]
  i = 1
  while 1:
    t = Discs[0][0]*i - Discs[0][1] - 1
    if t > 0:
      Equal = True
      for j in range(1, len(Discs)):
        a = (t + Discs[j][1] + j + 1) / Discs[j][0]
        if a % 1:
          Equal = False
          break
      if Equal:
        return t
    i += 1



# Part One -- OUTPUTS CORRECT ANSWER OF 16824
print(Time('''Disc #1 has 17 positions; at time=0, it is at position 5.
Disc #2 has 19 positions; at time=0, it is at position 8.
Disc #3 has 7 positions; at time=0, it is at position 1.
Disc #4 has 13 positions; at time=0, it is at position 7.
Disc #5 has 5 positions; at time=0, it is at position 1.
Disc #6 has 3 positions; at time=0, it is at position 0.'''))

# Part Two -- OUTPUTS CORRECT ANSWER OF 3543984
print(Time('''Disc #1 has 17 positions; at time=0, it is at position 5.
Disc #2 has 19 positions; at time=0, it is at position 8.
Disc #3 has 7 positions; at time=0, it is at position 1.
Disc #4 has 13 positions; at time=0, it is at position 7.
Disc #5 has 5 positions; at time=0, it is at position 1.
Disc #6 has 3 positions; at time=0, it is at position 0.
Disc #7 has 11 positions; at time=0, it is at position 0'''))
