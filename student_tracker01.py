import json
import os
student={}
if not os.path.exists("student.json"):
    with open ("student.json","w")as f:
        json.dump(student,f)
def user():
    with open("student.json","r")as f:
        data=json.load(f)
    while True:
        login=input('''
                    1.New User
                    2.I Have Account
                    
                    Select Your option :''')
        if login=='1' :
            name=input("Enter Your Name :")
            id=int(input("Enter Your id :"))
            new_key="stud"+str(id)
            if new_key in data:
                print("Already ,You Have account")
                continue
            dept=input("Enter Your Department :")
            year=int(input("Enter Your year of study :"))
            print("Welcome",name,"!")
            Task=dict({})
            student[new_key]={  
                "name":name,
                "id":id,
                "dept":dept,
                "year":year,
                "task":Task,
                "completed":[]
            }
            data.update(student)
            with open("student.json","w")as f:
                json.dump(data,f,indent=4)
        elif login=="2":
            with open("student.json","r")as f:
                data=json.load(f)
            id=int(input("Enter Your id :"))
            new_key="stud"+str(id)
            if new_key in data:
                print(data)
                #return(data[new_key])
            else:
                print("Invalid User")
                continue
        menu()
def menu():
    while True:
        print("----------MENU----------\n")
        print('''    
            1.Add Task 
            2.View Task
            3.Mark Tasks Completed
            4.Search Tasks
            5.Categorize Task
            6.Completed Task
            7.Exit
            ''')        
        choice=int(input("Enter Your Choice :"))
        new_key="stud"+str(id)
        match choice:
            case 1:
                with open("student.json","r")as f:
                    data=json.load(f)
                n=int(input("Enter How many task You want to add :"))
                for i in range(1,n+1):
                    cat=input("Enter the category :")
                    task=[]
                    task=str(input("Enter Your Task :"))
                    Task={cat:task}
                    key=list(data.keys())
                    for new_key in key:                 
                        data[new_key]["task"].update(Task)
                    with open("student.json","w")as file:
                        json.dump(data,file,indent=4)
                        print("Task Added!")
                        continue
            case 2:
                with open("student.json","r")as f:
                    data=json.load(f)
                key=(data.keys())
                for new_key in key:
                    y=data[new_key]["task"].values()
                    z=list(y)
                    j=1
                    for i in z:
                        print(f"{j}.{i}")
                        j+=1
            case 3:
                with open("student.json","r")as f:
                    data=json.load(f)
                key=data.keys()
                for new_key in key:
                    y=data[new_key]["task"]
                    j=1
                    for i in y:
                        print(f"{j}.{y[i]}")
                        j+=1
                n=input("Enter the task which is you completed : ")
                for new_key in key:
                    y=data[new_key]["task"]
                    for i in y:
                        if y[i] ==n:
                            data[new_key]["completed"].append(n)
                            data[new_key]["task"].pop(i)
                            print("task",n,"is completed")
                            break
                with open("student.json","w")as f:
                    json.dump(data,f,indent=4)
            case 4:
                with open("student.json","r")as f:
                   data=json.load(f)
                n=input("search your task :")
                for new_key in key:
                    y=data[new_key]["task"]
                    for i in y:
                        if y[i] ==n:
                            print("Task is Found,You still not finished the Task:",n)
                        else:
                            for j in data[new_key]["completed"]:
                                if j==n:
                                    print("You finished the Task")
                                else:
                                    print("Task is not found")
            case 5:
                with open("student.json","r")as f:
                    data=json.load(f)
                key=data.keys()
                for new_key in key:
                    y=data[new_key]["task"]
                    j=1
                    for i in y:
                        print(f"{j}.{i}:{y[i]}")
                        j+=1
            case 6:
                with open("student.json","r") as f:
                    data=json.load(f)
                key=data.keys()
                j=1
                for new_key in key:
                    y=data[new_key]["completed"]
                    for i in y:
                        print(f"{j}.{i}")
            case 7:
                break   
user()