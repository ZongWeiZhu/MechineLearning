# -*- coding=utf-8 -*-
#4.5.3 测试算法
#程序清单 4-1
from numpy import *
def loadDataSet():
	postingList = [['my','dog','has','flea', \
					'problem','help','please'],
					['maybe','not','take','him',\
					'to','dog','park','stupid'],
					['my', 'dalmation', 'is', 'so', 'cute', \
					'I', 'love', 'him'],
					['stop','posting','stupid','worthless','garbage'],
					['mr','licks','ate','my','steak','how','to','stop','him'],
					['quit','buying','worthless','dog','food','stupid']]
	classVec = [0,1,0,1,0,1]
	return postingList,classVec

def createVocabList(dataSet):
	vocabSet = set([])
	for document in dataSet:
		vocabSet = vocabSet | set(document)
	return list(vocabSet)

def setOfWord2Vec(vocabList, inputSet):
	returnVec = [0]*len(vocabList)
	for word in inputSet:
		if word in vocabList:
			returnVec[vocabList.index(word)] = 1
		else:
			print "the word: %s is not in my Vocabulary!" % word
	return returnVec
#程序清单4-2
#功能应该就是统计每个单词出现的频率
def trainNB0(trainMatrix,trainCategory):
	numTrainDocs = len(trainMatrix)
	numWords = len(trainMatrix[0])
	#sum(trainCategory)=3
	#float(numTrainDocs)=6
	pAbusive = sum(trainCategory)/float(numTrainDocs)
	p0Num = ones(numWords)
	p1Num = ones(numWords)
	p0Denom = 2.0
	p1Denom = 2.0
	for i in range(numTrainDocs):
		if trainCategory[i] == 1:
			p1Num += trainMatrix[i] #统计单词出现的次数
			p1Denom += sum(trainMatrix[i])#统计所有单词出现的次数 
		else:
			p0Num += trainMatrix[i]
			p0Denom += sum(trainMatrix[i])
	p1Vect = log(p1Num/p1Denom)
	p0Vect = log(p0Num/p0Denom)
	return p0Vect,p1Vect,pAbusive

listOPosts,listClasses = loadDataSet()
myVocabList = createVocabList(listOPosts)
#print myVocabList
#print setOfWord2Vec(myVocabList,['cute','love'])
trainMat = []
for postingDoc in listOPosts:
	trainMat.append(setOfWord2Vec(myVocabList,postingDoc))
p0V,p1V,pAb = trainNB0(trainMat,listClasses)
