# -*- coding: utf-8 -*-
from numpy import *
import operator 
import matplotlib
import matplotlib.pyplot as plt
from os import listdir

def img2vector(filename):
	returnVect = zeros((1,1024))
	fr = open(filename)
	for i in range(32):
		lineStr = fr.readline()
		for j in range(32):
			returnVect[0,32*i+j] = int(lineStr[j])
	return returnVect

def classify0(inx,dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	diffMat = tile(inx, (dataSetSize,1))-dataSet
	sqDiffMat = diffMat**2
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances**0.5
	sortedDistIndicies = distances.argsort()
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
	sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)	
	return sortedClassCount[0][0]

def handwritingClassTest():
	hwLabels = []
	trainingFileList = listdir('trainingDigits')
	m = len(trainingFileList)
	trainingMat = zeros((m,1024))
	for i in range(m):
		fileNameStr = trainingFileList[i]
		fileStr = fileNameStr.split('.')[0]
		classNumStr = int(fileStr.split('_')[0])
		hwLabels.append(classNumStr)
		#放着每个文本的值
		trainingMat[i,:] = img2vector('trainingDigits/%s' % fileNameStr)
	testFileList = listdir('testDigits')
	errorCount = 0.0
	mTest = len(testFileList)
	for i in range(mTest):
		fileNameStr = testFileList[i]
		fileStr = fileNameStr.split('.')[0]
		classNumStr = int(fileStr.split('_')[0])
		vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
		classfierResult = classify0(vectorUnderTest,trainingMat,hwLabels,3)
		print "the classfier came back with: %d, the real answer is: %d"\
			% (classfierResult,classNumStr)
		if(classfierResult != classNumStr):errorCount += 1.0
	print "the total number of errors is:%d" % errorCount
	print "the total error rate is: %f" % (errorCount/float(mTest))

testVertor = img2vector('F:/ML/KNN/0_13.txt')
handwritingClassTest()