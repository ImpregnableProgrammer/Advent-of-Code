# Part One
First_Part=lambda c,S=__import__('re').search,s=sorted:sum([int(S('(?<=\-)\d+(?=\[)',i).group())for i in c.split('\n')if S('(?<=\[).*(?=\])',i).group()in''.join(s(s({*S('([a-z]*\-*)+(?![0-9])',i).group().replace('-','')}),key=i.count,reverse=1))])

# Part Two
Second_Part=lambda c,re=__import__('re'),s=sorted,X=lambda f:int(re.search('(?<=\-)\d+(?=\[)',f).group()):[X(i)for i in c.split('\n')if re.search('(?<=\[).*(?=\])',i).group()in''.join(s(s({*re.search('([a-z]*\-*)+(?![0-9])',i).group().replace('-','')}),key=i.count,reverse=1))and'north'in''.join([[chr(97+(ord(u)-97+X(i))%26),' '][u=='-']for u in re.sub('\-\d+\[.*\]','',i)])]
