import pandas as pd

# Read the df from the file
df = pd.read_csv('Books.csv')
df = df[:200]  # Limiting the df to 200 rows
df = df[["Book-Title", "Book-Author", "Year-Of-Publication"]]  # Get title, author and year of publication

#Rename the columns
df.rename(
    columns={"Book-Title": "title", 
             "Book-Author": "author", 
             "Year-Of-Publication": "year"}, 
            inplace=True)  # Rename the columns


#Save the df to a new file
df.to_csv('twohundred_books.csv', index=False)