
def Part1(nums):
    b=sum(2**n * (sum(nums[i][-n-1] == '1' for i in range(len(nums))) > (len(nums) // 2)) for n in range(len(nums[0])))
    return b * (~(2**len(nums[0])-1) ^ (~b)) # Clever bitwise stuff to multiply b by non-2's complement of ~b

def Part2(nums):
    # F=lambda b=1,L=[nums]:[L.append([L[-1][j]for j in range(len(L[-1]))if L[-1][j][n]=="10"[sum(L[-1][i][n]=='1'for i in range(len(L[-1])))>=(len(L[-1])/2)]])for n in range(len(nums[0]))]and[i for i in L if len(i)<12]
    L, i = nums, 0
    while len(L) > 1:
        bit = sum(l[i] == '1'for l in L) >= len(L) / 2
        L = [l for l in L if l[i] == "01"[bit]]
        i += 1
    L2, i = nums, 0
    while len(L2) > 1:
        bit2 = sum(l[i] == '1' for l in L2) >= len(L2) / 2
        L2 = [l for l in L2 if l[i] == "10"[bit2]]
        i += 1
    #print([L[i] for i in range(len(L)) if len(L[i]) < 20])
    #bN=["01"[a=='0'] for a in b]
    # nums = sorted(nums, key=lambda d:([i+1 for i in range(len(d)-1) if (d[i] == b[i]) != (d[i+1] == b[i+1])] + [len(nums[0])])[0])
    #print(nums[-2:], ''.join(b))
    print(L, L2)
    toBin=lambda n:sum(2**i * (n[-i-1]=='1') for i in range(len(n)))
    return toBin(L[-1]) * toBin(L2[-1])
    #return toBin(nums[-1]) * toBin(nums[-2])

Input = open("Inputs/Day_03", 'r').read()[:-1].split('\n')
print(Part1(Input))
print(Part2(Input))

