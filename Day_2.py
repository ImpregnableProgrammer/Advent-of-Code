# For Part One
def First_Part(i):
 f=4
 u="123456789"
 for m in i.split('\n'):
  for t in m:
   f=(t=='L')and f-(f%3>0)or (t=='R')and f+((f+1)%3>0)or (t=='U')and f-3*(f>2)or (t=='D')and f+3*(f<6)
  print(end=u[f])
 print()

# For Part Two
def Second_Part(i):
 f=10
 u="  1   234 56789 ABC   D  "
 for m in i.split():
  for t in m:
   f=(t=='L')and f-(f not in[2,6,10,16,22])or (t=='R')and f+(f not in[2,8,14,18,22])or (t=='U')and f-5*(u[f-5*(f>4)]!=' 'and f>4)or (t=='D')and f+5*(u[f+5*(f<20)]!=' 'and f<20)
  print(end=u[f])
 print()
