# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 13:39:22 2019

@author: JSO
"""

import time
from random import seed
from random import randint
seed(time.time())

def createTestFile(capacity, cases, minItems, maxItems, minWeight, maxWeight):
    with open('bin.txt', 'w') as outFile:
        outFile.write(str(cases) + "\n")
        
        for _ in range(cases):
            outFile.write(str(capacity) + "\n")
            numItems = randint(minItems,maxItems)
            outFile.write(str(numItems) + "\n")
        
            for _ in range(numItems):
                value = randint(minWeight, maxWeight)
                outFile.write(str(value) + " ")
            outFile.write("\n")

def readTestCases(fileName):
    with open(fileName, 'r') as inFile:
        numTestCases = int(inFile.readline())
        
        testCaseCapacityAndWeights = []
        for _ in range(numTestCases):
            binCapacity = int(inFile.readline())
            inFile.readline()
            
            weights = []
            items = inFile.readline().split()
            for weight in items:
                weights.append(int(weight))
            testCaseCapacityAndWeights.append([binCapacity, weights])
        
        return testCaseCapacityAndWeights

class Bin:
    def __init__(self, capacity):
        self.weight = 0
        self.weightRemaining = capacity        
    #def addItem(self, weight):
        #self.weight + weight

def firstFit(capacity, weights):
    bins = []
    
    for weight in weights:
            foundBin = None
            for binX in bins:
                if binX.weight + weight <= capacity:
                    binX.weight = binX.weight + weight
                    foundBin = True
                    #print(binX.weight)
                    break
                    
            if not foundBin:
                bins.append(Bin(capacity))
                bins[-1].weight = bins[-1].weight + weight
    return len(bins)

def bestFit(capacity, weights):
    bins = []
    
    for weight in weights:
        foundBin = None
        minimum = capacity + 1
        for binX in bins:
            if binX.weightRemaining >= weight and binX.weightRemaining - weight < minimum:
                minimum = binX.weightRemaining - weight
                index = bins.index(binX)
                #binX.weight = binX.weight + weight
                foundBin = True
        
        if foundBin:
            bins[index].weightRemaining = bins[index].weightRemaining - weight
        
        else:
            bins.append(Bin(capacity))
            bins[-1].weightRemaining = bins[-1].weightRemaining - weight
    return len(bins)

"""
MAIN FUNCTION
"""      
createTestFile(60, 20, 10000, 50000, 1, 30)    
capacityWeights = readTestCases('bin.txt')

i = 1
for case in capacityWeights:
    ticks = time.time()
    firstFitBins = firstFit(case[0], case[1])
    firstFitTime = time.time() - ticks
    
    ticks = time.time()
    bestFitBins = bestFit(case[0], case[1])
    bestFitTime = time.time() - ticks

    print("Test Case " + str(i) + ": Items: " + str(len(case[1])) + " First Fit: " + str(firstFitBins) + ", " + "%.2f" % firstFitTime + "s."
          " First Fit Decreasing: " + ", " + str(bestFitTime) + "s."
          " Best Fit: " + str(bestFitBins) + ", " + "%.2f" % bestFitTime + "s.")
    i = i + 1
    
    