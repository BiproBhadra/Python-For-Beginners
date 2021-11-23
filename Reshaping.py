import numpy as np
arr=np.random.randint(1,100,12)
print("1D Array-",arr,"\n Number of Dimension:",arr.ndim)
arr1=arr.reshape(2,6)
print("1D Converted to 2D array-",arr1,"\n Number of Dimension:",arr1.ndim)
arr2=arr.reshape(12)
print("2D converted to 1D-",arr2,"\n Number of Dimension:",arr2.ndim)
