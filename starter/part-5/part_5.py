### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here



def create_new_book(book_source):
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
    
  with open(book_source, 'a') as f:
    f.write(f"{title}, {author}, {year}, {rating}, {pages}\n")

# create_new_book()
### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here
def get_books_as_list_of_dictionaries(book_source):
  books_list = []
  with open(book_source, 'r') as f:
    file = f.readlines()

    for line in file:
      title, author, year, rating, pages = line.split(',')

      books_list.append({
        "title": title,
        "author": author,
        "year": int(year),
        "rating": float(rating),
        "pages": int(pages)
        })
  return books_list
        
def get_book_printed(book):
  print(f"Title: {book['title']}, Author {book['author']}, Year: {book['year']}, Rating: {book['rating']}, Pages: {book['pages']}")

def view_books(book_source):
  print('\nHere are all your books... \n')
  for book in get_books_as_list_of_dictionaries(book_source):
    get_book_printed(book)

def get_highest_rated_book(book_source):
    list = get_books_as_list_of_dictionaries(book_source)
    return max(list, key=lambda x: float(x["rating"]))

def get_lowest_rated_book(book_source):
    list = get_books_as_list_of_dictionaries(book_source)
    return min(list, key=lambda x: float(x["rating"]))

def get_sorted_list_by_rating(book_source):
    print("\nHere are all your books ranked by rating...\n")
    list = get_books_as_list_of_dictionaries(book_source)
    list =  sorted(list, key=lambda x: int(x["rating"]), reverse = True)
    for book in list:
        get_book_printed(book)

### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script

def main_menu(book_source):

  active = True

  while active:
    choice = input('''
    Choose 1 to add a book...
    Choose 2 to see all your books...
    Choose 3 to see a count of your books...
    Choose 4 to see a count of the pages of your books...
    Choose 5 to see your highest rated book...
    Choose 6 to see your lowest rated book...
    Choose 7 to see your books ranked by order of rating...
    Choose 0 to exit.

    Type Here:
    ''')
  
    if choice == "1":
      create_new_book(book_source)
    elif choice == "2":
      view_books(book_source)
    elif choice == "3":
      print(f"\nYou have a total of {len(get_books_as_list_of_dictionaries(book_source))} books.\n")
    elif choice == "4":
      print(f"\nYou books page count totals {sum([x['pages'] for x in get_books_as_list_of_dictionaries(book_source)])} pages!\n")
    elif choice == '5':
      print('\n Here is your highest rated book...\n')
      get_book_printed(get_highest_rated_book(book_source))
    elif choice == '6':
      print('\n Here is your lowest rated book...\n')
      get_book_printed(get_lowest_rated_book(book_source))
    elif choice == '7':
      get_sorted_list_by_rating(book_source)
    elif choice == '0':
      print("\nGoodbye")
      active = False
    else:
      print("\nSorry please type a number for one of the options.\n")

if __name__ == '__main__':
  main_menu('library.txt')

### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

