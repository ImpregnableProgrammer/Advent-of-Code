# Part One
def First_Part(B):
 V = N = D = 0
 for i in B.split(', '):
  if D % 360 == 0:
   N = N - int(i[1:]) if i[0]=='L' else N + int(i[1:])
  elif D % 360 == 90:
   V = V + int(i[1:]) if i[0]=='L' else V - int(i[1:])
  elif D % 360 == 180:
   N = N + int(i[1:]) if i[0]=='L' else N - int(i[1:])
  elif D % 360 == 270:
   V = V - int(i[1:]) if i[0]=='L' else V + int(i[1:])
  D = D + 90 if i[0]=='R' else D - 90
 print(abs(V) + abs(N))
 
# Part Two
def Second_Part(B):
 V = N = D = 0
 H = eval(('['+'1,'*500+'],')*500)
 A = 0
 for i in B.split(', '):
  o , p = V , N
  if D % 360 == 0:
   N = N - int(i[1:]) if i[0]=='L' else N + int(i[1:])
  elif D % 360 == 90:
   V = V + int(i[1:]) if i[0]=='L' else V - int(i[1:])
  elif D % 360 == 180:
   N = N + int(i[1:]) if i[0]=='L' else N - int(i[1:])
  elif D % 360 == 270:
   V = V - int(i[1:]) if i[0]=='L' else V + int(i[1:])
  D = D + 90 if i[0]=='R' else D - 90
  for i in range(p,N,1-2*(N<p)):
   if H[o][i]==0:
    A += abs(o) + abs(i)
   H[o][i]=0
  for x in range(o,V,1-2*(V<o)):
   if H[x][N]==0:
    A += abs(x) + abs(N)
   H[x][N]=0
  if A > 0:
   break
 print(A)
