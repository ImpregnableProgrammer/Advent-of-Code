# Part One
First_Part=lambda k,v=[],re=__import__('re'),J=lambda u,re=__import__('re'):re.match('\w+|\(\d+x\d+\)',u):len(k)>0 and First_Part(k[J(k).span()[1]+int(re.search('(?<=\()\d+',J(k).group()[0]=='('and J(k).group()or'(0').group()):],v+[J(k).group()[0]=='('and k[J(k).span()[1]:][:int(re.search('\d+',J(k).group()).group())]*int(re.search('(?<=x)\d+',J(k).group()).group())or J(k).group()])or len(''.join(v)) 

# Part Two
  # Initial Attempt; Throws Segmentation Fault with huge inputs
  Initial_Second_Part=lambda k,re=__import__('re'),M=lambda i,re=__import__('re'):re.search('\(\d+x\d+\)',i):M(k)!=None and Second_Part(k[:M(k).span()[0]]+k[M(k).span()[1]:M(k).span()[1]+int(re.search('(?<=\()\d+',M(k).group()).group())]*int(re.search('(?<=x)\d+',M(k).group()).group())+k[M(k).span()[1]+int(re.search('(?<=\()\d+',M(k).group()).group()):])or len(k)
# Final successfull attempt – FINALLY COMPLETED OVER ONE YEAR LATER!
# Recursive, so make sure to set recursion limit higher than length of input
D=lambda s,l=[[1,1]],c=0,re=__import__('re'):len(s)and (s[0]=='('and D(re.sub('^\(.*?\)','',s),[[1,1]]+[[o[0]-len(re.search('\(.*?\)',s).group(0)),o[1]]for o in l[1:]if o[0]>len(re.search('(?<=\()\d*',s).group(0))]+[[int(re.search('(?<=\()\d*',s).group(0)),int(re.search('(?<=x)\d*',s).group(0))*l[len(l)-1][1]]],c)or D(s[1:],[[1,1]]+[[o[0]-1,o[1]]for o in l[1:]if o[0]>1],c+l[len(l)-1][1]))or c
