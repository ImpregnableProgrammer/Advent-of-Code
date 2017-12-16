# First Part
import re
def First_Part(s):
  Bot_Dict = {}
  while all(sorted(o,key=int)!=['61','17'] for o in Bot_Dict.values()):
    for p in s.split('\n'):
      p=re.sub('(?<=output )\d+',lambda k:str(-int(k.group(0))-1),p)
      print(p)
      G=re.findall('-?\d+',p)
      if p[:3]=='bot' and G[0] in Bot_Dict.keys() and len(Bot_Dict[G[0]])>1:
        if G[1] not in Bot_Dict.keys():
          Bot_Dict[G[1]]=[]
        if G[2] not in Bot_Dict.keys():
          Bot_Dict[G[2]]=[]
        Bot_Dict[G[1]]+=len(Bot_Dict[G[1]])<2 and [min(Bot_Dict[G[0]],key=int)] or []
        Bot_Dict[G[2]]+=len(Bot_Dict[G[1]])<2 and [max(Bot_Dict[G[0]],key=int)] or []
        Bot_Dict[G[0]]=len(Bot_Dict[G[1]])>1 and [min(Bot_Dict[G[0]],key=int)] or len(Bot_Dict[G[2]])>1 and [max(Bot_Dict[G[0]],key=int)] or []
      elif p[:5]=='value':
        if G[1] not in Bot_Dict.keys():
          Bot_Dict[G[1]]=[]
        Bot_Dict[G[1]]+=len(Bot_Dict[G[1]])<2 and [G[0]] or []
      print(Bot_Dict)
  print([o for o in Bot_Dict.keys() if sorted(Bot_Dict[o],key=int)==['61','17']])
   
        
        
