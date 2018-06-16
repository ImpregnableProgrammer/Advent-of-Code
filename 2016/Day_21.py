
# First Part

def Scrambler(password, operations):
    for i in operations[:-1].split("\n"):
        s = i.split(" ")
        if s[0] == "swap":
            if s[1] == "position":
                indexOne = min(int(s[2]), int(s[5]))
                indexTwo = max(int(s[2]), int(s[5]))
            else:
                indexOne = min(password.find(s[2]), password.find(s[5]))
                indexTwo = max(password.find(s[2]), password.find(s[5]))
            password = password[:indexOne] + password[indexTwo] + password[indexOne+1:indexTwo] + password[indexOne] + password[indexTwo+1:]
        elif s[0] == "rotate":
            if s[1] == "based":
                index = password.find(s[6])
                numberTimes = index + 1 + 1 * (index >= 4)
                while numberTimes > 0:
                    password = password[-numberTimes:] + password[:-numberTimes]
                    numberTimes -= len(password)
            else:
                password = password[int(s[2]):] + password[:int(s[2])] if s[1] == "left" else password[-int(s[2]):] + password[:-int(s[2])]
        elif s[0] == "reverse":
            password = password[:int(s[2])] + password[int(s[2]):int(s[4])+1][::-1] + password[int(s[4])+1:]
        else:
            letter = password[int(s[2])]
            password = password[:int(s[2])] + password[int(s[2])+1:]
            password = password[:int(s[5])] + letter + password[int(s[5]):]
    return password

Input = open("Large_Inputs/Day_21_Operations", "r")

print(Scrambler("abcdefgh", Input.read()))

# SAMPLE INPUT
# print(Scrambler("abcde", '''swap position 4 with position 0
# swap letter d with letter b
# reverse positions 0 through 4
# rotate left 1 step
# move position 1 to position 4
# move position 3 to position 0
# rotate based on position of letter b
# rotate based on position of letter d
# '''))


# Second Part

def relativeRotation(password, char):
    index = password.find(char)
    numberTimes = index + 1 + 1 * (index >= 4)
    while numberTimes > 0:
        password = password[-numberTimes:] + password[:-numberTimes]
        numberTimes -= len(password)
    return password
    
    
def Unscrambler(password, operations):
    for i in operations[:-1].split("\n")[::-1]:
        s = i.split(" ")
        if s[0] == "swap":
            if s[1] == "position":
                indexOne = min(int(s[2]), int(s[5]))
                indexTwo = max(int(s[2]), int(s[5]))
            else:
                indexOne = min(password.find(s[2]), password.find(s[5]))
                indexTwo = max(password.find(s[2]), password.find(s[5]))
            password = password[:indexOne] + password[indexTwo] + password[indexOne+1:indexTwo] + password[indexOne] + password[indexTwo+1:]
        elif s[0] == "rotate":
            if s[1] == "based":
                currPassword = password
                while password != relativeRotation(currPassword, s[6]):
                    currPassword = currPassword[1:] + currPassword[:1]
                password = currPassword
            else:
                password = password[int(s[2]):] + password[:int(s[2])] if s[1] == "right" else password[-int(s[2]):] + password[:-int(s[2])]
        elif s[0] == "reverse":
            password = password[:int(s[2])] + password[int(s[2]):int(s[4])+1][::-1] + password[int(s[4])+1:]
        else:
            letter = password[int(s[5])]
            password = password[:int(s[5])] + password[int(s[5])+1:]
            password = password[:int(s[2])] + letter + password[int(s[2]):]
    return password

Input = open("Large_Inputs/Day_21_Operations", "r")

print(Unscrambler("fbgdceah", Input.read()))

# SAMPLE INPUT REVERSED
# print(Unscrambler("decab", '''swap position 4 with position 0
# swap letter d with letter b
# reverse positions 0 through 4
# rotate left 1 step
# move position 1 to position 4
# move position 3 to position 0
# rotate based on position of letter b
# rotate based on position of letter d
# '''))
            
            
