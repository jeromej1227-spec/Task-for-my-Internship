def avarage(mark):
    return sum(mark)/len(mark)
def highest(mark):
    return mark.index(max(mark))
def lowest(mark):
    return mark.index(min(mark))
def grade(mark):
    grade=[]
    for i in mark:
        if i>80 and i<100:
            grade.append("Grade A")
        elif i>60 and i<=80:
            grade.append("Grade B")
        elif i>=35 and i<=60:
            grade.append("Grade C")
        else:
            grade.append("Fail")
    return grade
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
print("Average Mark=",avarage(mark))
n=highest(mark)
print(f"Highest Mark={name[n]}:{mark[n]}")
o=lowest(mark)
print(f"Lowest Mark={name[o]}:{mark[o]}")
n=grade(mark)
for i in range(len(n)):
    print(f"{i+1}.{name[i]} : {n[i]}")

    