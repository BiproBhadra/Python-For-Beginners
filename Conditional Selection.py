import numpy as np
a=np.arange(1,16)
print(a)
print(a>10)
print("Even numbers are:",a[a%2==0])
print("Odd numbers are:",a[a%2!=0])
a[a>10]=0
print("Replicate all numbers by zero which are greater than 10 are:",a)
