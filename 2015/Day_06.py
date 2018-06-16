# Part One
def First_Part(G):
 H=eval(('['+'0,'*1000+'],')*1000)
 for i in G.split('\n'):
  Y=i.split();B=Y[0]=='turn';N,M=map(int,Y[[1,2][B]].split(','));J,K=map(int,Y[[3,4][B]].split(','))
  for i in range(M,-~K,1-2*(M>-~K)):
   for c in range(N,-~J,1-2*(N>-~J)):H[i][c]=int(B and'01'[Y[1]=='on']or'01'[H[i][c]==0])
 print(sum(map(lambda f:f.count(1),H)))
 
# Part Two
def Second_Part(G):
 H=eval(('['+'0,'*1000+'],')*1000)
 for i in G.split('\n'):
  Y=i.split();B=Y[0]=='turn';N,M=map(int,Y[[1,2][B]].split(','));J,K=map(int,Y[[3,4][B]].split(','))
  for i in range(M,-~K,1-2*(M>-~K)):
   for c in range(N,-~J,1-2*(N>-~J)):H[i][c]=max(H[i][c]+(1-2*(Y[1]=='off')),0)if B else H[i][c]+2
 print(sum(map(sum,H)))
   
