
# Microchips CANNOT be left on same floor as other RTG(s) unless connected to own RTG
# Must move at LEAST one RTG or microchip at a time
# Can move at MOST two RTGs or microchips in any combination: Two RTGs, RTG and corresponding microchip, Two microchips
# 4 floors


# Breadth-First search
# INITIAL ATTEMPT
import re
'''def First_Part(s):
  Z=lambda i:re.findall("[a-z]+(-compatible)?(microchip|generator)",s.split('\n')[i])
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
    print(P)'''
      

# Breadth-first search
# FINAL WORKING SOLUTION FOR BOTH PARTS!
def BFSearch(s):
  Conf = tuple(tuple(re.findall("[a-z]+(?:M|R)", s.split("\n")[i].replace("-compatible microchip", "M").replace(" generator", "R"))) for i in range(4))
  Elements = {Conf:0}
  Old = set()
  print(Elements, "\n")
  Step = 0
  Size = sum(len(u) for u in Conf)
  while 1:
    T = dict()
    for element, floor in Elements.items():
      if len(element[-1]) == Size:
        return Step
      D = tuple(tuple(sorted(i)) for i in element)
      for obj in range(len(element[floor])):
        Current = element[floor][obj]
        if Current[-1] == "M":
          if floor + 1 < 4 and (Current[:-1] + "R" in element[floor + 1] or all(i[-1] != "R" for i in element[floor+1])):
            Z = tuple(tuple(sorted(g)) for g in element[:floor] + (element[floor][:obj] + element[floor][obj+1:],) + ((Current,) + element[floor+1],) + element[floor+2:])
            if Z not in Old and Z not in T.keys():
              T.update({Z:floor + 1})
              Old.add(D)              
          if floor - 1 >= 0 and (Current[:-1] + "R" in element[floor - 1] or all(i[-1] != "R" for i in element[floor-1])) and any(len(i) for i in element[:floor]):
            Z = tuple(tuple(sorted(g)) for g in element[:floor-1] + ((Current,) + element[floor-1],) + (element[floor][:obj] + element[floor][obj+1:],) + element[floor+1:])
            if Z not in Old and Z not in T.keys():
              T.update({Z:floor - 1})
              Old.add(D)              
          for obj2 in range(obj+1, len(element[floor])):
            Current2 = element[floor][obj2]
            if Current2[:-1] == Current[:-1] and Current2[-1] == "R":
              if floor + 1 < 4 and all(i[:-1] + "R" in element[floor+1] for i in element[floor+1] if i[-1] == "M"):
                Z = tuple(tuple(sorted(g)) for g in element[:floor] + (element[floor][:obj] + element[floor][obj+1:obj2] + element[floor][obj2+1:],) + ((Current,) + (Current2,) + element[floor+1],) + element[floor+2:])
                if Z not in Old and Z not in T.keys():
                  T.update({Z:floor + 1})
                  Old.add(D)                  
              if floor - 1 >= 0 and all(i[:-1] + "R" in element[floor-1] for i in element[floor-1] if i[-1] == "M") and any(len(i) for i in element[:floor]):
                Z = tuple(tuple(sorted(g)) for g in element[:floor-1] + ((Current,) + (Current2,) + element[floor-1],) + (element[floor][:obj] + element[floor][obj+1:obj2] + element[floor][obj2+1:],) + element[floor+1:])
                if Z not in Old and Z not in T.keys():
                  T.update({Z:floor - 1})
                  Old.add(D)                  
            elif Current2[-1] == "M":
              if floor + 1 < 4 and ((Current[:-1] + "R" in element[floor+1] and Current2[:-1] + "R" in element[floor+1]) or all(i[-1] != "R" for i in element[floor+1])):
                Z = tuple(tuple(sorted(g)) for g in element[:floor] + (element[floor][:obj] + element[floor][obj+1:obj2] + element[floor][obj2+1:],) + ((Current,) + (Current2,) + element[floor+1],) + element[floor+2:])
                if Z not in Old and Z not in T.keys():
                  T.update({Z:floor + 1})
                  Old.add(D)                  
              if floor - 1 >= 0 and ((Current[:-1] + "R" in element[floor-1] and Current2[:-1] + "R" in element[floor-1]) or all(i[-1] != "R" for i in element[floor-1])) and any(len(i) for i in element[:floor]):
                Z = tuple(tuple(sorted(g)) for g in element[:floor-1] + ((Current,) + (Current2,) + element[floor-1],) + (element[floor][:obj] + element[floor][obj+1:obj2] + element[floor][obj2+1:],) + element[floor+1:])
                if Z not in Old and Z not in T.keys():
                  T.update({Z:floor - 1})
                  Old.add(D)                  
        else:
          Behind = Current[:-1] + "M" in element[floor] and any(i[-1] == "R" for i in element[floor] if i[:-1] != Current[:-1])
          if floor + 1 < 4 and all(i[:-1] + "R" in element[floor+1] for i in element[floor+1] if i[-1] == "M" and i[:-1] != Current[:-1]) and not Behind:
            Z = tuple(tuple(sorted(g)) for g in element[:floor] + (element[floor][:obj] + element[floor][obj+1:],) + ((Current,) + element[floor+1],) + element[floor+2:])
            if Z not in Old and Z not in T.keys():
              T.update({Z:floor + 1})
              Old.add(D)              
          if floor - 1 >= 0 and all(i[:-1] + "R" in element[floor-1] for i in element[floor-1] if i[-1] == "M" and i[:-1] != Current[:-1]) and not Behind and any(len(i) for i in element[:floor]):
            Z = tuple(tuple(sorted(g)) for g in element[:floor-1] + ((Current,) + element[floor-1],) + (element[floor][:obj] + element[floor][obj+1:],) + element[floor+1:])
            if Z not in Old and Z not in T.keys():
              T.update({Z:floor - 1})
              Old.add(D)              
          for obj2 in range(obj+1, len(element[floor])):
            Current2 = element[floor][obj2]
            Behind2 = (Current2[:-1] + "M" in element[floor] or Current[:-1] in element[floor]) and any(i[-1] == "R" for i in element[floor] if i[:-1] != Current2[:-1] and i[:-1] != Current[:-1])
            if Current2[:-1] == Current[:-1] and Current2[-1] == "M":
              if floor + 1 < 4 and all(i[:-1] + "R" in element[floor+1] for i in element[floor+1] if i[-1] == "M"):
                Z = tuple(tuple(sorted(g)) for g in element[:floor] + (element[floor][:obj] + element[floor][obj+1:obj2] + element[floor][obj2+1:],) + ((Current,) + (Current2,) + element[floor+1],) + element[floor+2:])
                if Z not in Old and Z not in T.keys():
                  T.update({Z:floor + 1})
                  Old.add(D)                  
              if floor - 1 >= 0 and all(i[:-1] + "R" in element[floor-1] for i in element[floor-1] if i[-1] == "M") and any(len(i) for i in element[:floor]):
                Z = tuple(tuple(sorted(g)) for g in element[:floor-1] + ((Current,) + (Current2,) + element[floor-1],) + (element[floor][:obj] + element[floor][obj+1:obj2] + element[floor][obj2+1:],) + element[floor+1:])
                if Z not in Old and Z not in T.keys():
                  T.update({Z:floor - 1})
                  Old.add(D)                  
            elif Current2[-1] == "R" and not Behind2:
              if floor + 1 < 4 and all(i[:-1] + "R" in element[floor+1] for i in element[floor+1] if i[-1] == "M" and i[:-1] != Current[:-1] and i[:-1] != Current2[:-1]):
                Z = tuple(tuple(sorted(g)) for g in element[:floor] + (element[floor][:obj] + element[floor][obj+1:obj2] + element[floor][obj2+1:],) + ((Current,) + (Current2,) + element[floor+1],) + element[floor+2:])
                if Z not in Old and Z not in T.keys():
                  T.update({Z:floor + 1})
                  Old.add(D)                  
              if floor - 1 >= 0 and all(i[:-1] + "R" in element[floor-1] for i in element[floor-1] if i[-1] == "M" and i[:-1] != Current[:-1] and i[:-1] != Current2[:-1]) and any(len(i) for i in element[:floor]):
                Z = tuple(tuple(sorted(g)) for g in element[:floor-1] + ((Current,) + (Current2,) + element[floor-1],) + (element[floor][:obj] + element[floor][obj+1:obj2] + element[floor][obj2+1:],) + element[floor+1:])
                if Z not in Old and Z not in T.keys():
                  T.update({Z:floor - 1})
                  Old.add(D)                  
    Step += 1
    Elements = T
    print(len(Elements), len(Old), Step,"\n")

