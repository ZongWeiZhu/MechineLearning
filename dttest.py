#-*- coding=utf-8 -*-
'''
2017.10.07
机器学习实战 决策树实验
Author:george
'''
from math import log

#计算给定数据的香农熵
def calcShannonEnt(dataSet):
	numEntries = len(dataSet)
	labelCounts = {}
	for featVec in dataSet:
		currentLabel = featVec[-1]
		if currentLabel not in labelCounts.keys():
			labelCounts[currentLabel] = 0
		labelCounts[currentLabel] += 1
	shannonEnt = 0.0
	for key in labelCounts:
		prob = float(labelCounts[key])/numEntries
		shannonEnt -= prob*log(prob,2)
	return shannonEnt

#自定义生成数据
def creatDataSet():
	dataSet = [[1,1,'yes'],
			[1,1,'yes'],
			[1,0,'no'],
			[0,1,'no'],
			[0,1,'no']]
	labels = ['no surfacing','flippers']
	return dataSet,labels 

#划分数据集
#返回 第几维数据axis等于value 的不包含该维的子集
def splitDataSet(dataSet, axis, value):
	retDataSet = []
	for featVec in dataSet:
		if featVec[axis] == value:
			reducedFeatVec = featVec[:axis]
			reducedFeatVec.extend(featVec[axis+1:])
			retDataSet.append(reducedFeatVec)
	return retDataSet

#选择信息熵最好的特征进行划分
def chooseBestFeatureSplit(dataSet):
	numFeature = len(dataSet[0])-1
	baseEntropy = calcShannonEnt(dataSet)
	bestInfoGain = 0.0; bestFeature = -1
	for i in range(numFeature):
		featList = [example[i] for example in dataSet] #把第i维的数据存进lIST中
		#print featList
		uniqueVals = set(featList)
		#print uniqueVals
		newEntropy = 0.0
		for value in uniqueVals:
			subDataSet = splitDataSet(dataSet, i, value)
			prob = len(subDataSet)/float(len(dataSet))
			newEntropy += prob*calcShannonEnt(subDataSet)
		infoGain = baseEntropy - newEntropy
		if(infoGain > bestInfoGain):
			bestInfoGain = infoGain
			bestFeature = i
	return bestFeature


dataSet,labels = creatDataSet()
print calcShannonEnt(dataSet)
print splitDataSet(dataSet,0,0)
print "best feature",chooseBestFeatureSplit(dataSet)
