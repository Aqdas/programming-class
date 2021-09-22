'''Write a program for employee registration. To register one employee, program should ask his/her year of experience,
name and employee ID, after every registration, program should ask, do you want to register more? (y/n).
If user enter 'y' program should register one more employee similarly you did it before if user enters 'n' then
program should stop registration process and show the results according to the following requirements:
All the register employees data should be save in the collection/list
Individual employee's record should be save in Dictionary
Iterate through the list in which you have saved registered employees
Show name of all registered employees along with their designations based on Arbisoft's criteria
Means if user has less than 3 years experience he/she will be Software Engineer
If experience is 3 or more than 3 he/she will Senior Software Engineer
If experience is 6 or less then he/she will Principle Software Engineer
expected Output: If you registered four employees
Zubair Shakoor
Senior Software Engineer
------------------------------------------------------------------------
Salman Ahmad
Senior Software Engineer
------------------------------------------------------------------------
Aqdus Rehman
Principle Software Engineer
------------------------------------------------------------------------
Anonymous
Software Engineer'''

arbisoft_employees = []
register_another_emp = True

while register_another_emp:
    name = input('Please enter your name: ')
    employee_id = input('Please enter your employee ID: ')
    experience = int(input('Please enter your years of Experience: '))
    employee_record = {
        'name': name,
        'experience': experience,
        'employee_id': employee_id
    }

    arbisoft_employees.append(employee_record)

    register = input('Do you want to register more? (y/n) ')
    if register in ['n', 'N']:
        register_another_emp = False


for employee in arbisoft_employees:
    designation = None
    if employee['experience'] < 3:
        designation = 'Software Engineer'
    elif 3 <= employee['experience'] < 6:
        designation = 'Senior Software Engineer'
    else:
        designation = 'Principal Software Engineer'

    print(f"{employee['name']}\n{designation}")
    print('------------------------------------------------------------------------')
