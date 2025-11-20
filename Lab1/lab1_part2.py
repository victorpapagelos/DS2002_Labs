class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__ (self, name, age, employee_id, position, salary, raise_amount, address, task, bonus, manager=None):
        super(). __init__(name, age)
        self.employee_id = employee_id
        self.position = position
        self.salary = salary
        self.raise_amount = raise_amount
        self.address= address
        self.task = task
        self.bonus = bonus
        self.manager = manager

    def get_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Employment ID: {self.employee_id}, Position: {self.position}, Salary: {self.salary} Address: {self.address}, Task: {self.task}")

    def salary_raise(self, percent=None):
        print(f"Current Salary: {self.salary}")
        if percent is None:
            percent = float(input("Enter raise percentage "))
        self.raise_amount = percent / 100
        self.salary += self.salary * self.raise_amount
        print(f"New salary for {self.name} after {percent}% raise: {self.salary}")

    def calculate_bonus(self):
        self.bonus = self.salary*0.05
        print(f"Bonus for {self.name} ({self.position}) is 5% of their salary, Bonus = {self.bonus}")

    def __str__ (self):
        return (f"{self.name} ({self.position}, Salary: {self.salary})")

class Manager(Employee):
    def __init__ (self, name, age, employee_id, position, salary, raise_amount, address, task, bonus, subordinates):
        super().__init__(name, age, employee_id, position, salary, raise_amount, address, task, bonus)
        if subordinates is None:
            self.subordinates = []
        else:
            self.subordinates = subordinates

    def add_subordinate(self, subordinate):
        self.subordinates.append(subordinate)
        print(f"Added {subordinate} as subordinate")

    def remove_subordinate(self, subordinate):
        self.subordinates.remove(subordinate)
        print(f"Removed {subordinate} as subordinate")
    
    def get_subordinates(self):
        print(f"{self.name}'s Subordinates: {[sub.name for sub in self.subordinates]}")

    def calculate_bonus(self):
        base_bonus = self.salary * 0.05
        manager_bonus = self.salary * 0.01 * len(self.subordinates)
        self.bonus = base_bonus + manager_bonus
        print(f"Base Bonus for {self.name} ({self.position}) is 5% of their salary, Bonus = {self.bonus}")
        print(f"Subordinate bonus (1% x {len(self.subordinates)} = {manager_bonus})")
        print(f"Final Bonus: {self.bonus + manager_bonus}")

    def get_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}, Position: {self.position}, Salary: {self.salary}, Address: {self.address}, Task: {self.task}")
        print(f"Number of Subordinates: {len(self.subordinates)}")
        sub_names = [sub.name for sub in self.subordinates]
        print(f"Subordinates: {sub_names}")

class Company:
    def __init__ (self, name, CEO):
        self.name = name
        self.employees = []
        self.CEO = CEO

    def add_employee(self, employee):
        if employee is self.CEO:
            print("The CEO can not be added as a regular employee")
            return
        self.employees.append(employee)
        print(f"Employee {employee} added.")
        if employee.manager is not None:
            employee.manager.add_subordinate(employee)
    
    def remove_employee(self, employee):
        if employee is self.CEO:
            print("Error: Can not Remove CEO from company.")
            return
        if isinstance(employee, Manager):
            print(f"Reassigning {employee.name}'s subordinates to CEO")
            for sub in employee.subordinates:
                self.CEO.add_subordinate(sub)
            employee.subordinates = []

        if employee in self.employees:
            self.employees.remove(employee)
            print(f"Employee {employee} removed.")


    
    def list_hierarchy(self):
        print(f"Company: {self.name}")
        print("CEO: ")
        self.CEO.get_details()

        print(f"Employees in {self.name}:")
        for emp in self.employees:
            emp.get_details()

    def company_salary(self):
        total = self.CEO.salary
        for emp in self.employees:
            total += emp.salary
        print(f"Total salaries being paid in {self.name}: {total}")

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
        self.time = time
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
        attend = [a.name for a in self.attending]
        print(f"Meeting on the topic {self.topic}, Attending: {attend} Time: {self.time}, Location: {self.location}")

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

#CEO/General-Manager
CEO_addr = Address("P road", "Halmstad")
                                                          #Salary Raise           Task  Bonus Subordinates 
CEO = Manager("John", 45, "M123", "CEO / General-Manager", 80000, None, CEO_addr, None, None, [] )

#Company  
company = Company("Halmstad Högskola Inc. ", CEO)

#Meetings
meeting1=Meeting("Resources", "12pm", "Conference Room")

#Tasks
task1=Task("Reconstruction of the company", "TBD")
task2=Task("Employee Supervision", "None")
task3=Task("Book-Keeping", "in 2 weeks")

#Assistant Manager (2nd Manager)
assis_manager_addr = Address("Z Road", "Halmstad")
#                                                              Salary Raise                     Task  Manager Subs
assis_manager=Manager("Bob", 32, "AM123", "Assistant-Manager", 65000, None, assis_manager_addr, None, "John", [])
#assis_manager_task = task2

#Employee 1
emp1_addr = Address("A road", "Halmstad")
emp1 = Employee("Alice", 30, "E001", "Developer", 30000, None, emp1_addr, None, None)
#emp1_task = task3
#Employee 2
emp2_addr = Address("B Road", "Halmstad")
emp2 = Employee("Thomas", 23, "E002", "Accountant", 28000, None, emp2_addr, None, None)
#Employee 3
emp3_addr = Address("C Road", "Halmstad")
emp3 = Employee("Leo", 48, "E003", "Productioneer", 36000, None, emp3_addr, None, None)


#Adding Employees, Subordinates, Manager, Tasks, Meeting
company.add_employee(assis_manager)
company.add_employee(emp1)
company.add_employee(emp2)
company.add_employee(emp3)

task1.add_task_performer(CEO)
task2.add_task_performer(assis_manager)
task3.add_task_performer(emp2)


#Meeting
meeting1.add_attending(CEO)
meeting1.add_attending(assis_manager)
meeting1.add_attending(emp1)
meeting1.make_meeting()

#Subordinates
CEO.add_subordinate(emp1)
CEO.add_subordinate(emp2)
CEO.add_subordinate(assis_manager)
assis_manager.add_subordinate(emp3)

#"Details"
CEO.get_subordinates()
CEO.calculate_bonus()
assis_manager.calculate_bonus()

#Remove a Manager
#company.remove_employee(assis_manager)
#CEO.get_subordinates()

#Remove employee
#company.remove_employee(emp2)
#company.list_hierarchy()

#Raise
#emp1.salary_raise(5)

#Company Salaries being paid
company.company_salary()
company.remove_employee(CEO)