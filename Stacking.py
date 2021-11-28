import numpy as np
a=np.array([1,2,3,4])
b=np.array([5,6,7,8])
print("Horizontal stacking:",np.hstack((a,b)))    #It will Horizontaly arrange the matrix
print("Vertical stacking:\n",np.vstack((a,b)))    #It will Vertically arrange the matrix

--------------------------------------------------------------------------------------------
import numpy as np
np.random.seed(122)
arr1=np.random.randint(1,21,9).reshape(3,3)
arr2=np.random.randint(50,71,9).reshape(3,3)
print("Array 1:\n",arr1)
print()
print("Array 2:\n",arr2)
print()
print("Horizontal Stacking:\n",np.hstack((arr1,arr2)))
print()
print("Vertical Stacking:\n",np.vstack((arr1,arr2)))

----------------------------------------------------------------------------------------------

# "--" Used for separating the two codes and its not included in the program.
