# First_Part
def First_Part(n,x=1,y=1,xo=1,yo=1,c=0):
  if x!=7 or y!=4:
    if bin((x+y+1)*(x+y+4)-2*y+n).count('1')%2<1 and x+1!=xo:
      #print(1)
      First_Part(n,x+1,y,x,y,c+1)
    if bin((x+y+1)*(x+y+4)-2*y+n-2).count('1')%2<1 and y+1!=yo:
      #print(2)
      First_Part(n,x,y+1,x,y,c+1)
    if bin((x+y-1)*(x+y+2)-2*y+n).count('1')%2<1 and x-1!=xo:
      #print(3)
      First_Part(n,x-1,y,x,y,c+1)
    if bin((x+y+1)*(x+y+2)-2*y+n+2).count('1')%2<1 and y-1!=yo:
      #print(4)
      First_Part(n,x,y-1,x,y,c+1)
  else:
    return c
  
def First_Part(n,xf,yf):
  i=0
  l=[[1,1]]
  while 1:
    u=[]
    for g in l:
      x,y=g[0],g[1]
      if x==xf and y==yf:
        return i
      if not bin((x+y+1)*(x+y+4)-2*y+n).count('1')%2:
        u+=[[x+1,y]]
      if not bin((x+y+1)*(x+y+4)-2*y-2+n).count('1')%2:
        u+=[[x,y+1]]
      if not bin((x+y-1)*(x+y+2)-2*y+n).count('1')%2:
        u+=[[x-1,y]]
      if not bin((x+y-1)*(x+y+2)-2*y+2+n).count('1')%2:
        u+=[[x,y-1]]
    i+=1
    l=u
    
    
    