# Second Part -- ATTAINS CORRECT ANSWER OF 71 IN 27 MIN 26 SEC!
#print(BFSearch('''The first floor contains An elerium generator, An elerium-compatible microchip, A dilithium generator, A dilithium-compatible microchip, a polonium generator, a thulium generator, a thulium-compatible microchip, a promethium generator, a ruthenium generator, a ruthenium-compatible microchip, a cobalt generator, and a cobalt-compatible microchip.
#The second floor contains a polonium-compatible microchip and a promethium-compatible microchip.
#The third floor contains nothing relevant.
#The fourth floor contains nothing relevant.'''))

# First Part -- ATTAINS CORRECT ANSWER OF 47 IN 14 SEC!
print(BFSearch('''The first floor contains a polonium generator, a thulium generator, a thulium-compatible microchip, a promethium generator, a ruthenium generator, a ruthenium-compatible microchip, a cobalt generator, and a cobalt-compatible microchip.
#The second floor contains a polonium-compatible microchip and a promethium-compatible microchip.
#The third floor contains nothing relevant.
#The fourth floor contains nothing relevant.'''))

# Given Sample
#print(BFSearch('''The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
#The second floor contains a hydrogen generator.
#The third floor contains a lithium generator.
#The fourth floor contains nothing relevant.'''))


