%%timeit
a=[]
for i in range(1,15):
    a.append(i*10)
    

import numpy as np
%timeit np.arange(1,11)**2


%timeit [i**2 for i in range(1,11)]

#Numpy will be taking much lesser time than the list as from the above code it is clearly visible.


#Size-Numpy data structures takes up less space
#Performance-thay have a need for speed and a faster than list 
#Functionality-SciPy and NumPy have optimised functions such as linear algebra operations built in
    
