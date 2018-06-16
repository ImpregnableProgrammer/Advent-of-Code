# Part One; Two Solutions
First_Part_1=lambda c,k=0:k<len(c)and(1-2*(c[k]==')'))+J(c,k+1)or 0
First_Part_2=lambda f,re=__import__('re'):eval(re.sub('\)+',lambda f:`-len(f.group())`,re.sub('\(+',lambda i:'+'+`len(i.group())`,re.sub('\(\)','',f))))

# Part Two; Two Solutions
Second_Part_1=lambda c,J=lambda c,k=0:k<len(c)and(1-2*(c[k]==')'))+J(c,k+1)or 0:-~[J(c[:o])for o in range(1,-~len(c))].index(-1)
Second_Part_2=lambda c,X=lambda f,re=__import__('re'):eval(re.sub('\)+',lambda f:`-len(f.group())`,re.sub('\(+',lambda i:'+'+`len(i.group())`,re.sub('\(\)','',f)))+'+0'):-~[X(c[:o])for o in range(1,-~len(c))].index(-1)
