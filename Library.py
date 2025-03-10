

class Book:
    def __init__(self, name, author, book_id):
        self.name = name
        self.author = author
        self.book_id = book_id
        self.next = None

class Student:
    def __init__(self, name, email, book, author, student_id):
        self.name = name
        self.email = email
        self.book = book
        self.author = author
        self.student_id = student_id
        self.next = None

class Library:
    def __init__(self):
        self.start_lib = None
        self.start = None

    def initialize_lib(self):
        new_book1 = Book("The Kite Runner", "Khaled Hosseini", 101)
        new_book2 = Book("To Kill A Mockingbird", "Harper Lee", 102)
        new_book3 = Book("The Alchemist", "Paulo Coelho", 103)
        new_book4 = Book("Pride And Prejudice", "Jane Austen", 104)
        new_book5 = Book("A Tale Of Two Cities", "Charles Dickens", 105)

        self.start_lib = new_book1
        new_book1.next = new_book2
        new_book2.next = new_book3
        new_book3.next = new_book4
        new_book4.next = new_book5

    def book_issue(self):
        if self.start_lib is None:
            print("\n\t\t\t\t No books left in the library to issue!\n\t\t\t\t Sorry for the inconvenience!")
            return

        ptr = self.start_lib
        print("\n\t*************** Books Available: ****************")
        i = 1
        while ptr:
            print(f"\n\t_\n")
            print(f"\n\t Book {i}")
            print(f"\n\t Book Title: {ptr.name}")
            print(f"\n\t Name of Author: {ptr.author}")
            print(f"\n\t Book ID: {ptr.book_id}")
            print(f"\n\t_\n")
            ptr = ptr.next
            i += 1

        book_id = int(input("\n\n\t Enter the Book ID: "))
        ptr = self.start_lib
        flag = False
        while ptr:
            if ptr.book_id == book_id:
                flag = True
                break
            ptr = ptr.next

        if flag:
            new_student = Student(
                input("\n\t Enter your Name: "),
                input("\n\t Enter your Email: "),
                ptr.name,
                ptr.author,
                ptr.book_id
            )

            print(f"\n\t Issue of Book ID {new_student.student_id} done successfully!\n")

            if self.start is None:
                self.start = new_student
            else:
                student_ptr = self.start
                while student_ptr.next:
                    student_ptr = student_ptr.next
                student_ptr.next = new_student

            self.start_lib = self.delete_book(new_student.student_id)
            print("\n\n\t Press any key to go to the main menu: ")

        else:
            print("\n\t\t      ...Invalid Option!...")

    def book_return(self):
        student_id = int(input("\n\n\t*************** Books Submission: ****************\n\n\t Enter your Book ID: "))
        ptr = self.start
        flag = False
        while ptr:
            if ptr.student_id == student_id:
                flag = True
                break
            ptr = ptr.next

        if flag:
            print(f"\n\t_\n")
            print(f"\n\t Student Name: {ptr.name}")
            print(f"\n\t Student Email: {ptr.email}")
            print(f"\n\t Name of Book Issued: {ptr.book}")
            print(f"\n\t Book ID: {ptr.student_id}")
            print(f"\n\t_\n")
            self.start = self.remove_student(ptr.student_id)
            self.add_book(ptr.book, ptr.author, ptr.student_id)
            print(f"\n\t Return of Book ID {student_id} done successfully!\n")
            print("\n\t Thank you! Do visit again!")
        else:
            print("\n\tSorry, the book doesn't exist! Please recheck the entered ID.")

    def remove_student(self, student_id):
        ptr = self.start
        preptr = None
        while ptr and ptr.student_id != student_id:
            preptr = ptr
            ptr = ptr.next

        if ptr is None:
            return self.start

        if preptr is None:
            self.start = ptr.next
        else:
            preptr.next = ptr.next

        return self.start

    def add_book(self, bookname, authorname, book_id):
        new_book = Book(bookname, authorname, book_id)
        if self.start_lib is None:
            self.start_lib = new_book
        else:
            ptr = self.start_lib
            while ptr.next:
                ptr = ptr.next
            ptr.next = new_book

    def delete_book(self, book_id):
        ptr = self.start_lib
        preptr = None
        while ptr and ptr.book_id != book_id:
            preptr = ptr
            ptr = ptr.next

        if ptr is None:
            return self.start_lib

        if preptr is None:
            self.start_lib = ptr.next
        else:
            preptr.next = ptr.next

        return self.start_lib

    def display(self):
        ptr = self.start
        while ptr:
            print(f"\n\t************* Details of Students: **************")
            print(f"\n\t_\n")
            print(f"\n\t\t Student Name: {ptr.name}")
            print(f"\n\t\t Student Email: {ptr.email}")
            print(f"\n\t\t Name of Book Issued: {ptr.book}")
            print(f"\n\t\t Book ID: {ptr.student_id}")
            print(f"\n\t_\n")
            print(f"\n\n\t*\n")
            ptr = ptr.next
        print("\n\n\t Press any key to go to the main menu: ")

    def greetings(self):
        print("\n\n")
        print("\t\t\t     ****************************************")
        print("\t\t\t     *                                      *")
        print("\t\t\t     *                                      *")
        print("\t\t\t     *     ----------------------------     *")
        print("\t\t\t     *      WELCOME TO STUDENT LIBRARY      *")
        print("\t\t\t     *     ----------------------------     *")
        print("\t\t\t     *                                      *")
        print("\t\t\t     *                                      *")
        print("\t\t\t     ****************************************")
        print("\n\n")
        print("\t\t\t     ****************************************")
        print("\t\t\t     *                                      *")
        print("\t\t\t     *       ------------------------       *")
        print("\t\t\t     *           STUDENT LIBRARY            *")
        print("\t\t\t     *       ------------------------       *")
        print("\t\t\t     *                                      *")
        print("\t\t\t     *                                      *")
        print("\t\t\t     *       Mumbai,Maharashtra,India       *")
        print("\t\t\t     *     Email: studentlib@gmail.com      *")
        print("\t\t\t     *     Contact:8800991010,8800992020    *")
        print("\t\t\t     *                                      *")
        print("\t\t\t     ****************************************")
        print("\n\n\t\t\t             Press any key to continue: ")
        input()

    def main_menu(self):
        while True:
            print("\n\n")
            print("\n\t\t\t*\n")
            print("\n\t\t\t\t      MAIN MENU: ")
            print("\n\t\t\t\t     1.ISSUE OF BOOKS ")
            print("\n\t\t\t\t     2.RETURN OF BOOKS ")
            print("\n\t\t\t\t     3.DISPLAY STUDENT DETAILS ")
            print("\n\t\t\t\t     4.EXIT\n ")
            print("\n\t\t\t*\n")
            choice = int(input("\n\t\t\t\t      Enter your choice: "))
            if choice == 1:
                self.book_issue()
            elif choice == 2:
                self.book_return()
            elif choice == 3:
                self.display()
            elif choice == 4:
                break
            else:
                print("\n\t\t\t\t      ...Invalid Option!...")

if __name__ == "__main__":
    library = Library()
    library.initialize_lib()
    library.greetings()
    library.main_menu()

