#View

import numpy as np
a=np.array([10,20,30,40,50,60,70,80,90])
b=a[3:6]            #As a view we are getting all the elements here that's why any change will reflect in the array.
b[:]=0
print(b)
print(a)

#Copy

import numpy as np
a=np.array([10,20,30,40,50,60,70,80,90])
b=a[3:6].copy()     #For using copy in slicing any changes won't reflect in the original array.        
b[:]=0
print(b)
print(a)
