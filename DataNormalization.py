# Load libraries
import pandas
from pandas.plotting import scatter_matrix
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

# Z-Score Constant
ZscoreCons=1

# Transforming Vibrations in x, z to VibNorm
VibNorm=[]
count=0
for i,k in zip(xList1,zList1):
    val=i*i+k*k
    sqrtval=val**(1.0/2)
    if(sqrtval==0):
        count=count+1
    VibNorm.append(sqrtval)

# Thresholding
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

# FInal Normalized Data Formation
FinalData=[]

for i in range(0, len(ClassList1)):
    FinalData.append(ClassList1[i])
    FinalData.append(DistList1[i])
    FinalData.append(Vib[i])

# Creating Chunks of List
n=3
def chunks(FinalData, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(FinalData), n):
        # Create an index range for l of n items:
        yield FinalData[i:i+n]

SuperCleanData=[]
SuperCleanData=list(chunks(FinalData, n))

# Writing into file
myFile = open('TestML2_1500.csv', 'w')
with myFile:
    writer = csv.writer(myFile, delimiter=",")
    writer.writerows(SuperCleanData)
    
