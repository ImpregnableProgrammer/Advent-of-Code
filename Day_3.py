# For Part One
def First_Part(B):
 Z=0
 for i in B.split('\n'):
  Z+=all((int(i.split()[h[0]])+int(i.split()[h[1]]))>int(i.split()[h[2]])for h in([0,1,2],[1,2,0],[2,0,1]))
 print(Z)

# For Part Two
def Second_Part(B):
 Z=0
 L=[o.split()[h]for h in[0,1,2]for o in B.split('\n')]
 B='\n'.join(' '.join(i)for i in[L[i:3+i]for i in range(0,len(L),3)])
 for i in B.split('\n'):
  Z+=all((int(i.split()[h[0]])+int(i.split()[h[1]]))>int(i.split()[h[2]])for h in([0,1,2],[1,2,0],[2,0,1]))
 print(Z)
