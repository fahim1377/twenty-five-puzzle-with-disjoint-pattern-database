# from state import *

size = 5
goal_row = [4,0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4]
goal_column = [4,0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,0,1,2,3]
def Manhatan_distance(state):

    value = 0
    for i in range(len(state.vectors)):
        if(state.vectors[i]==0):
            continue
        current_row = (int)(i/size)
        current_column = (int)(i%size)
        value += abs(goal_column[state.vectors[i]]-current_column)+abs(goal_row[state.vectors[i]]-current_row)
    return value

def linearhoritzonalconflict(state):
    lc=0
    for row in range(0,size):

        for col in range(0,size):
            max=state.vectors[row*size+col]
            if state.vectors[row*size + col]==0 or goal_row[state.vectors[row*size+col]]!=row:
                continue
            for tile in range(col,size):
                tilevalue = state.vectors[row*size+tile]
                if tilevalue !=0 and goal_row[tilevalue] == row:
                    if tilevalue >= max:
                        continue
                    else:
                        lc +=2
    return lc
def linearverticalconflict(state):
    lc=0
    for col in range(0,size):

        for row in range(0,size):
            max=state.vectors[row*size + col]
            if state.vectors[row*size + col]==0 or goal_column[state.vectors[row*size+col]]!= col:
                continue
            for tile in range(row,size):
                tilevalue = state.vectors[tile*size+col]
                if tilevalue !=0 and goal_column[tilevalue] == col:
                    if tilevalue >= max:
                        continue
                    else:
                        lc +=2
    return lc


def lnrCnflct_Pls_MnhtnDstnc(state):
    return Manhatan_distance(state)+linearverticalconflict(state)+linearhoritzonalconflict(state)