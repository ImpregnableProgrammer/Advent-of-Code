def First_Part(code):
    for i in range(0, len(code), 4):
        if code[i] in (1, 2):
            a, b, c = code[i+1:i+4]
            op = lambda a, b: a + b if code[i] == 1 else a * b
            code = code[:c] + [op(code[a], code[b])] + code[c+1:]
        elif code[i] == 99:
            break
        else:
            assert True, "Something went wrong!"
    return code[0]

def Second_Part(code, goal = 19690720):
    for i in range(100):
        for j in range(100):
            oldCode = code
            code = code[:1] + [i, j] + code[3:]
            if First_Part(code) == goal:
                return i, j
            else:
                code = oldCode
    
with open("Inputs/Day_02.txt", "r") as Input:
    Input = [*map(int, Input.read().split(","))]
    Input1 = Input[:1] + [12, 2] + Input[3:]
    print(First_Part(Input1))
    print(Second_Part(Input))
    
        
