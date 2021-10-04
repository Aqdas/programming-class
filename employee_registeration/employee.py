class Employee:
    arbisoft_employees = []

    def __init__(self):

        self.department = None
        self.experience = None
        self.name = None
        self.employee_id = None

    def register_employee(self):
        self.name = input('Please enter your name: ')
        self.employee_id = input('Please enter your employee ID: ')
        self.experience = int(input('Please enter your years of Experience: '))
        self.department = input('Enter relevant department: ')
        self._add_employee()

    def _add_employee(self):
        employee_record = {
            'name': self.name,
            'experience': self.experience,
            'employee_id': self.employee_id,
            'department': self.department,
            'designation': self.get_designation(self.experience),
        }
        Employee.arbisoft_employees.append(employee_record)

    def get_designation(self, experience):
        if experience < 3:
            designation = 'Software Engineer'
        elif 3 <= experience < 6:
            designation = 'Senior Software Engineer'
        else:
            designation = 'Principal Software Engineer'

        return designation

    @staticmethod
    def print_employee_detail():
        for employee in Employee.arbisoft_employees:
            print(f"\n{employee['name']}\n{employee['designation']}\n{employee['department']}")
            print('------------------------------------------------------------------------')


register_another_emp = True

while register_another_emp:
    employee = Employee()
    employee.register_employee()
    register = input('Do you want to register more? (y/n) ')
    if register in ['n', 'N']:
        register_another_emp = False

Employee.print_employee_detail()
