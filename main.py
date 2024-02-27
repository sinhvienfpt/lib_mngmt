# Simple library management system
import library
import pandas as pd
from random import randint

def print_menu():
    print("Please select an option:")
    print("1. Insert a book")
    print("2. Delete a book")
    print("3. Display all books")
    print("4. Search a book by ID")
    print("5. Search a book by author")
    print("Other. Exit the system")
    
    
# Read the df from the file, import default 200 books
df = pd.read_csv('./twohundred_books.csv')
mylib= library.LibraryManagement()  # Create a library management object
index = set()
for i in range(len(df)):
    newindex = randint(0,1000) # Generate a random index
    while newindex in index:
        newindex = randint(0,1000)
    mylib.insert(newindex,(df['title'][i],df['author'][i],df['year'][i]))
    index.add(newindex)




# Main loop
print("Welcome to the Library Management System")
while True:
    print_menu()    
    input_ = input("Enter your choice: ")
    
    
    # Insert a book
    if input_ == '1':
        book_id = int(input("Enter the book ID: "))
        while book_id in index:
            print("This book ID already exists, please enter a new one")
            book_id = int(input("Enter the book ID: "))
        title = input("Enter the title: ")
        author = input("Enter the author: ")
        year = int(input("Enter the year: "))
        mylib.insert(book_id, (title, author, year))
        index.add(book_id)
    
    # Delete a book
    elif input_ == '2':
        book_id = int(input("Enter the book ID: "))
        if book_id not in index:
            print("This book ID does not exist")
            continue
        else:
            mylib.delete(book_id)
            index.remove(book_id)
            print(f"The book with ID {book_id} deleted successfully")
        
    # Display all books
    elif input_ == '3':
        mylib.display()
        
    # Search a book by ID
    elif input_ == '4':
        if book_id not in index:
            print("This book ID does not exist")
        book_id = int(input("Enter the book ID: "))
        mylib.searchbyid(book_id)
        
    # Search a book by author
    elif input_ == '5':
        author = input("Please enter the author's full name or part of his name: ")
        mylib.searchbyauthor(author)
        
    # Exit the system
    else:
        print("Thank you for using the Library Management System")
        break
