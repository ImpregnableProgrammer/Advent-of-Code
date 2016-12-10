# Part One
First_Part=lambda c:len([i for i in c.split('\n')if re.search(r'\[\w*(\w)((?!\1)\w)\2\1\w*\]',i)==None and re.search(r'(\w)((?!\1)\w)\2\1',i)!=None])
