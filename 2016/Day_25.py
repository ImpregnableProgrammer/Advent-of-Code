
# First Part
import re
def First_Part(s):
  s=s.split('\n')
  n=0
  while 1:
    Reg={'a': n,'b':0,'c':0,'d':0}
    i=0
    Z=[0, 1]
    while Z[-2:] == [0, 1] or Z[-2:] == [1, 0]:
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
      elif l[0] == 'out':
        Z += [Reg[l[1]] if l[1].isalpha() else int(l[1])]
        print(n, Z[-1])
      i+=1
    n+=1
    print()
    
First_Part('''cpy a d
cpy 4 c
cpy 643 b
inc d
dec b
jnz b -2
dec c
jnz c -5
cpy d a
jnz 0 0
cpy a b
cpy 0 a
cpy 2 c
jnz b 2
jnz 1 6
dec b
dec c
jnz c -4
inc a
jnz 1 -7
cpy 2 b
jnz c 2
jnz 1 4
dec b
dec c
jnz 1 -4
jnz 0 0
out b
jnz a -19
jnz 1 -21''')
