import numpy as np
a=[]
size=int(input("State the Size of list for converting it into array:"))
for i in range(size):
    val=int(input("Enter Number:"))
    a.append(val)
print("Our List is=",a)    
arr=np.array(a)
for i in range(arr.size):
    print(arr[i])
sum=0
for i in range(arr.size):
    sum=sum+arr[i]
print("Sum of array elements=",sum) 
