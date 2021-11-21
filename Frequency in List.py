a=[]
size=int(input("Enter the list Size: "))
for i in range(size):
      val=int(input("Enter the number: ")) 
      a.append(val)
print("Our List is: ",a)
key=int(input("Enter the number to find Frequency: "))
count=0
for i in range(size):
      if(a[i]==key):
          count=count+1
print("Frequency=",count)       
