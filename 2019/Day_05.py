
def First_Part(prog):
    i = 0
    while i < len(prog):
        inst = prog[i]
        opMode = int(inst[-2:])
        parmModes = inst[:-2]
        parmModeApply = lambda parmMode, index: int(prog[index]) if parmMode == "1" else int(prog[int(prog[index])])
        if opMode == 1:
            addends = []
            for j in range(i+1, i+3):
                parmMode = parmModes[-1] if parmModes else "0"
                addends.append(parmModeApply(parmMode, j))
                parmModes = parmModes[:-1]
            prog[int(prog[i+3])] = str(sum(addends))
            i += 4
        elif opMode == 2:
            mult = []
            for j in range(i+1, i+3):
                parmMode = parmModes[-1] if parmModes else "0"
                mult.append(parmModeApply(parmMode, j))
                parmModes = parmModes[:-1]
            prog[int(prog[i+3])] = str(mult[0] * mult[1])
            i += 4
        elif opMode == 3:
            prog[int(prog[i+1])] = input()
            i += 2
        elif opMode == 4:
            parmMode = parmModes[-1] if parmModes else "0"
            print("Output:", parmModeApply(parmMode, i+1))
            i += 2
        elif opMode == 99:
            return 0
        else:
            i += 1
            
def Second_Part(prog):
    i = 0
    while i < len(prog):
        inst = prog[i]
        opMode = int(inst[-2:])
        parmModes = inst[:-2]
        getParmMode = lambda parmModes: parmModes[-1] if parmModes else "0"
        parmModeApply = lambda parmMode, index: int(prog[index]) if parmMode == "1" else int(prog[int(prog[index])])
        if opMode == 1:
            addends = []
            for j in range(i+1, i+3):
                parmMode = getParmMode(parmModes)
                addends.append(parmModeApply(parmMode, j))
                parmModes = parmModes[:-1]
            prog[int(prog[i+3])] = str(sum(addends))
            i += 4
        elif opMode == 2:
            mult = []
            for j in range(i+1, i+3):
                parmMode = getParmMode(parmModes)
                mult.append(parmModeApply(parmMode, j))
                parmModes = parmModes[:-1]
            prog[int(prog[i+3])] = str(mult[0] * mult[1])
            i += 4
        elif opMode == 3:
            prog[int(prog[i+1])] = input()
            i += 2
        elif opMode == 4:
            parmMode = getParmMode(parmModes)
            print("Output:", parmModeApply(parmMode, i+1))
            i += 2
        elif opMode == 5:
            if parmModeApply(getParmMode(parmModes), i+1):
                parmModes = parmModes[:-1]
                i = parmModeApply(getParmMode(parmModes), i+2)
            else:
                i += 2
        elif opMode == 6:
            if not parmModeApply(getParmMode(parmModes), i+1):
                parmModes = parmModes[:-1]
                i = parmModeApply(getParmMode(parmModes), i+2)
            else:
                i += 2
        elif opMode == 7:
            a = parmModeApply(getParmMode(parmModes), i+1)
            parmModes = parmModes[:-1]
            b = parmModeApply(getParmMode(parmModes), i+2)
            if a < b:
                prog[int(prog[i+3])] = "1"
            else:
                prog[int(prog[i+3])] = "0"
        elif opMode == 8:
            a = parmModeApply(getParmMode(parmModes), i+1)
            parmModes = parmModes[:-1]
            b = parmModeApply(getParmMode(parmModes), i+2)
            if a == b:
                prog[int(prog[i+3])] = "1"
            else:
                prog[int(prog[i+3])] = "0"
        elif opMode == 99:
            return 0
        else:
            i += 1
            
Input = open("Inputs/Day_05.txt", "r").read().split(",")
# Input = "1002,4,3,4,33".split(",")
# First_Part(Input)

Input = "3,9,8,9,10,9,4,9,99,-1,8".split(",")
Second_Part(Input)

