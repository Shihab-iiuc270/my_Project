from abc import ABC

class User(ABC):
    def __init__(self,name,phone,email,address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Employee(User):
    def __init__(self,name,phone,email,address,age,designation,salary):
        super().__init__(name,phone,email,address)
        self.age = age
        self.designation = designation
        self.salary = salary

class Admin(User):
    def __init__(self,name,phone,email,address,age,designation,salary):
        super().__init__(name,phone,email,address)
        
    def add_employee(self,restaurent,employee):
        restaurent.add_employee(employee)
    def view_employee(self,restaurent):
        restaurent.view_employee()

class Restaurent:
    def __init__(self,name):
        self.name = name
        self.employees = []
    def add_employee(self,employee):
        self.employees.append(employee)
    def view_employee(self):
        print("Employee List!!")
        for emp in self.employees:
            print(emp.name,emp.email,emp.address,emp.phone)

class Menu:
    def __init__(self):
        self.items = []

    def add_item(self,item):
        self.items.append(item)

    def find_item(self,item_name):
        for item in self.items:
            if item.name.lowe() == item_name.lower():
                return item
        return None
    def remove_item(self,item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("item removed successfully")
        else:
            print("Item not found")










        