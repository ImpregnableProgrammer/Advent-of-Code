# First Part -- WORK IN PROGRESS
import re
def First_Part(s):
  Z=lambda i:re.findall("a ([a-z-]+? (?:microchip|generator))",s.split('\n')[i])
  T=[[[Z(0),Z(1),Z(2),Z(3)]]*2]
  E=sum(len(Z(I)) for I in range(4))
  print("T =",T)
  P=0
  for i in [1]:
    K=[]
    for i in T:
      Old=i[0]
      for u in range(1,len(i)):
        U=[i[u]]
        #print(i[u],len(i),U)
        if len(i[u][3])==E:
            print(i[u][3])
            return P
        for q in range(4):
          for z in range(len(i[u][q])):
            O=i[u][q][z].replace('-compatible microchip','').replace(' generator','')
            V=not (any(n for n in i[u][q] if 'generator' in n and O not in n) and O+'-compatible microchip' in i[u][q])
            if q+1<4:
              L=i[u][:q]+[i[u][q][:z]+i[u][q][z+1:]]+[i[u][q+1]+[i[u][q][z]]]+i[u][q+2:]
              if ('generator' in i[u][q][z] and all(n.replace('-compatible microchip',' generator') in i[u][q+1] for n in i[u][q+1] if 'microchip' in n and O not in n) and V)\
              or ('microchip' in i[u][q][z] and (not any(n for n in i[u][q+1] if 'generator' in n and O not in n) or O+' generator' in i[u][q+1]))\
              and L!=Old:
                print(L)
                U+=[L]
            if q-1>-1:
              L=i[u][:q-1]+[i[u][q-1]+[i[u][q][z]]]+[i[u][q][:z]+i[u][q][z+1:]]+i[u][q+1:]
              if ('generator' in i[u][q][z] and all(n.replace('-compatible microchip',' generator') in i[u][q-1] for n in i[u][q-1] if 'microchip' in n and O not in n) and V)\
              or ('microchip' in i[u][q][z] and (not any(n for n in i[u][q-1] if 'generator' in n and O not in n) or O+' generator' in i[u][q-1]))\
              and L!=Old:
                print(L)
                U+=[L]
        K+=[U]
    T=K
    #print("T =",T)
    P+=1
    print(P)
      
            
