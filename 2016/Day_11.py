# First Part
def First_Part(s):
  Reg={'a':0,'b':0,'c':0,'d':0}
  s=s.split('\n')
  i=0
  while i<len(s):
    l=s[i].split()
    if l[0]=='cpy':
      Reg[l[2]]=l[1].isdigit()and int(l[1])or Reg[l[1]]
    elif l[0]=='jnz':
      i+=((l[1].isdigit()and int(l[1]))or Reg[l[1]])and int(l[2])-1or 0
    else:
      Reg[l[1]]+=(-1)**(l[0]=='dec')
    i+=1
  print(Reg['a'])
  
# Second Part
def Second_Part(s):
  Reg={'a':0,'b':0,'c':1,'d':0}
  s=s.split('\n')
  i=0
  while i<len(s):
    l=s[i].split()
    if l[0]=='cpy':
      Reg[l[2]]=l[1].isdigit()and int(l[1])or Reg[l[1]]
    elif l[0]=='jnz':
      i+=((l[1].isdigit()and int(l[1]))or Reg[l[1]])and int(l[2])-1or 0
    else:
      Reg[l[1]]+=(-1)**(l[0]=='dec')
    i+=1
  print(Reg['a'])
        
        