# Depth-first search -- NOPE!
# Finds A path but not neccessarily the SHORTEST path
# Also MUCH too SLOW for given input
# Ouputs 43 for given sample case :(
def DFSearch(s):
  Element = [re.findall("[a-z]+(?:M|R)", s.split("\n")[i].replace("-compatible microchip", "M").replace(" generator", "R")) for i in range(4)]
  print(Element)
  Old = []
  Step = 0
  Size = sum(len(u) for u in Element)
  Search(Element, 0, 0, Size, [])

def Search(element, floor, step, size, Old):
  if len(element[-1]) == size:
    print(step)
    for i in Old:
      print(i)
    #print(step, len(Old))
    exit(0)
  #if [[], [], ['hydrogenR', 'hydrogenM'], ['lithiumR', 'lithiumM']] == element:
  #  print(step, element, Old[-1])
  #print("Beg.",len(Old), step, element, floor)
  for obj in range(len(element[floor])):
    #if [[], ['lithiumM'], ['hydrogenM', 'hydrogenR', 'lithiumR'], []] == element and 6 == step:
    #  print(element[floor][obj], element, step, floor, len(element[floor]), obj)
    Current = element[floor][obj]
    if Current[-1] == "M":
      for obj2 in range(obj+1, len(element[floor])):
        #if [[], ['lithiumM'], ['hydrogenM', 'hydrogenR', 'lithiumR'], []] == element and 6 == step:
        #  print(element[floor][obj], element[floor][obj2], element, step, floor, len(element[floor]), obj, obj2)
        Current2 = element[floor][obj2]
        if Current2[:-1] == Current[:-1] and Current2[-1] == "R":
          if floor + 1 < 4 and all(i[:-1] + "R" in element[floor+1] for i in element[floor+1] if i[-1] == "M"):
            Z = element[:floor] + [element[floor][:obj] + element[floor][obj+1:obj2] + element[floor][obj2+1:]] + [[Current] + [Current2] + element[floor+1]] + element[floor+2:]
            if [sorted(i) for i in Z] not in Old:
              #print(step + 1, Z)
              Search(Z, floor + 1, step + 1, size, Old + [[sorted(i) for i in element]])
          if floor - 1 >= 0 and all(i[:-1] + "R" in element[floor-1] for i in element[floor-1] if i[-1] == "M"):
            Z = element[:floor-1] + [[Current] + [Current2] + element[floor-1]] + [element[floor][:obj] + element[floor][obj+1:obj2] + element[floor][obj2+1:]] + element[floor+1:]
            if [sorted(i) for i in Z] not in Old:
              #print(step + 1, Z)
              Search(Z, floor - 1, step + 1, size, Old + [[sorted(i) for i in element]])
        elif Current2[-1] == "M":
          #if floor + 1 < 4:
          #  print(((Current[:-1] + "R" in element[floor+1] and Current2[:-1] + "R" in element[floor+1]) or all(i[-1] != "R" for i in element[floor+1])), element, step)
          if floor + 1 < 4 and ((Current[:-1] + "R" in element[floor+1] and Current2[:-1] + "R" in element[floor+1]) or all(i[-1] != "R" for i in element[floor+1])):
            Z = element[:floor] + [element[floor][:obj] + element[floor][obj+1:obj2] + element[floor][obj2+1:]] + [[Current] + [Current2] + element[floor+1]] + element[floor+2:]
            #print(step + 1, Z)
            if [sorted(i) for i in Z] not in Old:
              #print(step + 1, Z)
              Search(Z, floor + 1, step + 1, size, Old + [[sorted(i) for i in element]])
          if floor - 1 >= 0 and ((Current[:-1] + "R" in element[floor-1] and Current2[:-1] + "R" in element[floor-1]) or all(i[-1] != "R" for i in element[floor-1])):
            Z = element[:floor-1] + [[Current] + [Current2] + element[floor-1]] + [element[floor][:obj] + element[floor][obj+1:obj2] + element[floor][obj2+1:]] + element[floor+1:]
            # print(Z, step, floor, element)
            if [sorted(i) for i in Z] not in Old:
              #print(Z)
              Search(Z, floor - 1, step + 1, size, Old + [[sorted(i) for i in element]])
      if floor + 1 < 4 and (Current[:-1] + "R" in element[floor + 1] or all(i[-1] != "R" for i in element[floor+1])):
        Z = element[:floor] + [element[floor][:obj] + element[floor][obj+1:]] + [[Current] + element[floor+1]] + element[floor+2:]
        if [sorted(i) for i in Z] not in Old:
          #print(step + 1, Z)
          Search(Z, floor + 1, step + 1, size, Old + [[sorted(i) for i in element]])
      if floor - 1 >= 0 and (Current[:-1] + "R" in element[floor - 1] or all(i[-1] != "R" for i in element[floor-1])):
        Z = element[:floor-1] + [[Current] + element[floor-1]] + [element[floor][:obj] + element[floor][obj+1:]] + element[floor+1:]
        if [sorted(i) for i in Z] not in Old:
          #print(step + 1, Z)
          Search(Z, floor - 1, step + 1, size, Old + [[sorted(i) for i in element]])
    else:
      #print(step + 1, element[floor][obj], floor, element)
      for obj2 in range(obj+1, len(element[floor])):
        Current2 = element[floor][obj2]
        if Current2[:-1] == Current[:-1] and Current2[-1] == "M":
          if floor + 1 < 4 and all(i[:-1] + "R" in element[floor+1] for i in element[floor+1] if i[-1] == "M"):
            Z = element[:floor] + [element[floor][:obj] + element[floor][obj+1:obj2] + element[floor][obj2+1:]] + [[Current] + [Current2] + element[floor+1]] + element[floor+2:]
            #print(step + 1, Z)
            if [sorted(i) for i in Z] not in Old:
              #print(step + 1, Z)
              Search(Z, floor + 1, step + 1, size, Old + [[sorted(i) for i in element]])
          if floor - 1 >= 0 and all(i[:-1] + "R" in element[floor-1] for i in element[floor-1] if i[-1] == "M"):
            Z = element[:floor-1] + [[Current] + [Current2] + element[floor-1]] + [element[floor][:obj] + element[floor][obj+1:obj2] + element[floor][obj2+1:]] + element[floor+1:]
            if [sorted(i) for i in Z] not in Old:
              Search(Z, floor - 1, step + 1, size, Old + [[sorted(i) for i in element]])
        elif Current2[-1] == "R":
          if floor + 1 < 4 and all(i[:-1] + "R" in element[floor+1] for i in element[floor+1] if i[-1] == "M" and i[:-1] != Current[:-1] and i[:-1] != Current2[:-1]):
            Z = element[:floor] + [element[floor][:obj] + element[floor][obj+1:obj2] + element[floor][obj2+1:]] + [[Current] + [Current2] + element[floor+1]] + element[floor+2:]
            if [sorted(i) for i in Z] not in Old:
              Search(Z, floor + 1, step + 1, size, Old + [[sorted(i) for i in element]])
          if floor - 1 >= 0 and all(i[:-1] + "R" in element[floor-1] for i in element[floor-1] if i[-1] == "M" and i[:-1] != Current[:-1] and i[:-1] != Current2[:-1]):
            Z = element[:floor-1] + [[Current] + [Current2] + element[floor-1]] + [element[floor][:obj] + element[floor][obj+1:obj2] + element[floor][obj2+1:]] + element[floor+1:]
            if [sorted(i) for i in Z] not in Old:
              Search(Z, floor - 1, step + 1, size, Old + [[sorted(i) for i in element]])
      if floor + 1 < 4 and all(i[:-1] + "R" in element[floor+1] for i in element[floor+1] if i[-1] == "M" and i[:-1] != Current[:-1]):
        Z = element[:floor] + [element[floor][:obj] + element[floor][obj+1:]] + [[Current] + element[floor+1]] + element[floor+2:]
        #print(step + 1, Z)
        if [sorted(i) for i in Z] not in Old:
          #print(step + 1, Z, element)
          Search(Z, floor + 1, step + 1, size, Old + [[sorted(i) for i in element]])
      if floor - 1 >= 0 and all(i[:-1] + "R" in element[floor-1] for i in element[floor-1] if i[-1] == "M" and i[:-1] != Current[:-1]):
        Z = element[:floor-1] + [[Current] + element[floor-1]] + [element[floor][:obj] + element[floor][obj+1:]] + element[floor+1:]
        if [sorted(i) for i in Z] not in Old:
          #print(step + 1, Z)
          Search(Z, floor - 1, step + 1, size, Old + [[sorted(i) for i in element]]) 
  #print("End",len(Old), step, element, floor)
