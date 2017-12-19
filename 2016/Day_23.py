# First Part
def First_Part(s):
  Reg={'a':7,'b':0,'c':0,'d':0}
  s=s.split('\n')
  i=0
  while i<len(s):
    l=s[i].split()
    if l[0]=='cpy' and l[2].isalpha():
      Reg[l[2]]=Reg[l[1]] if l[1].isalpha() else int(l[1])
    elif l[0]=='jnz':
      i+=(Reg[l[2]]-1 if l[2].isalpha() else int(l[2])-1) if (l[1].isalpha() and Reg[l[1]]) or (not l[1].isalpha() and int(l[1])) else 0
    elif l[0]=='tgl':
      I=i+(Reg[l[1]] if l[1].isalpha() else int(l[1]))
      if I<len(s):
        if len(s[I].split())>2:
          s[I]=s[I].replace('jnz','#').replace('cpy','jnz').replace('#','cpy')
        else:
          s[I]=s[I].replace('inc','#').replace('dec','inc').replace('tgl','inc').replace('#','dec')
    else:
      Reg[l[1]]+=(-1)**(l[0]=='dec')
    i+=1
  print(Reg['a'])
  
# Second Part
# Currently unfinished – Takes too long
def Second_Part(s):
  Reg={'a':12,'b':0,'c':0,'d':0}
  s=s.split('\n')
  i=0
  while i<len(s):
    l=s[i].split()
    if l[0]=='cpy' and l[2].isalpha():
      Reg[l[2]]=Reg[l[1]] if l[1].isalpha() else int(l[1])
    elif l[0]=='jnz':
      i+=(Reg[l[2]]-1 if l[2].isalpha() else int(l[2])-1) if (l[1].isalpha() and Reg[l[1]]) or (not l[1].isalpha() and int(l[1])) else 0
    elif l[0]=='tgl':
      I=i+(Reg[l[1]] if l[1].isalpha() else int(l[1]))
      if I<len(s):
        if len(s[I].split())>2:
          s[I]=s[I].replace('jnz','#').replace('cpy','jnz').replace('#','cpy')
        else:
          s[I]=s[I].replace('inc','#').replace('dec','inc').replace('tgl','inc').replace('#','dec')
    else:
      Reg[l[1]]+=(-1)**(l[0]=='dec')
    i+=1
  print(Reg['a'])
