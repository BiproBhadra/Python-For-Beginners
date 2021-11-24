a=[]
size=int(input("Enter the size of list:"))
for i in range(size):
    val=int(input("Enter the number: "))
    a.append(val)
print("Our list is ",a)    
i=0
j=size-1
while(i<j):
    t=a[i]
    a[i]=a[j]
    a[j]=t
    i=i+1
    j=j-1
print("List after reverse is",a)  
