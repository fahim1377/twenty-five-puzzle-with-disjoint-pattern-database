from Heuristic import *
import copy
SIZE = 5
LENGHT = 25
class State:
    def __init__(self,vectors,father):
        self.vectors = vectors
        self.depth = 0
        self.notzeros = []
        self.father = father
        for i in range(1,len(vectors)):
            if i in vectors:
                self.notzeros.append(vectors.index(i))
        self.gn = 0
        self.hn = lnrCnflct_Pls_MnhtnDstnc(self)
        self.fn  = self.hn+self.gn
    def __lt__(self, other):
        if(self.fn < other.fn ):
            return True
        if(self.fn == self.fn):
            return self.hn < self.hn
        return False

    def moveRight(self,index):

        if(not (index+1)%SIZE) or self.vectors[index+1] or (not self.vectors[index]):
            return False
        childState1 = copy.deepcopy(self)
        childState1.father = self
        childState1.depth = self.depth+1
        childState1.vectors[index],childState1.vectors[index+1] = childState1.vectors[index+1],childState1.vectors[index]
        idx = childState1.notzeros.index(index)
        childState1.notzeros[idx] = index+1
        childState1.gn +=1
        childState1.hn = lnrCnflct_Pls_MnhtnDstnc(childState1)
        childState1.fn = childState1.hn +childState1.gn
        return childState1

    def moveLeft(self,index):
        if(not (index)%SIZE) or self.vectors[index-1] or (not self.vectors[index]):
            return False
        childState2 = copy.deepcopy(self)
        childState2.father = self
        childState2.depth = self.depth+1
        childState2.vectors[index],childState2.vectors[index-1] = childState2.vectors[index-1],childState2.vectors[index]
        idx = childState2.notzeros.index(index)
        childState2.notzeros[idx] = index-1
        childState2.gn +=1
        childState2.hn = lnrCnflct_Pls_MnhtnDstnc(childState2)
        childState2.fn = childState2.hn +childState2.gn
        return childState2
    def moveUp(self,index):
        if(index<SIZE) or self.vectors[index-SIZE] or (not self.vectors[index]):   # if index is not in first row or up is not blank and value of index is not zero
            return False
        childState3 = copy.deepcopy(self)
        childState3.father = self
        childState3.depth = self.depth+1
        childState3.vectors[index],childState3.vectors[index-SIZE] = childState3.vectors[index-SIZE],childState3.vectors[index]
        idx = childState3.notzeros.index(index)
        childState3.notzeros[idx] = index-SIZE
        childState3.gn +=1
        childState3.hn = lnrCnflct_Pls_MnhtnDstnc(childState3)
        childState3.fn = childState3.hn +childState3.gn
        return childState3
    def moveDown(self,index):
        if(index > (LENGHT - SIZE -1) ) or self.vectors[index+SIZE] or (not self.vectors[index]):
            return False
        childState4 = copy.deepcopy(self)
        childState4.father = self
        childState4.depth = self.depth+1
        childState4.vectors[index],childState4.vectors[index+SIZE] = childState4.vectors[index+SIZE],childState4.vectors[index]
        idx = childState4.notzeros.index(index)
        childState4.notzeros[idx] = index+SIZE
        childState4.gn +=1
        childState4.hn = lnrCnflct_Pls_MnhtnDstnc(childState4)
        childState4.fn = childState4.hn +childState4.gn
        return childState4


    def moves(self):
        states = []
        for i in self.notzeros:
            moveup = self.moveUp(i)
            movedown = self.moveDown(i)
            moveright = self.moveRight(i)
            moveleft = self.moveLeft(i)
            if(movedown):
                states.append(movedown)
            if(moveup):
                states.append(moveup)
            if(moveright):
                states.append(moveright)
            if(moveleft):
                states.append(moveleft)
        return states

