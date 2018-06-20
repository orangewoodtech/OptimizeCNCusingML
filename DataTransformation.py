# Load libraries
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.model_selection import cross_val_score
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import csv, math
import numpy as np
from statistics import *

url = 'C:\\Users\\Ankit Kumar\\Desktop\\LabelClean1800.csv'
names = ['Class', 'Dist', 'X', 'Y', 'Z', 'VibNorm']
dataset = pandas.read_csv(url, names=names)

array = dataset.values
Class=array[:,0]
Dist=array[:,1]
x=array[:,2]
y=array[:,3]
z=array[:,4]

# Z-constant
#ZscoreCons=3

ClassList=list(map(float, Class))

DistList=[]
DistList=list(map(float, Dist))

xList = list(map(float, x))
'''
meanX=mean(xList)
stdevX=stdev(xList)
print(meanX, stdevX)
Xnorm=[]
for i in xList:
    ZScoreval=abs(i-meanX)-ZscoreCons*stdevX
    if(ZScoreval<=stdevX):
        ZScoreval=0
    else:
        ZScoreval=ZScoreval*3
    Xnorm.append(ZScoreval)
'''

yList=list(map(float,y))
'''
meanY=mean(yList)
stdevY=stdev(yList)
#print(meanY, stdevY)
Ynorm=[]
for i in yList:
    ZScoreval=abs(i-meanY)-ZscoreCons*stdevY
    if(ZScoreval<=stdevY):
        ZScoreval=0
    else:
        ZScoreval=ZScoreval*3
    Ynorm.append(ZScoreval)
'''
# Znormalization List	
zList=list(map(float,z))
'''	
meanZ=mean(zList)
stdevZ=stdev(zList)
#print(meanZ, stdevZ)
Znorm=[]
for i in zList:
    ZScoreval=abs(i-meanZ)-ZscoreCons*stdevZ
    if(ZScoreval<=stdevZ):
        ZScoreval=0
    else:
        ZScoreval=ZScoreval*3
    Znorm.append(ZScoreval)
'''	
Vib=[]
count=0
for i,k in zip(xList,zList):
    val=i*i+k*k
    sqrtval=val**(1.0/2)
    Vib.append(round(sqrtval, 2))
	
currentD=round(abs(DistList[0]))
nextD=currentD

currentC=ClassList[0]
nextC=currentC

VibInterval=[]
xL=[]
yL=[]
zL=[]
count=0

L=len(ClassList)
print(L)

VeryCleanData=[]
row=[]


def label():
    global nextC, nextD, currentC, currentD, count
    if(nextC==currentC):
        while(nextC):
            while(nextD>=abs(round(currentD))-5 and count<L-1):
                xL.append(xList[count])
                zL.append(zList[count])
                count=count+1				
                nextD=abs(DistList[count])
                nextC=ClassList[count]
                #print(nextC, nextD, count)
            meanX=mean(xL)
            meanZ=mean(zL)
            #print(abs(round(currentD))-5, round(meanX, 2), round(meanZ, 2), Class[count])
            row.append(nextC)
            row.append(round(currentD)-5)
            row.append(round(meanX, 2))
            row.append(round(meanZ, 2))

            if(abs(round(currentD)-5)==0):
                break
            currentD=abs(round(currentD))-5
            xL.clear()
            zL.clear()
            nextC=ClassList[count-1]
        
label()

n=4
def chunks(row, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(row), n):
        # Create an index range for l of n items:
        yield row[i:i+n]
#print(VeryCleanData)
VeryCleanData=[]
VeryCleanData=list(chunks(row, n))
print(list(chunks(row, n)))
myFile = open('TestML1800.csv', 'w')
with myFile:
    writer = csv.writer(myFile, delimiter=",")
    writer.writerows(VeryCleanData)
