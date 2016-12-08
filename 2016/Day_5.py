# Part One
def First_Part(f,Y='',i=0):
 while len(Y)!=8:
  import hashlib
  m=hashlib.md5()
  m.update(f+`i`)
  if m.hexdigest()[:5]=='00000':
   Y+=m.hexdigest()[5]
  i+=1
 print(Y)
 
# Part Two
def Second_Part(f,Y=list('        '),Z=[],i=0):
 while' 'in Y:
  import hashlib
  m=hashlib.md5()
  m.update(f+`i`)
  if m.hexdigest()[:5]=='00000'and m.hexdigest()[5].isdigit()and 0<=int(m.hexdigest()[5])<8and int(m.hexdigest()[5])not in Z:
   Z+=[int(m.hexdigest()[5])]
   Y[int(m.hexdigest()[5])]=m.hexdigest()[6]
  i+=1
 print(''.join(Y))
