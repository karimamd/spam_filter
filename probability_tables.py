from spam import *
from hham import *
from eham import *
count=0
print (eham.__len__())
for i in eham:
    if len(i[0]) >8:
        eham.remove(i)
        count+=1
print (eham.__len__())
print (count)

