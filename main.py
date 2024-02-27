#Simple library management system
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

mylib= library.LibraryManagement()  #Create a library management object
index = set()
for i in range(len(df)):
    newindex = randint(0,1000) #Generate a random index
    while newindex in index:
        newindex = randint(0,1000)
    mylib.insert(newindex,(df['title'][i],df['author'][i],df['year'][i]))
    index.add(newindex)

# Main loop
print("Welcome to the Library Management System")
while True:
    print_menu()    
    input_ = input("Enter your choice: ")
    if input_ == '1':
        book_id = int(input("Enter the book ID: "))
        while book_id in index:
            print("This book ID already exists, please enter a new one")
            book_id = int(input("Enter the book ID: "))
        title = input("Enter the title: ")
        author = input("Enter the author: ")
        year = int(input("Enter the year: "))
        mylib.insert(book_id, (title, author, year))
    elif input_ == '2':
        book_id = int(input("Enter the book ID: "))
        mylib.delete(book_id)
    elif input_ == '3':
        mylib.display()
    elif input_ == '4':
        book_id = int(input("Enter the book ID: "))
        mylib.searchbyid(book_id)
    elif input_ == '5':
        author = input("Enter the author: ")
        mylib.searchbyauthor(author)
    else:
        print("Thank you for using the Library Management System")
        break