# Create an Employee type that contains information about employees
#  of a company. Each employee must have a name, job title,
#   and employment start date.

class Employee:

    def __init__(self, first_name, job_title, start_date):
        self.first_name = first_name
        self.job_title = job_title
        self.start_date = start_date
    

# Create a Company type that employees can work for. A company should
#  have a business name, address, and industry type.

class Company:

    def __init__(self, name, address, industry_type):
        self.business_name = name
        self.address = address
        self.industry_type = industry_type
        self.employees = list()
    
    def output_company(self):
        print(f'{self.business_name} is in the {self.industry_type} industry and has the following employees')

    def output_employees(self):
        for employee in self.employees:
            print(f'* {employee.first_name}')

# Create two companies, and 5 people who want to work for them.
NSS = Company("Nashville Software School", "301 Plus Park Blvd #300, Nashville, TN 37217", "Kick-ass coding school")
CQCC = Company("Castle's quarantined coding camp", "living room", "its ok, kinda lonely")

Castle1 = Employee("Castle1", "Lead Developer", "2/04/2020")
Castle2 = Employee("Castle2", "Lead Developer", "2/04/2020")
Castle3 = Employee("Castle3", "Lead Developer", "2/04/2020")
Castle4 = Employee("Castle4", "Lead Developer", "2/04/2020")
Castle5 = Employee("Castle5", "Lead Developer", "2/04/2020")




# Assign 2 people to be employees of the first company.
NSS.employees.append(Castle1)
NSS.employees.append(Castle2)
NSS.employees.append(Castle3)




# Assign 3 people to be employees of the second company.
CQCC.employees.append(Castle4)
CQCC.employees.append(Castle5)

# Output a report to the terminal the displays a business name, and its employees.
NSS.output_company()
NSS.output_employees()

CQCC.output_company()
CQCC.output_employees()



