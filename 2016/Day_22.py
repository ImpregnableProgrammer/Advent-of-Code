
# First Part

import re

def viablePairs(s):
    s = [*map(lambda i:re.sub(" +", " ", i), s.split("\n")[2:-1])]
    c = 0
    for o in range(len(s)):
        z = s[o].split(" ")
        for q in range(len(s)):
            m = s[q].split(" ")
            if int(z[2][:-1]) and int(z[2][:-1]) <= int(m[3][:-1]) and o != q:
                c += 1
    return c

Input = open("Large_Inputs/Day_22_Nodes", "r")

print(viablePairs(Input.read()))


# Second Part

# Defunct recursive search method that brute-forcingly and recursively searches for the first empty node encountered beginning from the goal node
# def Search(state, maxX, maxY, currX, currY, newStates, visited):
#     currentNode = state[(currX, currY)]
#     visited += [(currX, currY)]
#     for x, y in [(1,0), (0,1), (-1,0), (0,-1)]:
#         newX = currX + x
#         newY = currY + y
#         currState = state
#         if newX > -1 and newX <= maxX and newY > -1 and newY <= maxY and (newX, newY) not in visited:
#             adjacentNode = state[(newX, newY)]
#             if currentNode["Used"] <= adjacentNode["Size"] - adjacentNode["Used"]:
#                 currState[(currX, currY)]["Used"] = 0
#                 currState[(newX, newY)]["Used"] += currentNode["Used"]
#                 return currState, currX, currY
#             else:
#                 currState, newX, newY = Search(currState, maxX, maxY, newX, newY, newStates, visited)
#                 currState[(newX, newY)]["Used"] += currentNode["Used"]
#                 currState[(currX, currY)]["Used"] = 0
#         newStates += [currState]
#         return currState, currX, currY

def Second_Part(s):
    s = [*map(lambda i:re.sub(" +", " ", i), s.split("\n")[2:])][:-1]
    Nodes = {(int(i.split(" ")[0].split("-")[1][1:]), int(i.split(" ")[0].split("-")[2][1:])) : (int(i.split(" ")[1][:-1]), int(i.split(" ")[2][:-1])) for i in s}
    maxX = max(i[0] for i in Nodes.keys())
    maxY = max(i[1] for i in Nodes.keys())
    for i in Nodes.keys():            
        if Nodes[i][1] < 1:
            emptyNode = i
            break
    Nodes["Goal"] = (maxX, 0)
    Nodes["Empty"] = Nodes["PrevEmpty"] = emptyNode
    States = (Nodes,)
    oldStates = set()
    steps = 0
    while 1:
        newStates = tuple()
        for state in States:
            emptyNode = state["Empty"]
            if state["Goal"] == (0, 0):
                return steps
            for x, y in [(1,0), (0,1), (-1,0), (0,-1)]:
                currState = state.copy()
                adjNode = (emptyNode[0] + x, emptyNode[1] + y)
                if adjNode[0] >= 0 and adjNode[0] <= maxX and adjNode[1] >= 0 and adjNode[1] <= maxY and adjNode != currState["PrevEmpty"] and currState[adjNode][1] <= currState[emptyNode][0]:
                    currState[emptyNode] = (currState[emptyNode][0], currState[adjNode][1])
                    currState[adjNode] = (currState[adjNode][0], 0)
                    currState["Empty"] = adjNode
                    currState["PrevEmpty"] = emptyNode
                    if currState["Goal"] == adjNode:
                        currState["Goal"] = emptyNode
                    if (currState["Goal"], currState["Empty"]) not in oldStates:
                        newStates += (currState,)
                        oldStates.add((currState["Goal"], currState["Empty"]))
        States = newStates
        steps += 1

Input = open("Large_Inputs/Day_22_Nodes", "r")

# OUTPUTS THE CORRECT ANSWER OF 192 IN 2 MIN. 20 SEC!
print(Second_Part(Input.read()))

# SAMPLE INPUT
# print(Second_Part('''
# Filesystem            Size  Used  Avail  Use%
# /dev/grid/node-x0-y0   10T    8T     2T   80%
# /dev/grid/node-x0-y1   11T    6T     5T   54%
# /dev/grid/node-x0-y2   32T   28T     4T   87%
# /dev/grid/node-x1-y0    9T    7T     2T   77%
# /dev/grid/node-x1-y1    8T    0T     8T    0%
# /dev/grid/node-x1-y2   11T    7T     4T   63%
# /dev/grid/node-x2-y0   10T    6T     4T   60%
# /dev/grid/node-x2-y1    9T    8T     1T   88%
# /dev/grid/node-x2-y2    9T    6T     3T   66%
# '''))
