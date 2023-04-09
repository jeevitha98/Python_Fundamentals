n=int(input('enter the number of employees'))
employees={}
for i in range(n):
    name=input('enter employee name')
    salary=input('enter employee salary')
    employees[name]=salary

print('Know salary details of any employee')
while True:
    name=input('enter emp name')
    salary=employees.get(name, -1)
    if salary == -1:
        print('employees does not exist')
    else:
        print('the salary of the employee is',salary)
    
    choice=input('do you want to know the salary of another employee[Yes|No]')
    if choice=='No':
        break
