# Part One
First_Part=lambda f,G=lambda c:map(int,c.split('x')):sum([2*(G(i)[0]*G(i)[1]+G(i)[1]*G(i)[2]+G(i)[2]*G(i)[0])+min(G(i)[0]*G(i)[1],G(i)[1]*G(i)[2],G(i)[2]*G(i)[0])for i in f.split('\n')])

# Part Two
Second_Part=lambda f,G=lambda c:map(int,c.split('x')),V=lambda i:min((G(i)[0],G(i)[1]),(G(i)[1],G(i)[2]),(G(i)[2],G(i)[0]),key=sum):sum([V(i)[0]*2+V(i)[1]*2+G(i)[0]*G(i)[1]*G(i)[2]for i in f.split('\n')])
