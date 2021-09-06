import csv 
from collections import Counter
with open("a.csv",newline="") as f:
    reader=csv.reader(f)
    filedata=list(reader)
newdata="whitehatjr"
data=Counter(newdata)
print(data)
newlist=data.items()
print(newlist)
value=data.values()
print(value)
