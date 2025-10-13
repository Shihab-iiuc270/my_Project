from abc import ABC
from orders import Order
class User(ABC):
    def __init__(self,name,phone,email,address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Employee(User):
    def __init__(self, name, phone, email, address,age,designation,salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.address = address
        self.designation = designation
        self.salary = salary
# emp = Employee("shihab",102838,"shihab@gmail.com","patiya",23,"student",10000)
# print(emp.name,emp.salary)
class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        
    def add_employee(self,restaurent,employee):
        restaurent.add_employee(employee)

    def view_employee(self,restaurent):
        restaurent.view_employee()

    def add_new_item(self,restaurent,item):
        restaurent.menu.add_menu_item(item)

    def remove_item(self,restaurent,item):
        restaurent.menu.remove_item(item)
    def view_menu(self,restaurent):
        restaurent.menu.show_menu()
        
class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def view_menu(self,restaurent):
        restaurent.menu.show_menu()
    def add_to_cart(self,restaurent,item_name,quantity):
        item = restaurent.menu.find_item(item_name)
        if item:
            if(item.quantity<quantity):
                print("Invalid Quantity!!!.\nItem Quantity EXceeded!!!")
            else:
                item.quantity = quantity
                self.cart.add_item(item)
        else:
            print("Item not found!!")
    def view_cart(self):
        print("Your Cart!!")
        print("Name\t Price\t Quantity")
        for item,quantity in self.cart.items.items():
            print(f"{item.name} {item.price} {quantity}")
        print(f"Total Prince :{self.cart.total_prise} ")

    def pay_bill(self):
        print(f"Total {self.cart.total_prise} paid Successfully")
        self.cart.clear()



        
# mn = Menu()
# item = FoodItem("pizza",12.45,10)
# item2 = FoodItem("sadh",115,30)
# mamr_res = Restaurent("ALLah Dan")

# # mn.show_menu()



# customer1 = Customer("abdur rahim","abdurrahim@",402802,"dhak")
# admin = Admin("abdur rahim","abdurrahim@",402802,"dhak")
# admin.add_new_item(mamr_res,item)
# admin.add_new_item(mamr_res,item2)
# customer1.view_menu(mamr_res)
# item_name = input("Enter item name : ")
# item_quan = int(input("Enter item quantity : "))
# customer1.add_to_cart(mamr_res,item_name,item_quan)
# customer1.view_cart()
# customer1.add_to_cart(mamr_res,item,5)
# customer1.view_cart()


# ad = Admin("sagor",1234,"sagor@","dhaka")
# ad.add_employee("shiha",4883,"shihabu2w8i","dhk",22,"std",23)

# ad.view_employee()
