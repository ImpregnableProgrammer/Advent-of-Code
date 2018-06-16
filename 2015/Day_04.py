# Part One
def First_Part(f,Y=0):
 for i in range(10000000):
  import hashlib
  m=hashlib.md5()
  m.update(f+`i`)
  if m.hexdigest()[:5]=='00000':print f+`i`;Y+=i;break
 print(Y)
 
 # Part Two
 def Second_Part(f,Y=0):
 for i in range(10000000):
  import hashlib
  m=hashlib.md5()
  m.update(f+`i`)
  if m.hexdigest()[:6]=='000000':print f+`i`;Y+=i;break
 print(Y)
