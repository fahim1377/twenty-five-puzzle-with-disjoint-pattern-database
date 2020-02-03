from state import *
import queue
import json
import sys
import random
import heapq
HASH_BASE = 67
HASH_MODE = 1e+30

SIZE = 25

goal1 = State([1, 2, 0, 0, 0, 6, 7, 0, 0, 0, 11, 12, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],None)
goal2 = State([0, 0, 3, 4, 5, 0, 0, 8, 9, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],None)
goal3 = State([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 17, 18, 0, 0, 21, 22, 23, 0, 0],None)
goal4 = State([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 15, 0, 0, 0, 19, 20, 0, 0, 0, 24,0],None)

visitlist = set()

def checkTmp2(state,father):

    if father is None:
        return True
    if(state.hash==father.hash):
        return False
    return checkTmp2(state,father.father)

def checkTmp(state):
    if state.hash in visitlist:
        return False
    return True

def make_hash(state):
    state.hash = 1
    for i in state.notzeros:                      #hash base on locaton of notzeros
        state.hash *= HASH_BASE
        state.hash += i
        state.hash %= HASH_MODE


def A_star(firstState,goal):
    fringe = []
    heapq.heappush(fringe,firstState)
    maxfn = firstState.fn
    cnt = 0
    make_hash(firstState)
    visitlist.clear()
    while(True):
        if not fringe:
            return False

        node = heapq.heappop(fringe)
        cnt += 1
        if(node.fn < maxfn):                                       #show that if not be consistence
            maxfn = node.fn
            print("Database hoy",node.depth)
        # if(len(fringe)%1000==0):
        #     print (node.vectors)
        #     print (node.fn,"fn")
        #     print (node.hn,"hn")
        #     print (node.depth,"depth")
        #     print (len(fringe),"fringe")
        #     print(cnt)

        if(not checkTmp(node)):
            continue;
        visitlist.add(node.hash)                               #for consistency must be here not when  you produce childs

        if(node.vectors==goal.vectors):
            return node.depth
        for i in node.moves():
            make_hash(i)
            if(checkTmp(i)):                                      #make it quicker       note :you musnt add it to close list case of consistency
                heapq.heappush(fringe,i)


###############################  part1: 5o random state generate and find the hn
# dict = {}
# for i in range(50):
#     numDB1 = [1,2,6,7,11,12,13]
#     l = []
#     for d in range(SIZE):
#         l.append(0)
#     for j in numDB1:
#         r = random.randint(0, LENGHT-1)
#         while l[r]:
#             r = random.randint(0, LENGHT-1)
#         l[r] = j
#     ranstate = State(l,None)
#     make_hash(ranstate)
#     h = A_star(ranstate,goal1)
#     dict[' '.join([str(elem) for elem in ranstate.notzeros])] = h
#     print(dict,i)
#     with open('data1.json', 'w') as f:
#         json.dump(dict, f)


##################################### part 2 :50 state generate and find the hn
# dict = {}
# for i in range(50):
#     numDB1 = [3,4,5,8,9,10]
#     l = []
#     for d in range(SIZE):
#         l.append(0)
#     for j in numDB1:
#         r = random.randint(0, LENGHT-1)
#         while l[r]:
#             r = random.randint(0, LENGHT-1)
#         l[r] = j
#     ranstate = State(l,None)
#     make_hash(ranstate)
#     h = A_star(ranstate,goal2 )
#     dict[' '.join([str(elem) for elem in ranstate.notzeros])] = h
#     print(dict,i)
#     with open('data2.json', 'w') as f:
#         json.dump(dict, f)
##################################### part 3 :50 state generate and find the hn
# dict = {}
# for i in range(21,50):
#     numDB1 = [16,17,18,21,22,23]
#     l = []
#     for d in range(SIZE):
#         l.append(0)
#     for j in numDB1:
#         r = random.randint(0, LENGHT-1)
#         while l[r]:
#             r = random.randint(0, LENGHT-1)
#         l[r] = j
#     ranstate = State(l,None)
#     make_hash(ranstate)
#     h = A_star(ranstate,goal3 )
#     if ' '.join([str(elem) for elem in ranstate.notzeros]) in dict:
#         continue
#     dict[' '.join([str(elem) for elem in ranstate.notzeros])] = h
#     print(dict,i)
#     with open('data3.json', 'w') as f:
#         json.dump(dict, f)
##################################### part 4 :50 state generate and find the hn
# dict = {}
# for i in range(50):
#     numDB1 = [14,15,19,20,24]
#     l = []
#     for d in range(SIZE):
#         l.append(0)
#     for j in numDB1:
#         r = random.randint(0, LENGHT-1)
#         while l[r]:
#             r = random.randint(0, LENGHT-1)
#         l[r] = j
#     ranstate = State(l,None)
#     make_hash(ranstate)
#     h = A_star(ranstate,goal4 )
#     dict[' '.join([str(elem) for elem in ranstate.notzeros])] = h
#     print(dict,i)
#     with open('data4.json', 'w') as f:
#         json.dump(dict, f)
