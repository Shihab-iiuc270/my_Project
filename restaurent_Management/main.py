from food_items import FoodItem
from menu import Menu
from users import Admin,Customer,Employee
from orders import Order
from restaurent import Restaurent
mamar_res = Restaurent("Allahr Dan")
def customer_menu():
    name = input("Enter YOur name : ")
    email = input("Enter your Email : ")
    phone = input("Enter YOur phone : ")
    address = input("Enter YOur address : ")
    customer = Customer(name=name,email=email,phone=phone,address=address)

    while True:
        print(f"Welcome {customer.name}!!")
        print("1.View Menu")
        print("2.Add item to Cart!!")
        print("3.View Cart")
        print("4.Paybill")
        print("5.Exit")

        choice = int((input("Enter YOur choice : ")))
        if choice == 1:
            customer.view_menu(mamar_res)
        elif choice == 2:
            item_name = input("Enter item name : ")
            quan = int(input("Enter item quantity : "))
            customer.add_to_cart(mamar_res,item_name=item_name,quantity= quan)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            break
        else:
            print("Invalid Choice")

def admin_menu():
    name = input("Enter YOur name : ")
    email = input("Enter your Email : ")
    phone = input("Enter YOur phone : ")
    address = input("Enter YOur address : ")
    admin = Admin(name=name,email=email,phone=phone,address=address)

    while True:
        print(f"Welcome {admin.name}!!")
        print("1.Add New Item")
        print("2.Add New Employee!!")
        print("3.View employee")
        print("4.view items")
        print("5.delete items")
        print("6.Exit")

        choice = int((input("Enter YOur choice : ")))
        # if choice == 1:
        #     admin.view_menu(mamar_res)
        if choice == 1:
            item_name = input("Enter item name : ")
            item_price = int(input("Enter item price : "))
            quan = int(input("Enter item quantity : "))
            item = FoodItem(item_name,item_price,quantity=quan)
            admin.add_new_item(mamar_res,item=item)
        elif choice == 2:
            name = input("Enter employee name : ")
            phone = input("Enter employee number : ")
            email = input("Enter employee mail : ")
            designation = input("Enter employee designaiton : ")
            age  = input("Enter employee age : ")
            address = input("Enter employee address : ")
            salary = input("Enter salary : ")
            emp = Employee(name=name,phone=phone,email=email,address=address,age=age,designation=designation,salary=salary)
            admin.add_employee(mamar_res,emp)
        elif choice == 3:
            admin.view_employee(mamar_res)
        elif choice == 4:
            admin.view_menu(mamar_res)
        elif choice == 5:
            item = input("Enter item name: ")
            admin.remove_item(mamar_res,item=item)
        elif choice == 6:
            break
        else:
            print("Invalid choice")

while True:
    print("Welcome !!")
    print("1.Customer")
    print("2.Admin")
    print("3.Exit")

    choice = int(input("Enter Your choice : "))
    if choice ==1 :
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice  == 3:
        break
    else:
        print("Invalid input")
    
