# We have multiple classes than inherit from the same interface or parent class
# one of those can cosist of many of the other
# - creates a hierarchy and a treelike structure
# - increases flexibility

from abc import ABCMeta, abstractmethod, abstractstaticmethod

class IDepartment(metaclass=ABCMeta):
    
    @abstractstaticmethod
    def print_department():
        """ Implement in child class """

    @abstractmethod
    def __init__(self, employees):
        """ Implement in child class """


class Accounting(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Accounting department: {self.employees}")


class Development(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Development department: {self.employees}")


class ParentDepartment(IDepartment):

    def __init__(self, employees):
        self.employees = employees
        self.base_employees = employees
        self.sub_depts = []

    def add(self, dept):
        self.sub_depts.append(dept)
        self.employees += dept.employees
        
    def print_department(self):
        print("Parent department")
        print(f"Parent department base employees: {self.base_employees}")
        print(f"Total number of employees: {self.employees}")
        for dept in self.sub_depts:
            print(dept.print_department())

        
d1 = Accounting(200) 
d2 = Development(30)

p_dept = ParentDepartment(30)
p_dept.add(d1)
p_dept.add(d2)
p_dept.print_department()

