# Part One
First_Part=lambda f,M=lambda g:g[0]*g[1]:sum([M(map(int,i.split()[1].split('x')))for i in f.split('\n')if'rect'in i])

# Part Two
def Second_Part(f):
  H=list(eval(('['+'" ",'*50+'],')*6))
  for i in f.split('\n'):
    Y=i.split()
    if Y[0]=='rect':
      K=map(int,Y[1].split('x'))
      # print('rect',K)
      for h in range(K[1]):
        for m in range(K[0]):H[h][m]='#'
    else:
      if Y[1]=='row':
        V=int(Y[2].split('=')[-1])
        # print('row',V,int(Y[-1]))
        for u in[1]*int(Y[-1]):H[V]=H[V][-1:]+H[V][:-1]
      else:
        V=int(Y[2].split('=')[-1])
        print('column',V,int(Y[-1]))
        U=[H[i][V]for i in range(6)]
        for u in[1]*int(Y[-1]):U=U[-1:]+U[:-1]
        for c in range(6):H[c][V]=U[c]
  for e in H:print(''.join(e))
