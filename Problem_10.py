# SUPERMARKET MANAGEMENT SYSTEM

#importing imoprtant packages
import csv
import datetime

#all these variables are global variables
# Define a dictionary to store product information
products = {}

def save_product(name, price, type):
    p_fields = ["Name","Price","Type"]
    p_data = [name, price, type]
    with open("Products.csv", "w+") as p_file:
        p_csv = csv.writer(p_file)
        p_csv.writerow(p_fields)
        p_csv.writerow(p_data) 
    print ("Product saved successfully")
    p_file.close()

# Define a dictionary to store product type information
product_types = {}

# Define a list to store bills
bills = []

# Define a dictionary to store customer feedback
feedback = {}

# A.Define a function to prompt the user to enter the admin username and password
def admin_login():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    if username == "g5" and password == "123":
        #calling the function for further details
        manage_product()
    else:
        print("\nInvalid username or password")
        print("Re-enter your valid username and password:")
        admin_login()
    
# B.Define a function to manage products
def manage_product():
    while True:
        print("\nPRODUCT MENU")
        print("1. Add new product")
        print("2. Edit the Existing Product")
        print("3. View details of the Product")
        print("4. Listing of all Product Manage Product Type")
        print("5. Add New Product Type")
        print("6. Edit the Existing Product Type")
        print("7. View details of the Product Type")
        print("8. Print Bill")
        print("0. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 0:
            break
        elif choice == 1:
            add_product()
        elif choice == 2:
            edit_product()
        elif choice == 3:
            view_product()
        elif choice == 4:
            list_products()
        elif choice == 5:
            add_product_type()
        elif choice == 6:
            edit_product_type()
        elif choice == 7:
            view_product_type()
        elif choice == 8:
            new_bill()
        else:
            print("Invalid choice")

# B.1.Define a function to add a new product
def add_product():
    print("Enter product details:")
    name = input("Name: ")
    price = float(input("Price: "))
    product_type = input("Type: ")
    if product_type not in product_types:
        print("Invalid product type")
        return
    products[name] = {"price": price, "type": product_type}
    print("Product added successfully")
    save_product(name, price, product_type)

# B.2.Define a function to edit an existing product
def edit_product():
    name = input("Enter product name: ")
    if name not in products:
        print("Product not found")
        return
    print("Enter new product details:")
    price = float(input("Price: "))
    product_type = input("Type: ")
    if product_type not in product_types:
        print("Invalid product type")
        return
    products[name] = {"price": price, "type": product_type}
    print("Product edited successfully")
    save_product()

# B.3.Define a function to view details of a product
def view_product():
    name = input("Enter product name: ")
    if name not in products:
        print("Product not found")
        return
    print(f"Name: {name}")
    print(f"Price: {products[name]['price']}")
    print(f"Type: {products[name]['type']}")

# B.4.Define a function to list all products
def list_products():
    if not products:
        print("No products found")
        return
    for name, details in products.items():
        print(f"Name: {name}")
        print(f"Price: {details['price']}")
        print(f"Type: {details['type']}")
        print()

# B.5.Define a function to add a new product type
def add_product_type():
    name = input("Enter product type name: ")
    description = input("Enter product type description: ")
    product_types[name] = description
    print("Product type added successfully")

# B.6.Define a function to edit an existing product type
def edit_product_type():
    name = input("Enter product type name: ")
    if name not in product_types:
        print("Product type not found")
        return
    description = input("Enter new product type description: ")
    product_types[name] = description
    print("Product type edited successfully")

# B.7.Define a function to view details of a product type
def view_product_type():
    name = input("Enter product type name: ")
    if name not in product_types:
        print("Product type not found")
        return
    print(f"Name: {name}")
    print(f"Description: {product_types[name]}")

# C.1.Define a function for create a New Bill
def new_bill():
    # Get customer information
    customer_name = input("Enter customer name: ")
    customer_address = input("Enter customer address: ")
    customer_phone = input("Enter customer phone number: ")
    
    # Initialize an empty list to store purchased products
    purchased_items = []
    purchased_items.append({
        "Customer_phone": customer_phone,
    })
    # Loop to add products to the bill
    while True:
        product_name = input("Enter product name: ")
        
        # Check if user wants to stop adding products
        if product_name == "0":
            break
        
        # Check if product with given ID exists
        ###product = list_products(product_name)
        #product = products.items()
        if product_name not in products:
            print("Product not found")
            continue
        
        # Get quantity of the product
        quantity = int(input("Enter quantity: "))
        
        # Calculate the total price for the product
        price = products[product_name]["price"] * quantity
        
        # Add the purchased product to the list
        purchased_items.append({
            "product_name": product_name,
            "quantity": quantity,
            "price": price
        })
    
    # Calculate the total price of the bill
    total_price = sum(item.get("price",0) for item in purchased_items)
    
    bills.append({
        "customer_name": customer_name,
        "customer_address": customer_address,
        "customer_phone": customer_phone,
        "purchased_items": purchased_items,
        "total_price": total_price
    })

    # Print the bill
    print("\nBILL")
    print("Customer name:", customer_name)
    print("Customer address:", customer_address)
    print("Customer phone:", customer_phone)
    total_price = sum(item.get("price", 0) for item in purchased_items)
    print("Total price:", total_price)
    print("Date & time =", datetime.datetime.now())
    var=input("If you want to edit your bill then press 1 else press any Key to continue")
    if(var=='1'):
        edit_bill()
    else:
        customer_feedback()



# C.2.Define a function to Edit the Existing Bill by using customers Phone number as a unique id
def edit_bill():
    # Get bill information
    customer_phone = input("Enter Customers Phone number to edit the bill: ")
    
    # Check if bill with given ID exists
    ###bill = list_products(customer_phone)
    bill = products[customer_phone]
    if bill is None:
        print("Bill not found")
        return
    
    # Print the current bill information
    print("\nCURRENT BILL")
    print("Customer name:", bill["customer_name"])
    print("Customer address:", bill["customer_address"])
    print("Customer phone:", bill["customer_phone"])
    print("Total price:", bill["total_price"])
    
    # Prompt user for changes to the bill information
    new_customer_name = input("Enter new customer name (leave blank to keep current): ")
    new_customer_address = input("Enter new customer address (leave blank to keep current): ")
    new_customer_phone = input("Enter new customer phone number (leave blank to keep current): ")
    
    # Update the bill with the changes
    if new_customer_name:
        bill["customer_name"] = new_customer_name
    if new_customer_address:
        bill["customer_address"] = new_customer_address
    if new_customer_phone:
        bill["customer_phone"] = new_customer_phone
    
    # Loop to edit purchased items
    while True:
        # Print current purchased items
        print("\nCURRENT PURCHASED ITEMS")
        for i, item in enumerate(bill["purchased_items"]):
            print("{}: {} x {} = {}".format(i+1, item["name"], item["quantity"], item["price"]))
        
        # Prompt user for action
        action = input("Enter item number to edit (0 to exit, -1 to add new item): ")
        
        # Check if user wants to exit
        if action == "0":
            break
        
        # Check if user wants to add a new item
        if action == "-1":
            product_name = input("Enter product Name: ")
            # Check if product with given ID exists
            ###product = list_products(product_name)
            #product = products["product_name"]
            if product_name is None:
                print("Product not found")
                continue
            quantity = int(input("Enter quantity: "))
            price = products[product_name]["price"] * quantity
            bill["purchased_items"].append({
                "product_name": product_name,
                "name": product_name,
                "quantity": quantity,
                "price": price
            })
            continue
        
        # Check if item number is valid
        try:
            item_num = int(action) - 1
            if item_num < 0 or item_num >= len(bill["purchased_items"]):
                raise ValueError
        except ValueError:
            print("Invalid item number")
            continue
        
        # Get the item to edit
        item = bill["purchased_items"][item_num]
        
        def find_product_by_id(product_id):
            for product in products.values():
                if product["product_id"] == product_id:
                    return product
                    return None


        # Prompt user for changes to the item information
        new_quantity = int(input("Enter new quantity (leave blank to keep current): "))
        if new_quantity:
            new_price = new_quantity * products[item["product_name"]]["price"]
            item["quantity"] = new_quantity
            item["price"] = new_price
    
    # Recalculate the total price of the bill
    total_price = sum(item["price"] for item in bill["purchased_items"])
    bill["total_price"] = total_price
    
    # Print the updated bill information
    print("\nUPDATED BILL")
    customer_feedback()


# D.Define a function for filling the Feedback from customer
def customer_feedback():
    # Get customer information
    print("Customer Feedback")
    name = input("Enter your name: ")
    email = input("Enter your email address: ")
    phone = input("Enter your phone number: ")
    
    # Get feedback information
    print("\nPlease rate our store on a scale of 1-5")
    rating = int(input("Enter your rating: "))
    if rating < 1 or rating > 5:
        print("Invalid rating")
        return
    
    feedback = input("Enter your feedback: ")
    
    # Save feedback to database or file
    save_feedback(name, email, phone, rating, feedback)
    
    print("Thank you for your feedback!")
# D.1. Save feedback to a csv file
def save_feedback(name, email, phone, rating, feedback):
    f_dict = {"Name":name, "Email":email, "Phone":phone, "Rating":rating, "Feedback":feedback}
    f_field = ["Name", "Email", "Phone","Rating","Feedback"]
    with open("feedback.csv", 'a+') as f_feed:
        feed = csv.DictWriter(f_feed, fieldnames=f_field)
        feed.writerow(f_dict)
    f_feed.close()
    return 0

#main functions begins here!
admin_login()