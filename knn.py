from numpy import *
def classify0(inX,dataSet,labels,k):
	dataSetSize=dataSet.shape[0]
	dataDiff=tile(inX,(dataSetSize,1))-dataSet
	dataDiff2=dataDiff**2	
	datadiff=dataDiff2.sum(axis=1)
	dataDifff=datadiff**0.5
	sortedDistIndex=dataDifff.argsort()
	classCount={}
	for i in k:
		label=labels[sortedDistIndex[i]]
		classCount[label]=classCount.get(label,0)+1
	sortedCount=sorted(classCount.iteritems(),key=itemgetter(1),reverse=True)
	return sortedCount[0][0]
