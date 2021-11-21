a=[]
size=int(input("Enter the list Size upto which you want the Odd/Even: "))
for i in range(size):
      val=int(input("Enter the number: ")) 
      a.append(val)
print("Our List is: ",a)
even=0
odd=0
for i in range(size):
    if(a[i]%2==0):
        even=even+1
    else:
        odd=odd+1
print("Total Even:",even,"Total Odd:",odd)            
