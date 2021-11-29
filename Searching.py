#we can search a value in an array and if the value is found the concerned index is returned for this we use where()method. 

import numpy as np
arr=np.array([1,5,7,23,45,67,23])
x=np.where(arr==23)
print("Value 23 is present at the index:",x)


#We can also use conditional based searching in where() function. 

import numpy as np
arr=np.array([1,5,8,23,45,67,23,86,90])
result=np.where(arr%2==0)
result


#Searchsorted this method performs a binary search in the array and returns the index where the specified value would be inserted to maintain the search order.
#This sorting work from left to right.

import numpy as np
a=np.array([1,5,7,23,45,67])
pos=np.searchsorted(a,19)
print(pos)


#For searching from right to left.

import numpy as np
a=np.array([1,5,7,23,45,67])
pos=np.searchsorted(a,19,side="right")
print(pos)

