t1=(1,2,3,4,5)
list1=list(t1)
for i in range(len(list1)):
    d=int(input('Enter elements:'))
    list1.append(d)
t1=tuple(list1)
print(t1)
