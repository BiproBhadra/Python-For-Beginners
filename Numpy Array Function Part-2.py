import numpy as np
np.random.seed(12)
matrix=np.random.randint(1,21,10)
print(matrix)
np.random.shuffle(matrix)
print(matrix)
arr=np.array([10,20,30,40,50,10,20,50])
print(np.unique(arr))
print(np.unique(arr).size)
b=np.unique(arr,return_index=True,return_counts=True)
print(b)
