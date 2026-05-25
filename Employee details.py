employee=[]
n=input("Enter 'add' to add details or enter anything to finish :")
while n=='add' or n=='Add' :
    id=int(input("Enter Employee id:"))
    Name=input("Enter Employee Name :")
    salary= float(input("Enter Your Salary:"))
    task=int(input("Enter No of Completed Out of 10:"))
    n=input("Enter 'add' to add details or enter anything to finish :")
    if task >=8 and task<=10:
        bonus=0.20
        Bonus=salary*bonus
        total_salary=salary+Bonus
    elif task >=6 and task<8:
        bonus=0.15
        Bonus=salary*bonus
        total_salary=salary+Bonus
    elif task >=4 and task<6:
        bonus=0.10
        Bonus=salary*bonus
        total_salary=salary+Bonus
    else:
        Bonus=0
        total_salary=salary+Bonus
    employee_detail=[id,Name,task,Bonus,total_salary]
    employee.append(employee_detail)
for j in employee:
    print("Employee id:",j[0])
    print("Employee Name:",j[1])
    print("Task Complted :",j[2])
    print("Bonus :",j[3])
    print("Total Salary",j[4])
    print("/n")