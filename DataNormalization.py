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

url = 'C:\\Users\\Ankit Kumar\\Desktop\\TestML1500.csv'
names = ['Class', 'Dist', 'X', 'Z']
dataset = pandas.read_csv(url, names=names)

array = dataset.values
Class1=array[:,0]
Dist1=array[:,1]
x1=array[:,2]
z1=array[:,3]

ClassList1=list(map(float, Class1))
DistList1=list(map(float, Dist1))
xList1=list(map(float, x1))
zList1=list(map(float, z1))



ZscoreCons=1

#print(ClassList1)

VibNorm=[]
count=0
for i,k in zip(xList1,zList1):
    #print('{} {} {}'.format(i,j,k))
    val=i*i+k*k
    sqrtval=val**(1.0/2)
    if(sqrtval==0):
        count=count+1
    VibNorm.append(sqrtval)

# Normalized Vibration List
Vib=[]
meanVib=mean(VibNorm)
stdevVib=stdev(VibNorm)
print(meanVib, stdevVib)
for i in VibNorm:
    ZScoreval=abs(i-meanVib)-ZscoreCons*stdevVib
    if(ZScoreval<=stdevVib):
        ZScoreval=0
    else:
        ZScoreval=ZScoreval*3
    Vib.append(ZScoreval)
#print(Vib)
FinalData=[]

for i in range(0, len(ClassList1)):
    FinalData.append(ClassList1[i])
    FinalData.append(DistList1[i])
    FinalData.append(Vib[i])
print(FinalData)

n=3
def chunks(FinalData, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(FinalData), n):
        # Create an index range for l of n items:
        yield FinalData[i:i+n]

SuperCleanData=[]
SuperCleanData=list(chunks(FinalData, n))
#print(list(chunks(row, n)))
myFile = open('TestML2_1500.csv', 'w')
with myFile:
    writer = csv.writer(myFile, delimiter=",")
    writer.writerows(SuperCleanData)