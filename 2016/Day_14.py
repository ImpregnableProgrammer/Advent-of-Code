from hashlib import *
import re

# First Part
def First_Part(s):
  p=i=0;
  while p<64:
    z=re.search(r'(.)\1{2}',md5(bytes(s+str(i),'utf8')).hexdigest())
    if z:
      for u in range(i+1,i+1001):
        if z.group()[0]*5 in md5(bytes(s+str(u),'utf8')).hexdigest():
          p+=1
    i+=1
  print(i-1)
  
# Second Part
def Key_Stretching(s):
  for i in range(2017):
    s=md5(bytes(s,'utf8')).hexdigest()
  return s

def Second_Part(s):
  p=i=0;
  Hash_dict={}
  while p<64:
    try:
      z=re.search(r'(.)\1{2}',Hash_dict[s+str(i)])
    except:
      m=Hash_dict[s+str(i)]=Key_Stretching(s+str(i))
      z=re.search(r'(.)\1{2}',m)
    if z:
      for u in range(i+1,i+1001):
        try:
           x=Hash_dict[s+str(u)]
        except:
           x=Hash_dict[s+str(u)]=Key_Stretching(s+str(u))
        if z.group()[0]*5 in x:
          p+=1
    i+=1
  print(i-1)
