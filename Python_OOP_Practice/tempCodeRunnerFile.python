import csv

class Book:
    counter = 0

    def __init__(self, ISBN, title, author, YOP) -> None:
        self.ISBN = ISBN
        self.title = title
        self.author = author
        self.YOP = YOP
        self.available = True

    def display_info(self):
        Book.counter += 1
        print(f"ID:{Book.counter}, ISBN: {self.ISBN}, Title: {self.title}, Author: {self.author}, Year of Publication: {self.YOP}, is_available: {self.available}")

    @staticmethod
    def import_books_from_csv(file_path):
        books = []
        with open(file_path, 'r', newline='', encoding='ISO-8859-1') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=';', quotechar='"')
            for row in reader:
                isbn = row['ISBN']
                title = row['Book-Title']
                author = row['Book-Author']
                yop = row['Year-Of-Publication']
                book_instance = Book(isbn, title, author, yop)
                books.append(book_instance)
        return books

    @staticmethod
    def reset_counter():
        Book.counter = 0


class Member:
    members_list = []

    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id
        self.borrowed_books = []
        Member.members_list.append(self)
        for member in Member.members_list:
            print(member.name)

    @classmethod
    def member_exists(cls, name):
        for member in cls.members_list:
            if member.name == name:
                return True
        return False

    def search_book(self, title, all_books):
        for book in all_books:
            if title.lower() in book.title.lower():
                print(f"Book Found - Title: {book.title}, Author: {book.author}, Available: {'Yes' if book.available else 'No'}")
                return book
        return None

    def borrow_book(self, book):
        if book.available:
            print(f'"{book.title}" has been successfully borrowed by "{self.name}". ')
            self.borrowed_books.append(book)
            book.available = False
        else:
            print(f'Sorry, "{book.title}" is not available for borrowing. It has been borrowed by {self.who_borrowed_book(book)}.')

    def who_borrowed_book(self, book):
        for member in Member.members_list:
            if book in member.borrowed_books and member != self:
                return member.name
        return "someone"

    def show_borrowed_books(self):
        if self.borrowed_books:
            print(f'Books borrowed by {self.name}:')
            for book in self.borrowed_books:
                print(book.title)
        else:
            print(f'No books borrowed by {self.name}.')

    def return_book(self, book_return):
        if book_return in self.borrowed_books:
            print(f'"{self.name}" has returned "{book_return.title}".')
            self.borrowed_books.remove(book_return)
            book_return.available = True
            self.show_borrowed_books()
        else:
            print(f'"{self.name}" did not borrow "{book_return.title}" or has already returned it.')

    def operations(self):
        def make_choice():
            choice = input('Do you want to search another book (yes/no)? ').strip()
            if choice == 'yes':
                self.operations()
            elif choice == 'no':
                self.show_borrowed_books()
                print('Have a good day! ')
            else:
                print('Invalid Choice! ')
                make_choice()

        title = input(f'Hi {self.name}, Enter Title Which You Want To Search: ').lower().strip()
        search = self.search_book(title, book_instances)

        if search:
            if search in self.borrowed_books:
                print(f'You already have "{search.title}" in your borrowed books list')
                make_choice()
            if search.available:
                choice = input(f'Do you want to borrow {search.title}: (yes/no)? ').strip()
                if choice == 'yes':
                    self.borrow_book(search)
                    make_choice()
                elif choice == 'no':
                    make_choice()
                else:
                    print('Invalid Choice! ')
                    make_choice()
            else:
                print(f'"{self.who_borrowed_book(search).title()}" had borrowed this book')
                make_choice()
        else:
            print(f'Sorry! We Do not Have "{title}". ')
            make_choice()

def main():
    try:
        global book_instances
        csv_file_path = 'books.csv'
        book_instances = Book.import_books_from_csv(csv_file_path)

        def add_new_member():
            new_member_name = input("Enter the name of the new member: ").strip()
            if not Member.member_exists(new_member_name):
                new_member_id = len(Member.members_list) + 1
                new_member = Member(new_member_name, new_member_id)
                print(f'New member "{new_member.name}" added with ID {new_member.id}.')
            else:
                print(f'Member "{new_member_name}" already exists.')

        def choices(member):
            choice = input(f'Welcome "{member.name}"! Do you want to explore the library now (yes/no)? ').strip()
            if choice == 'yes':
                member.operations()
            elif choice == 'no':
                print('Have a good day! See you soon.')
            elif choice == 'add':
                add_new_member()
                choices(member)
            elif choice not in ('yes', 'no', 'add'):
                print('Invalid Choice!')
                choices(member)

        while True:
            member_name = input("Enter the name of the member: ").strip()
            if Member.member_exists(member_name):
                existing_member = next(member for member in Member.members_list if member.name == member_name)
                choices(existing_member)
            else:
                member_id = len(Member.members_list) + 1
                new_member = Member(member_name, member_id)
                choices(new_member)

            another_member = input("Do you want to add another member (yes/no)? ").strip()
            if another_member.lower() != 'yes':
                print('Invalid Choide')
                another_member = input("Do you want to add another member (yes/no)? ").strip()
            

    except FileNotFoundError:
        print(f'File Not Found {csv_file_path}')


if __name__ == "__main__":
    main()
