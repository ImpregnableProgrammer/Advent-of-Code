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
    
    
    
