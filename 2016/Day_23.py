# First Part
# Currently unfinished
def First_Part(s):
  Reg={'a':0,'b':0,'c':0,'d':0}
  s=s.split('\n')
  i=0
  while i<len(s):
    l=s[i].split()
    print(l)
    if l[0]=='cpy':
      if not l[2].isdigit():
        Reg[l[2]]=l[1].isdigit()and int(l[1])or Reg[l[1]]
    elif l[0]=='jnz':
      i+=int(l[2])-1 if (l[1].isdigit() and int(l[1])) or Reg[l[1]] else 0
    elif l[0]=='tgl':
      I=i+((l[1].isdigit() and int(l[1]))or Reg[l[1]])
      if len(s[I].split())>2:
        s[I]=s[I].replace('jnz','#').replace('cpy','jnz').replace('#','cpy')
      else:
        s[I]=s[i].replace('inc','#').replace('dec','inc').replace('tgl','inc').replace('#','dec')
    else:
      Reg[l[1]]+=(-1)**(l[0]=='dec')
    i+=1
  print(Reg['a'])
