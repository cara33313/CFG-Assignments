from contextlib import nullcontext

import requests
import json


def get_available_books():
    result = requests.get('http://127.0.0.1:5001/books_available', headers={'content-type': 'application/json'})
    return result.json()

def borrow_book(book_name, first_name, last_name):
    book = {
        'book_name':book_name,
        'first_name':first_name,
        'last_name':last_name
    }
    result=requests.put(
        'http:127.0.0.1:5001/borrow_book',
        headers={'content-type': 'application/json'},
        data = json.dumps(book)
    )
    return result.json()

# Fomatting book names nicely
def display_books(books):
    # Print the names of the columns.
    print("{:<15}".format(
        'Book Names'))
    print('-' * 30)

    # print each data item.
    # sort out printing value 'none' at end
    for item in books:
        print("{:<15} ".format(
            item[0]
        ))
        print('-' * 30)


def run():
    print('############################')
    print('Hello, welcome to the library')
    print('############################')
    print()

    # ONLY DISPLAYS BOOKS WHICH ARE NOT CURRENTLY BORROWED BY OTHER PEOPLE
    book = input('Would you like to view all the books you can borrow?: ')
    print()
    available_book_name = get_available_books()
    print(display_books(available_book_name))



if __name__ == '__main__':
    run()
