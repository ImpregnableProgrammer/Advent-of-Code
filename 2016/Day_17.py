# First Part
from hashlib import *
def First_Part(n):
  l={'':[0,0]}
  while 1:
    u={}
    for p in l:
      x,y=l[p][0],l[p][1]
      hash=md5(bytes(n+p,'utf8')).hexdigest()
      if x==3 and y==3:
        return p
      if 'b'<=hash[3]<='f' and x+1<4:
        u[p+'R']=[x+1,y]
      if 'b'<=hash[1]<='f' and y+1<4:
        u[p+'D']=[x,y+1]
      if 'b'<=hash[2]<='f' and x-1>-1:
        u[p+'L']=[x-1,y]
      if 'b'<=hash[0]<='f' and y-1>-1:
        u[p+'U']=[x,y-1]
    l=u
    
# Second Part
def Second_Part(n):
  l={'':[0,0]}
  T=0
  while 1:
    u={}
    for p in l:
      x,y=l[p][0],l[p][1]
      if x==3 and y==3:
        T=len(p)
      else:
        hash=md5(bytes(n+p,'utf8')).hexdigest()
        if 'b'<=hash[3]<='f' and x+1<4:
          u[p+'R']=[x+1,y]
        if 'b'<=hash[1]<='f' and y+1<4:
         u[p+'D']=[x,y+1]
        if 'b'<=hash[2]<='f' and x-1>-1:
         u[p+'L']=[x-1,y]
        if 'b'<=hash[0]<='f' and y-1>-1:
          u[p+'U']=[x,y-1]
    if len(u)<1:
      return T
    l=u
