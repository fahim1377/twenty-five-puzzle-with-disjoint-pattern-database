from Database import A_star
from state import State
import json
SIZE = 25
subpuz1 = [0,1,1,0,0,0,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0]
subpuz2 = [0,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
subpuz3 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,0]
subpuz4 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,1]


goal1 = State([1, 2, 0, 0, 0, 6, 7, 0, 0, 0, 11, 12, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],None)
goal2 = State([0, 0, 3, 4, 5, 0, 0, 8, 9, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],None)
goal3 = State([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 17, 18, 0, 0, 21, 22, 23, 0, 0],None)
goal4 = State([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 15, 0, 0, 0, 19, 20, 0, 0, 0, 24,0],None)

dict = {}

f = open('data1.json')
dict = json.load(f)


f = open('data2.json')
dict2 = json.load(f)

f = open('data3.json')
dict3 = json.load(f)

f = open('data4.json')
dict4 = json.load(f)


def database(state):
    l = []
    h1 = 0
    h2 = 0
    ################################### part 1
    for i in range(SIZE):
        if subpuz1[state.vectors[i]]:
            l.append(state.vectors[i])
        else:
            l.append(0)
    firstState = State(l,None)
    hash = ' '.join([str(elem) for elem in firstState.notzeros])

    if hash in dict:
        h1 = dict[hash]
    else:
        h1 = A_star(firstState,goal1)
        dict[hash] = h1
        with open('data1.json', 'w') as f:
            json.dump(dict, f)
    ####################################################
    #################################part2
    l = []
    for i in range(SIZE):
        if subpuz2[state.vectors[i]]:
            l.append(state.vectors[i])
        else:
            l.append(0)
    firstState = State(l,None)
    hash = ' '.join([str(elem) for elem in firstState.notzeros])

    if hash in dict2:
        h2 = dict2[hash]
    else:
        h2 = A_star(firstState,goal2)
        dict2[hash] = h2
        with open('data2.json', 'w') as f:
            json.dump(dict2, f)
    ####################################################
    #################################part3
    l = []
    for i in range(SIZE):
        if subpuz3[state.vectors[i]]:
            l.append(state.vectors[i])
        else:
            l.append(0)
    firstState = State(l,None)
    hash = ' '.join([str(elem) for elem in firstState.notzeros])

    if hash in dict3:
        h3 = dict3[hash]
    else:
        h3 = A_star(firstState,goal3)
        dict3[hash] = h3
        with open('data3.json', 'w') as f:
            json.dump(dict2, f)
    ####################################################
    #################################part4
    l = []
    for i in range(SIZE):
        if subpuz4[state.vectors[i]]:
            l.append(state.vectors[i])
        else:
            l.append(0)
    firstState = State(l,None)
    hash = ' '.join([str(elem) for elem in firstState.notzeros])

    if hash in dict4:
        h4 = dict4[hash]
    else:
        h4 = A_star(firstState,goal4)
        dict4[hash] = h4
        with open('data4.json', 'w') as f:
            json.dump(dict2, f)

    return h1+h2+h3+h4
    ####################################################


