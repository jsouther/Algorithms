"""
Created on Mon Dec  2 15:41:48 2019

@author: JSO
"""

import time

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

def firstFit(capacity, weights):
    bins = []
    
    for weight in weights:
        foundBin = None
        for binX in bins:
            if binX.weight + weight <= capacity:
                binX.weight = binX.weight + weight
                foundBin = True
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
capacityWeights = readTestCases('bin.txt')

i = 1
for case in capacityWeights:
    ticks = time.time_ns()
    firstFitBins = firstFit(case[0], case[1])
    firstFitTime = time.time_ns() - ticks
    
    ticks = time.time_ns()
    bestFitBins = bestFit(case[0], case[1])
    bestFitTime = time.time_ns() - ticks

    print("Test Case " + str(i) + " First Fit: " + str(firstFitBins) + ", " + str(firstFitTime) + "ns."
          " First Fit Decreasing: " + ", " + str(bestFitTime) + "ns."
          " Best Fit: " + str(bestFitBins) + ", " + str(bestFitTime) + "ns.")
    i = i + 1