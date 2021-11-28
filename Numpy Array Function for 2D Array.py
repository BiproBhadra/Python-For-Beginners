import numpy as np
np.random.seed(12)
matrix=np.random.randint(1,21,9).reshape(3,3)
print(matrix)
print(np.sum(matrix))
print(np.min(matrix))
print(np.max(matrix))
print(np.min(matrix,axis=1))     #Finds row wise min
print(np.max(matrix,axis=0))     #Finds col wise max
print(np.sum(matrix,axis=1))     #Finds row wise sum
print(np.cumsum(matrix))         #Cumulative Sum
print(np.cumsum(matrix,axis=1))
