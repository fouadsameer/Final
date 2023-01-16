import datetime

class Client:
    def __init__(self, id, full_name, age, id_no, phone_number):
        self.id = id
        self.full_name = full_name
        self.age = age
        self.id_no = id_no
        self.phone_number = phone_number

class Librarian:
    def __init__(self, id, full_name, age, id_no, employment_type):
        self.id = id
        self.full_name = full_name
        self.age = age
        self.id_no = id_no
        self.employment_type = employment_type

class Book:
    def __init__(self, id, title, description, author, status):
        self.id = id
        self.title = title
        self.description = description
        self.author = author
        self.status = status

class BorrowingOrder:
    def __init__(self, id, date, client_id, book_id, status):
        self.id = id
        self.date = date
        self.client_id = client_id
        self.book_id = book_id
        self.status = status


class MainFile:
    def __init__(self):
        self.clients_list = []
        self.librarians_list = []
        self.books_list = []
        self.borrowed_orders_list = []

    def create_new_client(self, client_info):
        new_client = Client(*client_info)
        self.clients_list.append(new_client)

    def create_new_librarian(self, librarian_info):
        new_librarian = Librarian(*librarian_info)
        self.librarians_list.append(new_librarian)

    def create_new_book(self, book_info):
        new_book = Book(*book_info)
        self.books_list.append(new_book)

    def borrow_book(self, librarian_id, book_id, client_id_no):
        # Check if librarian exists in system
        librarian_exists = False
        for librarian in self.librarians_list:
            if librarian.id_no == librarian_id:
                librarian_exists = True
                break
        if not librarian_exists:
            print("Librarian not found in the system.")
            return
        # Check if book is available for borrowing
        for book in self.books_list:
            if book.id == book_id and book.status == "Available":
                # Check if client exists in system
                client_exists = False
                for client in self.clients_list:
                    if client.id_no == client_id_no:
                        client_exists = True
                        break
                if client_exists:
                    # Create borrowing order
                    new_order = BorrowingOrder(len(self.borrowed_orders_list) + 1,
                                               datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                               client_id_no, book_id, "Active")
                    self.borrowed_orders_list.append(new_order)
                    book.status = "Unavailable"
                    print("Borrowing Order Created Successfully!")
                else:
                    print("Client not found in the system.")
            else:
                print("Book not available for borrowing.")

    def search_order(self, order_id):
        for order in self.borrowed_orders_list:
            if order.id == order_id:
                return order
        return None

    def show_all_orders(self):
        for order in self.borrowed_orders_list:
            print(order.__dict__)

def main():
    main_file = MainFile()

    user_role = input("Enter as a client or librarian: ")
    if user_role.lower() == "client":
        client_id = input("Enter your ID: ")
        client_full_name = input("Enter your full name: ")
        client_age = input("Enter your age: ")
        client_id_no = input("Enter your ID number: ")
        client_phone_number = input("Enter your phone number: ")
        main_file.create_new_client([client_id, client_full_name, client_age, client_id_no, client_phone_number])
    elif user_role.lower() == "librarian":
        librarian_id = input("Enter your ID: ")
        librarian_full_name = input("Enter your full name: ")
        librarian_age = input("Enter your age: ")
        librarian_id_no = input("Enter your ID number: ")
        librarian_employment_type = input("Enter your employment type (Full/Part): ")
        main_file.create_new_librarian([librarian_id, librarian_full_name, librarian_age, librarian_id_no, librarian_employment_type])

    # create books
    books_number = int(input("Enter the number of books you want to create: "))
    for i in range(books_number):
        book_id = input("Enter book ID: ")
        book_title = input("Enter book title: ")
        book_description = input("Enter book description: ")
        book_author = input("Enter book author: ")
        main_file.create_new_book([book_id, book_title, book_description, book_author, "Available"])

    # Borrow book
    if user_role.lower() == "librarian":
        librarian_id = input("Enter Librarian ID: ")
        book_id = input("Enter the book ID you want to borrow: ")
        client_id_no = input("Enter the client ID number: ")
        main_file.borrow_book(librarian_id, book_id, client_id_no)

    # search for an order
    order_id = input("Enter order ID: ")
    order = main_file.search_order(order_id)
    if order:
        print(order.__dict__)
    else:
        print("Order not found.")

    # show all orders
    main_file.show_all_orders()

if __name__ == "__main__":
    main()

