import re

# First Part
def First_Part(s):
    Bot_Dict = {}
    g=0
    s=s.split('\n')
    while 1:
      p=re.sub('(?<=output )\d+',lambda k:str(-int(k.group(0))-1),s[g%len(s)])
      G=re.findall('-?\d+',p)
      if p[:3]=='bot' and G[0] in Bot_Dict.keys() and len(Bot_Dict[G[0]])>1:
        if sorted(Bot_Dict[G[0]],key=int)==['17','61']:
          print(G[0])
          break
        s.pop(g%len(s))
        if G[1] not in Bot_Dict.keys():
          Bot_Dict[G[1]]=[]
        if G[2] not in Bot_Dict.keys():
          Bot_Dict[G[2]]=[]
        X=len(Bot_Dict[G[1]])
        Y=len(Bot_Dict[G[2]])
        Bot_Dict[G[1]]+=(G[1][0]=='-' or (G[1][0]!='-' and X<2)) and [min(Bot_Dict[G[0]],key=int)] or []
        Bot_Dict[G[2]]+=(G[2][0]=='-' or (G[2][0]!='-' and Y<2)) and [max(Bot_Dict[G[0]],key=int)] or []
        Bot_Dict[G[0]]=(G[1][0]!='-' and X>1) and [min(Bot_Dict[G[0]],key=int)] or (G[2][0]!='-' and Y>1) and [max(Bot_Dict[G[0]],key=int)] or []
      elif p[:5]=='value':
        s.pop(g%len(s))
        if G[1] not in Bot_Dict.keys():
          Bot_Dict[G[1]]=[]
        Bot_Dict[G[1]]+=len(Bot_Dict[G[1]])<2 and [G[0]] or []
      g+=1

# Second Part
def Second_Part(s):
    Bot_Dict = {}
    g=0
    s=s.split('\n')
    while 1:
      p=re.sub('(?<=output )\d+',lambda k:str(-int(k.group(0))-1),s[g%len(s)])
      G=re.findall('-?\d+',p)
      if p[:3]=='bot' and G[0] in Bot_Dict.keys() and len(Bot_Dict[G[0]])>1:
        s.pop(g%len(s))
        if G[1] not in Bot_Dict.keys():
          Bot_Dict[G[1]]=[]
        if G[2] not in Bot_Dict.keys():
          Bot_Dict[G[2]]=[]
        X=len(Bot_Dict[G[1]])
        Y=len(Bot_Dict[G[2]])
        Bot_Dict[G[1]]+=(G[1][0]=='-' or (G[1][0]!='-' and X<2)) and [min(Bot_Dict[G[0]],key=int)] or []
        Bot_Dict[G[2]]+=(G[2][0]=='-' or (G[2][0]!='-' and Y<2)) and [max(Bot_Dict[G[0]],key=int)] or []
        Bot_Dict[G[0]]=(G[1][0]!='-' and X>1) and [min(Bot_Dict[G[0]],key=int)] or (G[2][0]!='-' and Y>1) and [max(Bot_Dict[G[0]],key=int)] or []
      elif p[:5]=='value':
        s.pop(g%len(s))
        if G[1] not in Bot_Dict.keys():
          Bot_Dict[G[1]]=[]
        Bot_Dict[G[1]]+=len(Bot_Dict[G[1]])<2 and [G[0]] or []
      g+=1
      if len(s)<1:
        j=1
        for o in Bot_Dict.keys():
          if 0>int(o)>-4:
            j*=int(Bot_Dict[o][0])
        print(j)
        break
        
        
