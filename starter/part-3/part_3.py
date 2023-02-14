my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below

def book_parser(bd):
    return f"{bd['title']} was written by {bd['author']} in the year {bd['year']}. It received a rating of {bd['rating']} and was {bd['pages']} pages long"
print(book_parser(my_book))

# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below

def my_book_keys(bd):
    return bd.keys()
print(my_book_keys(my_book))

def my_book_values(bd):
    return bd.values()
print(my_book_values(my_book))

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

