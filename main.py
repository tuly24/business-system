from book import add_book, list_books
from customer import add_customer, list_customers
from order import place_order, list_orders

def menu():
    print("1. Add Book")
    print("2. List Books")
    print("3. Add Customer")
    print("4. List Customers")
    print("5. Place Order")
    print("6. List Orders")
    print("7. Exit")

def main():
    while True:
        menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            title = input("Enter book title: ")
            author = input("Enter author: ")
            genre = input("Enter genre: ")
            price = float(input("Enter price: "))
            add_book(title, author, genre, price)

        elif choice == 2:
            list_books()

        elif choice == 3:
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            phone = input("Enter customer phone: ")
            add_customer(name, email, phone)

        elif choice == 4:
            list_customers()

        elif choice == 5:
            customer_id = int(input("Enter customer ID: "))
            book_title = input("Enter book title: ")
            quantity = int(input("Enter quantity: "))
            place_order(customer_id, book_title, quantity)

        elif choice == 6:
            list_orders()

        elif choice == 7:
            print("Exiting system.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()




