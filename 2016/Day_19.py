
# First Part

def remainingElf(n):
    d = 0
    m = n
    while m > 0:
        d += 1
        m >>= 1
    # Return the i'th odd number (0-indexed)
    # where i is the distance between the input and the closest power of 2 less than or equal to the input
    return 2 * (n - 2**(d-1)) + 1

print(remainingElf(3014387))


# Second Part

import math

# Iteratively simulate the process of finding the remaining elf
# Much too slow for given input, but very helpful in figuring out the pattern in the sequence
def Simulation(n):
    L = list(range(1, n+1))
    i = 0
    while len(L) > 1:
        n = len(L)
        if n % 2:
            D = dict(zip(L[:(n+1)//2], L[(n+1)//2-1:]))
            D.update(dict(zip(L[(n+1)//2:], L[:(n+1)//2])))
        else:
            D = dict(zip(L[:n//2], L[n//2:]))
            D.update(zip(L[n//2:], L[:n//2]))
        index = L.index(D[L[i%n]])
        L.remove(D[L[i%n]])
        i = 0 if i%n == len(L) else i+1 if i%n < index else i
    return L[0]

def remainingElf2(n):
    # Find the largest power of 3 less than or equal to n
    log3 = 3**int(math.log(n, 3))
    # Application of the pattern found through the above `Simulation' function
    return n if n==log3 else n-log3 if n-log3<log3 else log3+2*(n-2*log3)

# for i in range(1, 100):
#    print(i, '->', Simulation(i))

print(remainingElf2(3014387))
