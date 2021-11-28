Write statement to import numpy?
ans: import numpy as np
  
Create an Array using numpy?
ans: import numpy as np
     arr=np.array([1,2,3,4,5])
    
Create an Array of random 10 integers?
ans:  import numpy as np
      arr=np.random.randint(1,50,10)
      arr

Create an array of elements from 10-20?
ans:  import numpy as np
      arr=np.arange(10,21)
      arr
      
Create an array which contains value 5,10 times?
ans:  import numpy as np
      arr=np.ones(10)*5
      arr
      
Create a one dimensional array and convert that into 3*3 matrix?
ans:   import numpy as np
       arr=np.arange(1,10).reshape(3,3)
       arr
      
Create an array and then convert all the even numbers with 0?
ans:   import numpy as np
       arr=np.arange(1,11)
       arr[arr%2==0]=0
       arr
        
Create a 2D array of size 3*3 but all the elements should be between 0 and 1?
ans:   import numpy as np
       arr=np.random.rand(9).reshape(3,3)
       arr
      
Perform the following slicing?
Input:
  1 2  3  4 
  5 6  7  8
  9 10 11 12
  13 14 15 16
Output:
  6  7 
  10 11
  14 15
  
ans: import numpy as np
     arr1=np.arange(1,17).reshape(4,4)
     arr2=arr1[1,;1:3]
     arr2
   
Concatenate 2D array horizontally and vertically?
ans:  import numpy as  np
      arr1=np.arange(1,10).reshape(3,3)
      arr2=np.arange(10,19).reshape(3,3)
      np.hstack((arr1,arr2))
      
      import numpy as  np
      arr1=np.arange(1,10).reshape(3,3)
      arr2=np.arange(10,19).reshape(3,3)
      np.vstack((arr1,arr2))
      
      
  
  
  
    
    
