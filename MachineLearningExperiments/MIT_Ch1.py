#This program will put concepts from the MIT open courseware machine learning
#course's first lecture into practice.  It will read from a training set of
#images, then attempt to create the set of parameters that can most accurately
#classify the images as containing either an X or an O.

import numpy as np
import cv2
import time

#Labelled as -1 for X, or 1 for O.
LABELS = [-1,1,1,-1,-1,1,1,1,-1,1,-1,-1,1,1,-1,1,1,-1,-1,1,1,1,-1,1,-1,-1,1,1,-1,-1,-1,1]


def ImportTrainingSet():
#Import the training set.
    training = []
    for i in range(1,33):
        name = "T" + str(i) +".png" 
        image = np.array(cv2.imread(name,0))
        vec = []
        for j in image:
            for k in j:
                vec.append(k)
        training.append(vec)
        
    
    return training



def InitParams():
#Creates an array of the correct size and fills it with 
    sample = cv2.imread("T1.png",0)
    para=[]
    for i in range(0,sample.size):
        para.append(0)
    return para
    
def ImEval(image,theta):
#Evaluate an image using the parameter set.
    total = 0L
    for i in range(0,len(image)):
        total += image[i] * theta[i]
    return np.sign(total)


    
def Perceptron(theta,labels,results,images): 
#Update the parameter set with new values based on the previous testing cycle.
    
    for i in range(0,len(results)):
        if(results[i] != labels[i]):
            for j in range(0,len(theta)):
                theta[j] = theta[j] + labels[i] * images[i][j]
    return theta

def ReportAccuracy(results,labels):
#Evaluate the cycle's accuracy on the training set.
    total = len(labels)
    correct = 0
    for i in range(0,total):
        if results[i] == labels[i]:
            correct += 1
    print("Accuracy: " + str(correct) + "/" + str(total))
    if correct == total:
        return False
    else:
        return True


def main(labels):
#The main function of the program.
    startTime = time.time()
    tSet = ImportTrainingSet()
    theta = InitParams()

    incomplete = True
    counter = 0
    while incomplete:
    #Learning cycle loop.
        oldTime = time.time()
        results = []

        for i in tSet:
            results.append(ImEval(i,theta))

        theta = Perceptron(theta, labels,results,tSet)
        incomplete = ReportAccuracy(results, labels)
        elapsed = time.time() - oldTime
        counter +=1
        print("Learning cycle "+str(counter) + " complete.  Time elapsed: " + str(elapsed))
    elapsed = time.time() - startTime
    print("All cycles completed.  Training took " + str(elapsed) + " seconds.")
    output = open("model.txt", "w")
    output.write(str(theta))
    output.close()

main(LABELS)





        
