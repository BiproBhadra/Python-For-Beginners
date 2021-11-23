students_DB={}
#ask input from user or "q" to exit
while True:
    line=input("Please input the ID and Name separated by comma or q to exit:")
    if line=="q":
        break;
    id,name=line.split(",")    
    students_DB.update({id:name})
#output
for x,y in students_DB.items():
    print(x,y)    
#Searching a key
key=input("Enter ID to search:")    
if key in students_DB:
    print("Key=",key,"Value=",students_DB[key])
else:
    print("Key not found!")  
