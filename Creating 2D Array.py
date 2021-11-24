import numpy as np
matrix=[]
row=int(input("Enter the Number of Rows:"))
column=int(input("Enter the Number of Columns:"))
for i in range(row):
    a=[]
    for j in range(column):
        val=int(input("Enter the number:"))
        a.append(val)
    matrix.append(a)
arr=np.array(matrix) 
for i in range(row):
    for j in range(column):
        print(arr[i][j],end="  ")
    print()
print(type(arr))          #Multidimensional Array
