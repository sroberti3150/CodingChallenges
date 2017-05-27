#This program will demonstrate a method for determining the lowest-order
#polynomial that passes through every point in a randomly-generated set.

import numpy as np
from random import randint
from random import sample
import time


def CreateSet():#Creates the set of points.
    pointSet = []
    setSize = int(input("How many points will the program work with?"))
    xBuffer = 0
    x = -1*setSize

    for i in range(setSize):
        x+=xBuffer
        xBuffer = randint(1,4)
        pointSet.append((x, randint(-100,100)))
    
    
    
    return pointSet

def ConstructArrays(pointSet):#Reorganizes the set of points into the necessary NumPy Arrays
    y=[]
    x=[]
    for i in range(0, len(pointSet)):
        y.append(pointSet[i][1])
        x.append(pointSet[i][0])

    npY = np.array(y,dtype='float')
    npY = npY.transpose()
    
    xSize = len(pointSet)
    matrix = []
    for i in range(xSize):
        row = []
        for j in range(xSize):
            row.append(x[i]**(j))
        
        matrix.append(row)
    npX = np.array(matrix,dtype='float')
    return npX, npY

  
points=CreateSet()
start = time.time() 
x,y = ConstructArrays(points)

sol = np.linalg.solve(x,y)
deg = 0
string = ""
for i in sol:
    string = string + "("+str(i) +")"+ "x^" + str(deg) + " "
    deg +=1
    string += "+ "
output = string[:-2]
output += "= 0"
print(output)
elapsed = time.time() - start
print("Seconds taken to execute: " + str(elapsed))
