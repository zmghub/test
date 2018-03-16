from numpy import *
from math import log
import operator as op
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
	m=0
	for i in dataset:
		if i[feature]==value:
			returnset.append(i[:feature])
			returnset[m].extend(i[feature+1:])
			m += 1
	return returnset

def choFea(dataset):
	numfea=len(dataset[0])-1
	selfea=-1
	bestinfogain=0
	baseent=clcShEnt(dataset)
	for i in range(numfea):
		fealist=set([j[i] for j in dataset])
		newent=0
		for m in fealist:
			subdataset=dataSpl(dataset,i,m)
			pro=len(subdataset)/float(len(dataset))
			newent += pro*clcShEnt(subdataset)
		infogain=baseent-newent
		if infogain>bestinfogain:
			bestinfogain=infogain
			selfea=i
	return selfea

def classchoose(classnum):
	classcount={}
	for i in classnum:
		if i not in classcount.keys(): classcount[i]=0
		classcount[i] += 1
	sortedclasscount = sorted(classcount.iteritems(),key=op.itemgetter(1),reverse=1)
	return sortedclasscount[0][0]

def creattree(dataset,labels):
	classlist=[i[-1] for i in dataset]
	if classlist.count(classlist[0])==len(classlist):
		return classlist[0]
	elif len(dataset)==1:
		return classchoose(classlist)
	bestfeature=choFea(dataset)
	print(labels)
	bestfealab=labels[bestfeature]
	tree={bestfealab:{}}
	del(labels[bestfeature])
	feavalue=set([i[bestfeature] for i in dataset])
	for m in feavalue:
		sublabel=labels[:]
		tree[bestfealab][m]=creattree(dataSpl(dataset,bestfeature,m),sublabel)
	return tree


		
def classify(intree,labels,instance):
	fstr=intree.keys()[0]
	index=labels.index(fstr)
	nextdict=intree[fstr]
	feat=instance[index]
	for key in nextdict.keys():
		if key==feat:
			if isinstance(nextdict[key],dict):
				classresult=classify(nextdict[key],labels,instance)
			else: classresult=nextdict[key]
	return classresult

def stotree(intree,filename):
	import pickle
	fw=open(filename,'w')
	pickle.dump(intree,fw)
	fw.close()
def gettree(filename):
	import pickle
	fr=open(filename,'r')
	return pickle.load(fr)



