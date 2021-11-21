# Using in built function max & min

a=[]
size=int(input("Enter the size of list:"))
for i in range(size):
    val=int(input("Enter the number: "))
    a.append(val)
print("Our list is ",a)
minval=min(a)
print("Min value in the list is:",minval)
a.remove(minval)
secmin=min(a)
print("Second min value in the list is:",secmin)

# Alternative method by using sorting concept

a=[]
size=int(input("Enter the size of list:"))
for i in range(size):
    val=int(input("Enter the number: "))
    a.append(val)
print("Our list is ",a)
a.sort()
print("Min value=",a[0])
print("Second min value=",a[1])
