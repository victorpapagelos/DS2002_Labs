class Company:
    def __init__ (self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Employee {employee} added.")
    
    def remove_employee(self, employee):
        self.employees.remove(employee)
        print(f"Employee {employee} removed.")
    
    def list_employees(self):
        print(f"Employees in {self.name}:")
        for emp in self.employees:
            emp.get_details()

class Address:
    def __init__(self, street, city):
        self.street = street
        self.city = city
    
    def get_address(self):
        return(f"{self.street}, {self.city}")
    
    def __str__(self):
        return self.get_address()

class Meeting:
    def __init__(self, topic, time, location, attending = None):
        self.topic = topic
        self. time = time
        self.location = location
        if attending is None:
            self.attending = []
        else:
            self.attending = attending

    def add_attending(self, employee):
        self.attending.append(employee)
    
    def remove_attending(self, employee):
        self.attending.remove(employee)


    def make_meeting(self):
        print(f"Meeting on the topic {self.topic}, Attending: {self.attending} Time: {self.time}, Location: {self.location}")

class Task:
    def __init__(self, task, due_date, performers = None):
        self.task = task
        self.due_date = due_date
        if performers is None:
            self.performers = []
        else:
            self.performers = performers

    def add_task_performer(self, employee):
        self.performers.append(employee)
        employee.task = self
    
    def remove_task_performer(self, employee):
        self.performers.remove(employee)

    def __str__(self):
        performer_names = [p.name for p in self.performers]
        return (f"{self.task}, Due date: {self.due_date}, Performers: {performer_names}")

class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__ (self, name, age, employee_id, position, salary, raise_amount, address, task):
        self.name = name
        self.age = age
        self.employee_id = employee_id
        self.position = position
        self.salary = salary
        self.raise_amount = raise_amount
        self.address= address
        self.task = task

    def get_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}, Position: {self.position}, Salary: {self.salary} Address: {self.address}, Task: {self.task}")

    def salary_raise_percent(self):
        print(f"Current Salary: {self.salary}")
        self.raise_amount = float(input("Enter raise percentage)"))/100
        self.salary += self.salary * self.raise_amount
        print(f"New Salary after raise: {self.salary}")

    def __str__ (self):
        return (f"{self.name} ({self.position}, Salary: {self.salary})")

class Manager(Employee):
    def __init__ (self, subordinates, name, age, employee_id, position, salary, raise_amount, address, task):
        self.name = name
        self.age = age
        self. employee_id = employee_id
        self.position = position
        self.salary = salary
        self.raise_amount = raise_amount
        self.subordinates = subordinates
        self.address = address
        self.task = task
    def add_subordinate(self, subordinate):
        self.subordinates.append(subordinate)
        print(f"Added {subordinate} as subordinate")

    def remove_subordinate(self, subordinate):
        self.subordinates.remove(subordinate)
        print(f"Removed {subordinate} as subordinate")
    
    def get_subordinates(self):
        print(f"{self.name}'s Subordinates: {[sub.name for sub in self.subordinates]}")
        


#Company  
company = Company("Halmstad Högskola Inc. ")

#Meetings
meeting1=Meeting("Resources", "12pm", "Conference Room")

#Tasks
task1=Task("Reconstruction of the company", "TBD")
task2=Task("Employee Supervision", "None")
task3=Task("Book-Keeping", "in 2 weeks")

#Manager
manager_addr = Address("P road", "Halmstad")
manager = Manager([], "John", 45, "M123", "Manager", 80000, 0.01, manager_addr, None)
#manager_task = task1

#Assistant Manager (2nd Manager)
assis_manager_addr = Address("Z Road", "Halmstad")
assis_manager=Manager([], "Bob", 32, "AM123", "Assistant-Manager", 65000, 0.01, assis_manager_addr, None)
#assis_manager_task = task2

#Employee 1
emp1_addr = Address("A road", "Halmstad")
emp1 = Employee("Alice", 30, "E001", "Developer", 30000, 0.01, emp1_addr, None)
#emp1_task = task3
#Employee 2
emp2_addr = Address("B Road", "Halmstad")
emp2 = Employee("Thomas", 23, "E002", "Accountant", 28000, 0.01, emp2_addr, None)
#Employee 3
emp3_addr = Address("C Road", "Halmstad")
emp3 = Employee("Leo", 48, "E003", "Productioneer", 36000, 0.01, emp3_addr, None)

#Calling Functions
company.add_employee(manager)
task1.add_task_performer(manager)

company.add_employee(assis_manager)
task2.add_task_performer(assis_manager)

company.add_employee(emp1)
task3.add_task_performer(emp1)

company.add_employee(emp2)
company.add_employee(emp3)

manager.add_subordinate(emp1)
manager.add_subordinate(emp2)

assis_manager.add_subordinate(emp3)

manager.get_subordinates()
assis_manager.get_subordinates()

company.list_employees()

