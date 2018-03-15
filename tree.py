from numpy import *
from math import log
def clcShEnt(dataset):
	nofd=len(dataset)
	classnum={}
	for i in dataset:
		if i[-1] not in classnum.keys():
			classnum[i[-1]]=0
		classnum[i[-1]] += 1
	ent=0
	for key in classnum:
		prob=float(classnum[key])/nofd
		ent -= prob*log(prob,2)
	return ent 

def dataSpl(dataset,feature,value):
	returnset=[]
	for i in dataset:
		if i[feature]==value:
			returnset.extend(i[:feature])
			returnset.extend(i[feature+1:])
	return returnset

def choFea(dataset):
	numfea=len(dataset[0])-1
	selfea=-1
	bestinfogain=0
	baseent=clcShEnt(dataset)
	for i in numfea:
		fealist=set([j[i] for j in dataset])
		newent=0
		for m in fealist:
			subdataset=dataSpl(dataset,i,m)
			pro=len(subdataset)/float(len(dataset))
			newent += pro*clcShEnt(subdataset)
		infogain=baseent-newent
		if infogain>bentinfogain:
			bestinfogain=infogain
			selfea=i
	return selfea


