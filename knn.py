from numpy import *
import operator
def classify0(inX,dataSet,labels,k):
	dataSetSize=dataSet.shape[0]
	dataDiff=tile(inX,(dataSetSize,1))-dataSet
	dataDiff2=dataDiff**2	
	datadiff=dataDiff2.sum(axis=1)
	dataDifff=datadiff**0.5
	sortedDistIndex=dataDifff.argsort()
	classCount={}
	for i in range(k):
		label=labels[sortedDistIndex[i]]
		classCount[label]=classCount.get(label,0)+1
	sortedCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
	return sortedCount[0][0]

def file2mat(filename):
	fr=open(filename)
	contentline=fr.readlines()
	m=len(contentline)
	returnmat=zeros((m,3))
	returnlab=[]
	n=0
	for i in contentline:
		i=i.strip()
		icache=i.split('\t')
		returnmat[n,:]=icache[:3]
		returnlab.append(int(icache[-1]))
		n+=1
	return returnmat,returnlab

def autonorm(dataset):
	minva=dataset.min(0)
	maxva=dataset.max(0)
	rangex=maxva-minva
	normdata=zeros(shape(dataset))
	m=dataset.shape[0]
	normdata=dataset-tile(minva,(m,1))
	normdata=normdata/tile(rangex,(m,1))
	return normdata,rangex,minva

def datingclasstest():
	rate=0.1
	dataset,datalab=file2mat('datingTestSet2.txt')
	normmat,ranges,minva=autonorm(dataset)
	m=normmat.shape[0]
	n=int(m*rate)
	errorcount=0
	for i in range(n):
		classifyresult=classify0(normmat[i,:],normmat[n:m,:],datalab[n:m],3)
		print('the predicting value is %d,the real answer is %d' % (classifyresult,datalab[i]))
		if classifyresult != datalab[i]: errorcount += 1
	print('errorcount=%d,m=%s,n=%d' % (errorcount,m,n))
	x=errorcount/float(n)
	print ('the total error rate is : %f' % x)

def img2vec(filename):
	returnve = zeros((1,1024))
	fr = open(filename)
	for i in range(32):
		linestr=fr.readline()
		for j in range(32):
			returnve[0,32*i+j] = int(linestr[j])
	return returnve

from os import listdir

def hwct():
	hwlabels=[]
	flist=listdir('trainingDigits')
	m = len(flist)
	trainingdata = zeros((m,1024))
	for i in range(m):
		fnstr=flist[i]
		trainingdata[i,:] = img2vec('trainingDigits/%s' % fnstr)
		hwlabels.append(int(fnstr.split('_')[0]))
	testlist=listdir('testDigits')
	errorcount=0
	n=len(testlist)
	for j in range(n):
		tnstr=testlist[j]
		ut=img2vec('testDigits/%s' % tnstr)
		reallabel=int(tnstr.split('_')[0])
		result=classify0(ut,trainingdata,hwlabels,3)
		if result != reallabel: errorcount += 1
		print('the predicting result is %d ,the real answer is %d' % (result,reallabel))
	print('errorcount=%d' % errorcount)
	print('rate is %f' % (errorcount/float(n)))

	
