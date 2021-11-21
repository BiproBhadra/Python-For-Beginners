a=[]
size=int(input("Enter the list Size upto which you want the Sum: "))
for i in range(size):
      val=int(input("Enter the number: ")) 
      a.append(val)
print("Our List is: ",a)      
sum=0
for i in range(size):
      sum=sum+a[i]
print("Sum of List Element=",sum) 
