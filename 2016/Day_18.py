# First_Part
def First_Part(n,s):
  h=['.'+s+'.']
  Trap=['..^','^..','.^^','^^.']
  c=s.count('.')
  for i in range(n-1):
    m=''.join(['.','^'][h[i][k:k+3]in Trap]for k in range(len(s)))
    c+=m.count('.')
    h+=['.'+m+'.']
  print(c)
  
# Second Part –– Same as first part.
# But no array used to store the many generated strings, for the sake of saving space.
def Second_Part(n,s):
  h='.'+s+'.'
  Trap=['..^','^..','.^^','^^.']
  c=s.count('.')
  for i in range(n-1):
    m=''.join(['.','^'][h[k:k+3]in Trap]for k in range(len(s)))
    c+=m.count('.')
    h='.'+m+'.'
  print(c)
    
