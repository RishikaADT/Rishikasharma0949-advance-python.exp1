class Book:
    def _init_(self,title ,author):
     self.title=title 
     self.author=author
     self.available=True #Book is available by default


class Patron:
     def _init_(self,name):
      self.name= name
      self.borrowed_books=[] #list to store borrowed books


class Library:
     def _init_(self):
      self.books=[]
      self.patrons=[]

     def add_book(self, book):
      self.books.append(book) # Add book to library

     def register_patron(self,patron):
        self.patron.append(patron) # Register a new patron

     def borrow_book(self,patron,book):   
      if book. available:
         book.available =False
         patron.borrowed_books.append(book)  

     def return_book(self,patron,book):
       if book in patron.borrowed_books:
         book.available=True
         patron.borrowed_books.remove(book)
         print(f"{patron.name} returned {book.title}.")
       else:
            print(f"{patron.name} does not have {book.title}.")

         # --- Demonstration of the System ---
       if _name_ == "_main_":
         
    # Initialize Library
         my_library = Library()

    # Create Books and Patrons
         book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
         book2 = Book("1984", "George Orwell")
         patron1 = Patron("Alice")

    # Perform Operations
       my_library.add_book(book1)
       my_library.add_book(book2)
       my_library.register_patron(patron1)

       print("\n--- Borrowing Process ---")
       my_library.borrow_book(patron1, book1)

       print("\n--- Returning Process ---")
       my_library.return_book(patron1, book1)
       

