# First Part
def First_Part(n,xf,yf):
  i=0
  l={(1,1):[[1,1,'']]}
  while 1:
    u={}
    for g in l:
      xo,yo=g[0],g[1]
      for q in l[g]:
        x,y=q[0],q[1]
        p=q[2]
        u[(x,y)]=[]
        if x==xf and y==yf:
          return (i,p)
        if not bin((x+y+1)*(x+y+4)-2*y+n).count('1')%2:
          u[(x,y)]+=[[x+1,y,p+'R']]
        if not bin((x+y+1)*(x+y+4)-2*y-2+n).count('1')%2:
          u[(x,y)]+=[[x,y+1,p+'D']]
        if not bin((x+y-1)*(x+y+2)-2*y+n).count('1')%2 and x-1>-1 and x-1!=xo:
          u[(x,y)]+=[[x-1,y,p+'L']]
        if not bin((x+y-1)*(x+y+2)-2*y+2+n).count('1')%2 and y-1>-1 and y-1!=yo:
          u[(x,y)]+=[[x,y-1,p+'U']]
    i+=1
    l=u
