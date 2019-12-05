# Bin Packing
# Jacob Souther - CS325 HW 8, Problem 1
# Date: 04-Dec-2019
# Description: Implementation of first fit, first fit decreasing, and best fit bin packing approximation algorithms

import time

#Bin class. Bins are initialized with a weight of 0 and weight remaining equal to capacity.
class Bin:
    def __init__(self, capacity):
        self.weight = 0
        self.weightRemaining = capacity

#Merge sort takes an array and sorts it in decreasing order
def mergeSortDecreasing(array):
			if len(array) > 1:
				middle = len(array)//2

				leftArray = array[:middle]
				rightArray = array[middle:]

				mergeSortDecreasing(leftArray)
				mergeSortDecreasing(rightArray)

				#index of leftArray
				i = 0
				#index of rightArray
				j = 0
				#index of array
				k = 0

				#While left and right arrays contain items
				while i < len(leftArray) and j < len(rightArray):
					#if left value is greater, add it to the array
					if leftArray[i] > rightArray[j]:
						array[k] = leftArray[i]
						i += 1
					#if right value is lower, add it to the array
					else:
						array[k] = rightArray[j]
						j += 1
					k += 1

				#while only left has items, add them to the array
				while i < len(leftArray):
					array[k] = leftArray[i]
					i += 1
					k += 1

				#while only rightArray has items, add them to the array
				while j < len(rightArray):
					array[k] = rightArray[j]
					j += 1
					k += 1

#Reads a txt file to retrieve the numnber of test cases, items in each test case, and their weights
#Returns a list of pairs, first item in the pair is the bin capacity. Second item in the pair is a list of the item's weights
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

# Fill bins by first fit. Items are added in order to the first bin they fit. If no bin fits, a new bin is made.
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

# Fill bins by first fit. Items are first sorted in decreasing order and then placed in the same manner as first fit.
def firstFitDecreasing(capacity, weights):
    mergeSortDecreasing(weights)
    
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

# Items are added in order. Items are placed into the bin which leaves the least amount of leftover space.
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
    
    ticks = time.time_ns()
    firstFitDecreasingBins = firstFitDecreasing(case[0], case[1])
    firstFitDecreasingTime = time.time_ns() - ticks

    print("Test Case " + str(i) + " First Fit: " + str(firstFitBins) + ", " + str(firstFitTime) + "ns."
          " First Fit Decreasing: " + str(firstFitDecreasingBins) + ", " + str(firstFitDecreasingTime) + "ns."
          " Best Fit: " + str(bestFitBins) + ", " + str(bestFitTime) + "ns.")
    i = i + 1