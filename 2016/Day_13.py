# First_Part
def First_Part(n,xf,yf):
  i=0
  l={(1,1):[[1,1]]}
  while 1:
    u={}
    for g in l:
      xo,yo=g[0],g[1]
      for q in l[g]:
        x,y=q[0],q[1]
        u[(x,y)]=[]
        if x==xf and y==yf:
          return i
        if not bin((x+y+1)*(x+y+4)-2*y+n).count('1')%2:
          u[(x,y)]+=[[x+1,y]]
        if not bin((x+y+1)*(x+y+4)-2*y-2+n).count('1')%2:
          u[(x,y)]+=[[x,y+1]]
        if not bin((x+y-1)*(x+y+2)-2*y+n).count('1')%2 and x-1>-1 and x-1!=xo:
          u[(x,y)]+=[[x-1,y]]
        if not bin((x+y-1)*(x+y+2)-2*y+2+n).count('1')%2 and y-1>-1 and y-1!=yo:
          u[(x,y)]+=[[x,y-1]]
    i+=1
    l=u

# Second Part – IN PROGRESS
def Second_Part(n):
  i=c=0
  l={(1,1):[[1,1]]}
  while i<=50:
    u={}
    for g in l:
      xo,yo=g[0],g[1]
      for q in l[g]:
        x,y=q[0],q[1]
        u[(x,y)]=[]
        if not bin((x+y+1)*(x+y+4)-2*y+n).count('1')%2:
          u[(x,y)]+=[[x+1,y]]
          c+=1
        if not bin((x+y+1)*(x+y+4)-2*y-2+n).count('1')%2:
          u[(x,y)]+=[[x,y+1]]
          c+=1
        if not bin((x+y-1)*(x+y+2)-2*y+n).count('1')%2 and x-1>-1 and x-1!=xo:
          u[(x,y)]+=[[x-1,y]]
          c+=1
        if not bin((x+y-1)*(x+y+2)-2*y+2+n).count('1')%2 and y-1>-1 and y-1!=yo:
          u[(x,y)]+=[[x,y-1]]
          c+=1
    i+=1
    l=u
  return c
    
    
    
