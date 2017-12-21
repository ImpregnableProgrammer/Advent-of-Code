# First Part – input is a string
First_Part=lambda s:sum(int(g)for i,g in enumerate(s)if s[i]==s[(i+1)%len(s)])

# Second Part
