# -*- coding: UTF-8 -*- 
import matplotlib.pyplot as plt
#decide style of arrow

decinode={'boxstyle':'sawtooth','fc':'0.8'}
leafnode={'boxstyle':'round4','fc':'0.8'}
arrow_args={'arrowstyle':'<-'}

#the function of plot nodes
def plotnode(nodetxt,centerpt,parentpt,nodetype):
	creatplot.ax1.annotate(nodetxt,xy=parentpt,xycoords='axes fraction',
	xytext=centerpt,textcoords='axes fraction',va='center',ha='center',bbox=nodetype,
	arrowprops=arrow_args)

#the function of creat a graph
def creatplot(tree):
	fig=plt.figure(1,facecolor='white')
	fig.clf()
	axprops=dict(xticks=[0,10],yticks=[20,30])
	creatplot.ax1=plt.subplot(111,frameon=False)
	plottree.w=float(gnol(tree))
	plottree.d=float(gdot(tree))
	plottree.xoff=-0.5/plottree.w
	plottree.yoff=1.0
	plottree(tree,(0.5,1.0))
	plt.show()

#
def gnol(tree):
	leafnum=0
	fisrtkey=tree.keys()[0]
	postdic=tree[fisrtkey]
	for i in postdic.keys():
		if isinstance(postdic[i],dict):
			leafnum += gnol(postdic[i])
		else:
			leafnum += 1
	return leafnum
def gdot(tree):
	deepth=0
	firstkey=tree.keys()[0]
	postdic=tree[firstkey]
	for i in postdic.keys():
		if isinstance(postdic[i],dict):
			nwdpth = 1+gdot(postdic[i])
		else:
			nwdpth = 1
		if nwdpth>deepth:deepth=nwdpth
	return deepth
def crtree():
	return {'no surfacing':{0:'no',1:{'flippers':{0:'no',1:'yes'}}}}

def plotmidtext(cntrpt,parentpt,txt):
	x=(parentpt[0]-cntrpt[0])/2.0+cntrpt[0]
	y=(parentpt[1]-cntrpt[1])/2.0+cntrpt[1]
	creatplot.ax1.text(x,y,txt)

def plottree(tree,parentpt,txt=''):
	nol=gnol(tree)
	dot=gdot(tree)
	firststr=tree.keys()[0]
	cntrpt=(plottree.xoff+(1.0+float(nol))/2.0/plottree.w,plottree.yoff)
	plotmidtext(cntrpt,parentpt,txt)
	plotnode(firststr,cntrpt,parentpt,decinode)
	nextdict=tree[firststr]
	plottree.yoff -= 1.0/plottree.d
	for key in nextdict.keys():
		if isinstance(nextdict[key],dict):
			plottree(nextdict[key],cntrpt,str(key))
		else:
			plottree.xoff += 1.0/plottree.w
			plotnode(nextdict[key],(plottree.xoff,plottree.yoff),cntrpt,leafnode)
			plotmidtext((plottree.xoff,plottree.yoff),cntrpt,str(key))
	plottree.yoff += 1.0/plottree.d
	

