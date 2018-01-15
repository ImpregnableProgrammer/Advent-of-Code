# First Part -- IN PROGRESS
import re
def First_Part(s):
  Z=lambda i:re.findall("a ([a-z-]+? (?:microchip|generator))",s.split('\n')[i])
  T=[[[Z(0),Z(1),Z(2),Z(3)]]*2]
  E=sum(len(Z(I)) for I in range(4))
  #print("E =",E)
  P=0
  for Op in range(1):
    K=[]
    for i in T:
      Old=i[0]
      U=[Old]
      for u in range(1,len(i)):
        for q in range(4):
          for z in range(len(i[u][q])):
            O=i[u][q][z].replace('-compatible microchip','').replace(' generator','')
            if q+1<4:
              L=i[u][:q]+[i[u][q][:z]+i[u][q][z+1:]]+[i[u][q+1]+[i[u][q][z]]]+i[u][q+2:]
              #print(L)
              if ('generator' in i[u][q][z] and all(n.replace('-compatible microchip',' generator') in i[u][q+1] for n in i[u][q+1] if 'microchip' in n and O not in n))\
              or ('microchip' in i[u][q][z] and (not any(n for n in i[u][q+1] if 'generator' in n and O not in n) or O+' generator' in i[u][q+1]))\
              and L!=Old:
                U+=[L]
            if q-1>-1:
              L=i[u][:q-1]+[i[u][q-1]+[i[u][q][z]]]+[i[u][q][:z]+i[u][q][z+1:]]+i[u][q+1:]
              #print(L)
              if ('generator' in i[u][q][z] and all(n.replace('-compatible microchip',' generator') in i[u][q-1] for n in i[u][q-1] if 'microchip' in n and O not in n))\
              or ('microchip' in i[u][q][z] and (not any(n for n in i[u][q-1] if 'generator' in n and O not in n) or O+' generator' in i[u][q-1]))\
              and L!=Old:
                U+=[L]
        K+=[U]
      T=K
      #print("K =",K)
      P+=1
      
            
