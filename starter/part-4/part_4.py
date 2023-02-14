### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here
# def create_book():
#   title = input('What is the title of the book you would like to add? -')
#   author = input('Who is the author of the book you would like to add? -' )
#   try:
#     year = int(input('What year was this book published? - '))
#   except:
#     year = int(input('Please type a number for the year'))
#   rating = float(input('What rating out of 5 would you give this book? - '))
#   pages = int(input('What is the page count of the book? - '))

#   return {
#     'title': title,
#     'author': author,
#     'year': year,
#     'rating': rating,
#     'pages': pages
#   }

# print(create_book())

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here



### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

def create_new_book():
  title = input('\nWhat is the title of the book you would like to add? - ')
  author = input('Who is the author of the book you would like to add? - ')
  try:
    year = int(input('What year was this book published? - '))
  except:
    year = int(input('Please type a number - '))
  try:
    rating = float(input("What rating out of 5 would you give this book? - "))
  except:
    rating = int(input("Please type a number? - "))
  try:
    pages = int(input("What is the page count of the book? - "))
  except:
    pages = int(input("Please type a number? - "))
  
  book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }
    
  return book_dictionary

### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here


### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

current_books = [
  {
    "title": "A Game of Thrones",
    "author": "George RR Martin",
    "year": 1996,
    "rating": 4.5,
    "pages": 694
  },
  {
    "title": "The Lord of the Rings",
    "author": "J. R. R. Tolkien",
    "year": 1954,
    "rating": 4.0,
    "pages": 1178
  },
  {
    "title": "Percy Jackson and the Lightning Thief",
    "author": "Rick Riordan",
    "year": 2005,
    "rating": 3.5,
    "pages": 375
  },
  {
    "title": "The Way of Kings",
    "author": "Brandon Sanderson",
    "year": 2010,
    "rating": 4.0,
    "pages": 1007
  }
]

def print_all_books(list_of_books):
  print('\nHere are all your books...\n')
  
  for book in list_of_books:
    title = book["title"]
    author = book["author"]
    year = book["year"]
    rating = book["rating"]
    pages = book["pages"]

    print(f"Title: {title}, Author: {author}, Year: {year}, Rating: {rating}, Pages: {pages}")

def main_menu(books_source):

  active = True

  while active:
    choice = input('''
    Choose 1 to add a book
    Choose 2 to see all your books
    Choose 3 to see a count of your books
    choose 4 to see a count of the pages of your books
    choose 5 to exit

    Type Here:
    ''')
  
    if choice == "1":
      books_source.append(create_new_book())
    elif choice == "2":
      print_all_books(books_source)
    elif choice == "3":
      print(f"\nYou have a total of {len(books_source)} books.\n")
    elif choice == "4":
      print(f"\nYou books page count totals {sum([x['pages'] for x in books_source])} pages!\n")
    elif choice == "5":
      print("\nGoodbye")
      active = False
    else:
      print("\nSorry please type a number for one of the options.\n")


main_menu(current_books)