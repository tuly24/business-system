class Customer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

customers_list = []

def add_customer(name, email, phone):
    new_customer = Customer(name, email, phone)
    customers_list.append(new_customer)
    print(f"Customer '{name}' added successfully!")

def list_customers():
    if not customers_list:
        print("No customers available.")
    for customer in customers_list:
        print(f"Name: {customer.name}, Email: {customer.email}, Phone: {customer.phone}")

