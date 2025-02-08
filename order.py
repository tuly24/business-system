class Order:
    def __init__(self, customer_id, book_title, quantity):
        self.customer_id = customer_id
        self.book_title = book_title
        self.quantity = quantity

orders_list = []

def place_order(customer_id, book_title, quantity):
    new_order = Order(customer_id, book_title, quantity)
    orders_list.append(new_order)
    print(f"Order for {quantity} copy(ies) of '{book_title}' placed successfully!")

def list_orders():
    if not orders_list:
        print("No orders have been placed.")
    for order in orders_list:
        print(f"Customer ID: {order.customer_id}, Book Title: {order.book_title}, Quantity: {order.quantity}")

