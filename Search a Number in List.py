a=[]
size=int(input("Enter the list Size: "))
for i in range(size):
      val=int(input("Enter the number: ")) 
      a.append(val)
print("Our List is: ",a)
key=int(input("Enter the number to Search: "))
flag=0
for i in range(size):
      if(a[i]==key):
          flag=1
          index=i
          pos=i+1
          break
if(flag==1):
    print("Element found at",pos,"position & at index",index)        
else:
    print("Element not found")    
