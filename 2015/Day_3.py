# Part One
def First_Part(I):
 H=eval(('['+'1,'*500+'],')*500);R=T=H[0][0]=0
 for i in I:
  R+=(i=='v')-(i=='^')
  T+=(i=='>')-(i=='<')
  H[R][T]=0
 print sum(map(lambda g:g.count(0),H))
 
# Part Two
def Second_Part(I):
 H=eval(('['+'1,'*500+'],')*500);H[0][0]=X=0
 D={1:[0,0],2:[0,0]}
 for i in I:
  if X%2<1:
   D[1][0]+=(i=='v')-(i=='^')
   D[1][1]+=(i=='>')-(i=='<')
   H[D[1][0]][D[1][1]]=0
  else:
   D[2][0]+=(i=='v')-(i=='^')
   D[2][1]+=(i=='>')-(i=='<')
   H[D[2][0]][D[2][1]]=0
  X+=1
 print sum(map(lambda g:g.count(0),H))
  
