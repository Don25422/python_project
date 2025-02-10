class Employee:
    def __init__(self,name,position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def details(self):
        print(self.name,"is the",self.position)

employee1 = Employee("John", "CEO", 20000)
print(employee1.name, employee1.position, employee1.salary)

employee2 = Employee("Jane", "Managing Director", 10000)
print(employee2.name, employee2.position, employee2.salary)

employee3 = Employee("Eunice", "Secretary", 2000)

