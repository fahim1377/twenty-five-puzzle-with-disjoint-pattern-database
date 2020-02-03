from copy import copy

import copy

from Heuristic2 import database
SIZE = 5
LENGHT = 25
class State_cmplt:
    def __init__(self,vectors,father):
        self.vectors = vectors
        self.zeroindex = vectors.index(0)
        self.depth = 0
        self.father = father
        self.gn = 0

        self.hn = database(self)
        self.fn  = self.hn+self.gn
    def __lt__(self, other):
        if(self.fn < other.fn ):
            return True
        if(self.fn == self.fn):
            return self.hn < self.hn
        return False

    def moveRight(self):
        if(not (self.zeroindex+1)%SIZE):
            return False
        childState1 = copy.deepcopy(self)
        childState1.father = self
        childState1.depth = self.depth+1
        childState1.vectors[childState1.zeroindex],childState1.vectors[childState1.zeroindex+1] = childState1.vectors[childState1.zeroindex+1],childState1.vectors[childState1.zeroindex]
        childState1.zeroindex += 1 
        childState1.gn +=1
        childState1.hn = database(childState1)
        childState1.fn = childState1.hn +childState1.gn
        return childState1
    
    def moveLeft(self):
        if(not (self.zeroindex)%SIZE):
            return False
        childState2 = copy.deepcopy(self)
        childState2.father = self
        childState2.depth = self.depth+1
        childState2.vectors[childState2.zeroindex],childState2.vectors[childState2.zeroindex-1] = childState2.vectors[childState2.zeroindex-1],childState2.vectors[childState2.zeroindex]
        childState2.zeroindex -= 1 
        childState2.gn +=1
        childState2.hn = database(childState2)
        childState2.fn = childState2.hn +childState2.gn
        return childState2
    def moveUp(self):
        if(self.zeroindex < SIZE):
            return False
        childState3 = copy.deepcopy(self)
        childState3.father = self
        childState3.depth = self.depth+1
        childState3.vectors[childState3.zeroindex],childState3.vectors[childState3.zeroindex-SIZE] = childState3.vectors[childState3.zeroindex-SIZE],childState3.vectors[childState3.zeroindex]
        childState3.zeroindex -= SIZE
        childState3.gn +=1
        childState3.hn = database(childState3)
        childState3.fn = childState3.hn +childState3.gn
        return childState3
    def moveDown(self):
        if(self.zeroindex > (LENGHT-SIZE-1) ):
            return False
        childState4 = copy.deepcopy(self)
        childState4.father = self
        childState4.depth = self.depth+1
        childState4.vectors[childState4.zeroindex],childState4.vectors[childState4.zeroindex+SIZE] = childState4.vectors[childState4.zeroindex+SIZE],childState4.vectors[childState4.zeroindex]
        childState4.zeroindex += SIZE
        childState4.gn +=1
        childState4.hn = database(childState4)
        childState4.fn = childState4.hn +childState4.gn
        return childState4
    

    def moves(self):
        states = []
        moveup = self.moveUp()
        movedown = self.moveDown()
        moveright = self.moveRight()
        moveleft = self.moveLeft()
        if(movedown):
            states.append(movedown)
        if(moveup):
            states.append(moveup)
        if(moveright):
            states.append(moveright)
        if(moveleft):
            states.append(moveleft)
        return states

