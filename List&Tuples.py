name=[]
mark=[]
count=0
Name=[]
n=int(input("Enter How many records you want to add :"))
for i in range(1,n+1):
    a=input("Enter Your Name :")
    b=int(input("Enter Your Mark :"))
    name.append(a)
    mark.append(b)
for j in range(1,n+1):
    print(f"{j-1}.{name[j-1]} : {mark[j-1]}")
n=mark.index(max(mark))
print(f"Highest Mark ={name[n]}:{max(mark)}")
o=mark.index(min(mark))
print(f"Lowest Mark={name[o]}:{min(mark)}")
p=sum(mark)/len(mark)
print(f"Average Mark={p}")
for i in mark:
    if i>=35:
        count+=1
print(count,"Students are passed.")
for i in name:
    n=i.upper()
    Name.append(n)
print("Students name in upper case :")
i=1
for j in Name:
    print(f"{i}.{Name[i-1]}")
    i+=1