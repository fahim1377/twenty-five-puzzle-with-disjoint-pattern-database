from state2 import State_cmplt
import heapq
import sys
import queue
import time

firstState = State_cmplt([14,6,15,13,17,2,18,12,5,21,7,24,19,3,4,8,22,10,23,16,20,9,1,11,0],None)
goal = State_cmplt([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 0],None)
HASH_BASE = 67
HASH_MODE = 1e+30
visitlist = set()

def checkTmp(state,father):
    if father is None:
        return True
    if(state.hash==father.hash):
        return False
    return checkTmp(state,father.father)


def checkTmp2(state,visitedlist):
    if state.hash in visitedlist:
        return False
    return True


def A_star(firstState,goal):
    fringe = []
    heapq.heappush(fringe,firstState)
    maxfn = firstState.fn
    cnt = 0
    while(True):
        if not fringe:
            return False

        node = heapq.heappop(fringe)
        cnt += 1
        if(node.fn < maxfn):                                       #show that if not be consistence 
            maxfn = node.fn
            print("hoy",node.depth)
        if(len(fringe)%1==0):
            print (node.vectors)
            print (node.fn,"fn")
            print (node.hn,"hn")
            print (node.depth,"depth")
            print (len(fringe),"fringe")
            print(cnt)

        # if(not checkTmp2(node,visitlist)):
        #     continue;
        # visitlist.add(node.hash)                               #for consistency must be here not when  you produce childs

        if(node.vectors==goal.vectors):
            return node
        for i in node.moves():
            # make_hash(i)
            # if(checkTmp2(i,visitlist)):                                      #make it quicker       note :you musnt add it to close list case of consistency
            heapq.heappush(fringe,i)
def Path(node,path):
    if(node is None):
        return path
    path.append(node)
    return Path(node.father,path)

def make_hash(state):
    state.hash = 1
    for i in state.vectors:
        state.hash *= HASH_BASE
        state.hash += i
        state.hash %= HASH_MODE

make_hash(goal)
make_hash(firstState)
# make_hash(dummystate)

sys.setrecursionlimit(100000)
node = A_star(firstState,goal)
path =[]
path = Path(node,path)
print(4)
for i in reversed(path):
    if(i.vectors==[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ]):
        continue
    sarr = [str(a) for a in i.vectors]
    print(', '.join(sarr))

print (len(path)-2)
