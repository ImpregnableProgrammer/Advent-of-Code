
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
import re
def Second_Part(s):
  Reg={'a':12,'b':0,'c':0,'d':0}
  s=s.split('\n')
  i=0
  while i<len(s):
    s=re.sub(r"add (\w) (\w)\n@\n@\ndec (\w)\njnz \3 -5", r"add \1*\3 \2\n@\n@\n@\n@", re.sub(r"dec (\w)\ninc (\w)\njnz \1 -2", r"add \1 \2\n@\n@", re.sub(r"inc (\w)\ndec (\w)\njnz \2 -2", r"add \2 \1\n@\n@", '\n'.join(s)))).split('\n')
    l=s[i].split()
    if l[0]=='cpy' and l[2].isalpha():
      Reg[l[2]]=Reg[l[1]] if l[1].isalpha() else int(l[1])
    elif l[0] == "add":
      o=l[1].split('*')
      Reg[l[2]] += Reg[o[0]]*Reg[o[1]] if '*' in l[1] else Reg[l[1]]
    elif l[0]=='jnz':
      i+=(Reg[l[2]]-1 if l[2].isalpha() else int(l[2])-1) if (l[1].isalpha() and Reg[l[1]]) or (not l[1].isalpha() and int(l[1])) else 0
    elif l[0]=='tgl':
      I=i+(Reg[l[1]] if l[1].isalpha() else int(l[1]))
      if I<len(s):
        if len(s[I].split())>2:
          s[I]=s[I].replace('jnz','#').replace('cpy','jnz').replace('#','cpy')
        else:
          s[I]=s[I].replace('inc','#').replace('dec','inc').replace('tgl','inc').replace('#','dec')
    elif l[0] == 'inc' or l[0] == 'dec':
      Reg[l[1]]+=(-1)**(l[0]=='dec')
    i+=1
  print(Reg['a'])

Second_Part('''cpy a b
dec b
cpy a d
cpy 0 a
cpy b c
inc a
dec c
jnz c -2
dec d
jnz d -5
dec b
cpy b c
cpy c d
dec d
inc c
jnz d -2
tgl c
cpy -16 c
jnz 1 c
cpy 73 c
jnz 82 d
inc a
inc d
jnz d -2
inc c
jnz c -5''')
