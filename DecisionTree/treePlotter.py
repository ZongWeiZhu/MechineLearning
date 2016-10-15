# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt 

decisionNode = dict(boxstyle = "sawtooth", fc = "0.8")
leafNode = dict(boxstyle = "round4", fc = "0.8")
arrow_args = dict(arrowstyle = "<-")

def plotNode(nodeTxt, centerPt, parentPt, nodeType):
	createPlot.axl.annotate(nodeTxt, xy=parentPt, xycoords='axes fraction'
		,xytext=centerPt, textcoords='axes fraction',va="center", 
		ha="center", bbox=nodeType, arrowprops=arrow_args)

def createPlot():
	fig = plt.figure(1, facecolor='white')
	fig.clf()
	createPlot.axl = plt.subplot(111,frameon=False)
	plotNode('a decision node', (0.5,0.1), (0.1,0.5), decisionNode)
	plotNode('a leaf node', (0.8,0.1), (0.3,0.8), leafNode)
	plt.show()

def getNumLeafs(myTree):
	numLeafs = 0
	firstStr = myTree.keys()[0]
	secondDict = myTree[firstStr]
	for key in secondDict.keys():
		if type(secondDict[key]).__name__=='dict':
			numLeafs += getNumLeafs(secondDict[key])
		else: 
			numLeafs += 1
			#secondDict 存的是 no no  yes 也就是字典里的value
	return numLeafs
def getTreeDepth(myTree):
	maxDepth = 0
	firstStr = myTree.keys()[0]
	secondDict = myTree[firstStr]
	for key in secondDict.keys():
		if type(secondDict[key]).__name__=='dict':
			thisDepth = 1 + getTreeDepth(secondDict[key])
		else: thisDepth = 1
		if thisDepth > maxDepth:
			maxDepth=thisDepth

	return maxDepth


def retrieverTree(i):
	listOfTrees = [{'no surfacing':{0:'no',1:{'flippers':{0:'no',1:'yes'}}}}]
	return listOfTrees[i]

myTree = retrieverTree(0)
print getNumLeafs(myTree)
print getTreeDepth(myTree)