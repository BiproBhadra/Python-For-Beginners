a=[]
size=int(input("Enter the list Size: "))
for i in range(size):
      val=int(input("Enter the number: ")) 
      a.append(val)
print("Our List is: ",a)
max=a[0]
for i in range(size):
    if(a[i]>max):
        max=a[i]
min=a[0]
for i in range(size):
    if(a[i]<min):
        min=a[i]      
print("Maximum & Minimum Number:",max,"&",min)
