class Employers:
    def __init__(self, name, gender, idNo, role, salary):
        self.employeeName = name
        self.employeeGender = gender
        self.employeeIdNo = idNo
        self.employeeSalary = salary
        self.employeeRole = role

    def get_name_role(self):
        basic_info = f"{self.employeeName} is our {self.EmployeeRole}"
        return basic_info

    def salary_ranking(self):
        if self.employeeSalary > 200000:
            print(f"{self.employeeName} earns a salary of ksh {self.employeeSalary} and belongs to job group A")
        elif self.employeeSalary > 150000:
            print(f"{self.employeeName} earns a salary of ksh {self.employeeSalary} and belongs to job group B")
        elif self.employeeSalary > 100000:
            print(f"{self.employeeName} earns a salary of ksh {self.employeeSalary} and belongs to job group C")
        elif self.employeeSalary > 50000:
            print(f"{self.employeeName} earns a salary of ksh {self.employeeSalary} and belongs to job group D")
        else:
            print(f"{self.employeeName} earns a salary of ksh {self.employeeSalary} and belongs to job group  E")


emp1 = Employers("JeffDeActivist", "male", 12345678, "Junior DBA", 100000)  # emp1 for employer 1
print(emp1.employeeSalary)  # to view salary of emp1
print(emp1.get_name_role())  # calling the method get_name_role
print(emp1.salary_ranking())  # calling the method salary_ranking
"""demonstrating inheritance"""


# we are overriding class Employers by creating new objects in class SeniorWorkers
class SeniorWorkers(Employers):  # SeniorWorkers have inherited attributes and methods from class employers
    def __init__(self, name, gender, idNo, role, salary, seniorRole):
        super().__init__(name, gender, idNo, role, salary)
        self.SeniorWorkers = seniorRole

    def senior_roles(self):  # extend
        print(f"{self.employeeName} is a {self} also a {self.SeniorWorkers}")


snr1 = SeniorWorkers("Jeff Angayo", "male", 12346, "Senior DBA", 1000000, "CEO")  # senior worker 1
print(snr1.salary_ranking())  # a method inherited from class employees
print(snr1.senior_roles())  # calling the method senior_roles
