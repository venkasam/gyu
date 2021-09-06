from typing import ClassVar
from collections import Counter

import csv
with open("a.csv",newline="") as f:
    reader=csv.reader(f)
    filedata=list(reader)

filedata.pop(0)
newdata=[]
for i in range(len(filedata)):
    num=filedata[i][1]
    newdata.append(float(num))

#getting the mean
n=len(newdata)
newdata.sort()
total=0
for x in newdata:
    total=total+x

mean=total/n

print("mean is:"+str(mean)) 
#getting the median
if (n%2==0) :
    median1=float(newdata[n//2])
    median2=float(newdata[n//2-1])
    med=(median1+ median2)/2
else :
    med=newdata[n//2]
    print(n)

print("median is"+str(med))
#get mode
data=Counter(newdata)
moderange={
    "50-60":0,
    "60-70":0,
    "70-80":0
}
for hei,occ in data.items():
    if(50<float(hei)<60):
        moderange["50-60"]+=occ
    elif (60<float(hei)<70):
        moderange["60-70"]+=occ
    elif (70<float(hei)<80):
        moderange["70-80"]+=occ

mode_range,mode_occ=0,0
for range,occ in moderange.items():
    if (occ>mode_occ):
        mode_range,mode_occ=[int(range.split("-")[0]),int(range.split("-")[1])],occ

mode=float((mode_range[0]+mode_range[1])/2)
print(f"mode->{mode:2f}")

