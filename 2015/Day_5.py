# Part One
First_Part=lambda g:[all(o not in f for o in['ab','cd','pq','xy'])and any(i in f for i in[p*2 for p in'abcdefghijklmnopqrstuvwxyz'])and sum([f.count(i)for i in'aeiou'])>=3 for f in g.split('\n')].count(1)

# Part Two
Second_Part=lambda z,re=__import__('re'):[any(u in q for u in[p+j+p for p in'abcdefghijklmnopqrstuvwxyz'for j in'abcdefghijklmnopqrstuvwxyz'])and re.fullmatch(r'.*(\w{2}).*\1.*',q)!=None for q in z.split('\n')].count(1)
