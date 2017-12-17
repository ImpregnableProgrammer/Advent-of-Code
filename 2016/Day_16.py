# First Part
def First_Part(s):
  while len(s)<272:
    s=s+'0'+s[::-1].replace('1','b').replace('0','1').replace('b','0')
  s=s[:272]
  c=''.join(sum(map(ord,s[i-2:i]))/2%1and'0'or'1'for i in range(2,273,2))
  while len(c)%2<1:
    c=''.join(sum(map(ord,c[i-2:i]))/2%1and'0'or'1'for i in range(2,len(c)+1,2))
  print(c)
  
# Second Part
def Second_Part(s,n):
  while len(s)<n:
    s=s+'0'+s[::-1].replace('1','b').replace('0','1').replace('b','0')
  s=s[:n]
  c=''.join(sum(map(ord,s[i-2:i]))/2%1and'0'or'1'for i in range(2,n+1,2))
  while len(c)%2<1:
    c=''.join(sum(map(ord,c[i-2:i]))/2%1and'0'or'1'for i in range(2,len(c)+1,2))
  print(c)
