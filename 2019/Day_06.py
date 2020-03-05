
def First_Part(orbits):
    Orbits = dict()
    checksum = 0
    for orbit in orbits:
        od, og = orbit.split(')')
        Orbits[og] = od
    for og in Orbits.keys():
        while 1:
            try:
                og = Orbits[og]
                checksum += 1
            except KeyError:
                break
    return checksum

def Second_Part(orbits):
    Orbits = dict()
    for orbit in orbits:
        od, og = orbit.split(')')
        Orbits[og] = od
    oPast = ["YOU"]
    oCurr = [Orbits["YOU"]]
    oNext = list()
    dist = 0
    while "SAN" not in oCurr:
        for o in oCurr:
            oNext += ([Orbits[o]] if o != "COM" else []) + [i for i in Orbits.keys() if Orbits[i] == o and i not in oPast]
        oCurr = oNext
        oNext = list()
        oPast += oCurr
        dist += 1
    return dist - 1
            
        
    
Orbits = '''COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN'''.split('\n')

Orbits = open("Inputs/Day_06.txt", 'r').read().split('\n')[:-1]

print(First_Part(Orbits))
print(Second_Part(Orbits))       
