# First Part – Input is a string.
First_Part=lambda s:sum(int(g)for i,g in enumerate(s)if s[i]==s[(i+1)%len(s)])

# Second Part – Again, input is a string.
Second_Part=lambda s:sum(int(g)for i,g in enumerate(s)if s[i]==s[(i+len(s)//2)%len(s)])
