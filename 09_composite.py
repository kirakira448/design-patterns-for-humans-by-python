from abc import ABC, abstractmethod
import unittest

class Employee(ABC):
    @abstractmethod
    def __init__(self, name: str, salary: int):
        self._name = name
        self._salary = salary

    @abstractmethod
    def name(self):
        pass

    @property
    def salary(self):
        pass

    @salary.setter
    def salary(self, salary: int):
        pass

    @abstractmethod
    def get_roles(self):
        pass


class Developer(Employee):
    def __init__(self, name: str, salary: int):
        super().__init__(name, salary)
        self.roles = ["Developer"]
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, salary: int):
        self._salary = salary
    
    def get_roles(self):
        return self.roles

class Designer(Employee):
    def __init__(self, name: str, salary: int):
        super().__init__(name, salary)
        self.roles = ["Designer"]
        
    @property
    def name(self):
        return self._name   

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary: int):
        self._salary = salary

    def get_roles(self):
        return self.roles

class Organization:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee: Employee): 
        self.employees.append(employee)

    def get_net_salaries(self):
        return sum(employee.salary for employee in self.employees)

class TestComposite(unittest.TestCase):
    def test_organization(self):
        organization = Organization()

        john = Developer("John Doe", 12000)
        jane = Designer("Jane Doe", 10000)

        organization.add_employee(john)
        organization.add_employee(jane)

        self.assertEqual(organization.get_net_salaries(), 22000)

if __name__ == "__main__":
    unittest.main()
