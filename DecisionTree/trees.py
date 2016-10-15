# -*- coding: utf-8 -*-
from math import log

def calcShannonEnt(dataSet):
	numEntries = len(dataSet)
	labelCounts = {}
	for featVec in dataSet:
		currentLabel = featVec[-1]
		if currentLabel not in labelCounts.keys():
			labelCounts[currentLabel] = 0
		labelCounts[currentLabel]+=1
	shannonEnt = 0.0
	for key in labelCounts:
		prob = float(labelCounts[key])/numEntries
		shannonEnt -= prob*log(prob,2)
	return shannonEnt

def createDataSet():
	dataSet = [[1,1,'yes'],
			[1,1,'yes'],
			[1,0,'no'],
			[0,1,'no'],
			[0,1,'no']]
	labels = ['no surfacing','flippers']
	return dataSet,labels
def splitDataSet(dataSet, axis, value):
	retDataSet = []
	for featVec in dataSet:
		if featVec[axis] == value:
			#将featVec的除了下标为axis的元素存放到reducedFeatVec中
			reducedFeatVec = featVec[:axis]
			reducedFeatVec.extend(featVec[axis+1:])
			retDataSet.append(reducedFeatVec)
	return retDataSet
def chooseBestFeatureToSolit(dataSet):
	numFeatures = len(dataSet[0]) - 1
	#entropy 熵
	baseEntropy = calcShannonEnt(dataSet)
	bestInfoGain = 0.0
	bestFeature = -1
	for i in range(numFeatures):
		featList = [example[i] for example in dataSet]
		uniqueVals = set(featList)
		newEntropy = 0.0
		for value in uniqueVals:
			subDataSet = splitDataSet(dataSet,i,value)
			prob = len(subDataSet)/float(len(dataSet))
			# prob 可能性 应该就是百分比
			newEntropy += prob * calcShannonEnt(subDataSet)
		infoGain = baseEntropy -newEntropy
		# newEntropy越小 infoGain越大 混乱程度越小
		if(infoGain > bestInfoGain):
			bestInfoGain = infoGain
			bestFeature = i

	return bestFeature

def createTree(dataSet,labels):
	classList = [example[-1] for example in dataSet]
	if classList.count(classList[0]) == len(classList):
		return classList[0]
	if len(dataSet[0]) ==1:
		return majorityCnt(classList)
	bestFeat = chooseBestFeatureToSolit(dataSet)

	bestFeatLabel = labels[bestFeat]

	myTree = {bestFeatLabel:{}}

	del(labels[bestFeat])
	FeatValues = [example[bestFeat] for example in dataSet]

	uniqueVals = set(FeatValues)
	for value in uniqueVals:
		subLabels = labels[:]
		myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet,bestFeat,value),subLabels)

	return myTree



myDat,labels = createDataSet()
#print calcShannonEnt(myDat)
#print splitDataSet(myDat,0,1)
#print chooseBestFeatureToSolit(myDat)
print createTree(myDat,labels)