from contextlib import nullcontext

import requests
import json


def get_available_books():
    result = requests.get('http://127.0.0.1:5001/books_available',
                          headers={'content-type': 'application/json'}
                          )
    return result.json()

def borrow_book(book_name, first_name, last_name):
    book = {
        'book_name':book_name,
        'first_name':first_name,
        'last_name':last_name
    }
    result = requests.post(
        'http://127.0.0.1:5001/borrow_book',
        headers={'content-type': 'application/json'},
        data = json.dumps(book)
    )
    return result.json()

def return_book(book_name):
    returned_book = {
        'book_name': book_name
    }
    result = requests.put(
        'http://127.0.0.1:5001/return_book',
        headers = {'content-type': 'application/json'},
        data = json.dumps(returned_book)
    )
    return result.json()

def borrow_history(book_name):
    result = requests.get(
        f'http://127.0.0.1:5001/borrow_history/{book_name}',
        headers = {'content-type': 'application/json'}
    )
    return result.json()

# lists all the books not checked out from the library
def book_list(available_book_names):
    book_list = []
    for item in available_book_names:
        if item[1] == 0:
            book_list.append(item[0])
    return book_list

# lists all the books checked out from the library
def checked_out_books(available_book_names):
    checked_out_book_list = []
    for item in available_book_names:
        if item[1] == 1:
            checked_out_book_list.append(item[0])
    return checked_out_book_list

# formats the book list nicely
def display_books(books):
    # Print the names of the columns.
    print("{:<30} {:<30}".format(
        'Book Names', 'Available?'))
    print('-' * 44)


    for item in books:
        if item[1] == 0:
            available = 'Available'
        elif item[1] == 1:
            available = 'Not Available'

        print("{:<30} {:<30}".format(
            item[0], available))
        print('-' * 44)

# formats the borrow history of a book nicely
def display_history(books):
    print("{:<30} {:<30} {:<30} {:<30} {:<30}".format(
        'Book Name', 'First Name', 'Last Name', 'Date Borrowed', 'Returned?'))
    print('-' * 150)

    for item in books:
        if item[4] == 0:
            available = 'No'
        elif item[4] == 1:
            available = 'Yes'

        print("{:<30} {:<30} {:<30} {:<30} {:<30}".format(
            item[0], item[1], item[2], item[3], available))
        print('-' * 150)

def run():

    # function used whenever user is prompted to enter a book name
    def get_book_name():
        book_name_choice = input('Enter the name of the book you would like to borrow: ').title()
        return book_name_choice


    print('############################')
    print('Hello, welcome to the library')
    print('############################')
    print()

    book = input('Here are all the book available to borrow at our library, type anything to view all the books we have available: ')
    print()
    available_book_name = get_available_books()
    print(display_books(available_book_name))
    book_names_list = book_list(available_book_name)
    checked_out_books_list = checked_out_books(available_book_name)

    # choice of what action to take
    book_action = input('What would you like to do, type B to borrow a book, R to return a book or H to see the borrow history of a book: ').upper()

    borrow_choice = book_action == 'B'
    return_book_choice = book_action == 'R'
    history_choice = book_action == 'H'

    # used in while loop to keep prompting user to enter book if they are not entering one belonging to the library which is not checked out
    while borrow_choice:
        book_name = get_book_name()

        if book_name in book_names_list:
            first_name = input('Please enter your first name: ').title()
            last_name = input('Please enter your last name: ').title()
            borrow_book(book_name=book_name, first_name=first_name, last_name=last_name)
            print()
            print('You have successfully borrowed this book, to check the due date, return to the start of the process'
                    'and check the borrow history of the book')
            break

        elif book_name not in book_names_list:
            print('This book is not available to borrow at this library, please try again')

    # used in while loop to keep prompting user to enter book if they are not entering one belonging to the library which is checked out
    while return_book_choice:
        book_name = get_book_name()

        if book_name in checked_out_books_list:
            return_book(book_name=book_name)
            print('You have successfully returned this book')
            break

        elif book_name not in checked_out_books_list:
            print('This book is not currently checked out of this library, please try again')

    # used in while loop to keep prompting user to enter book if they are not entering one which belongs to the library
    while history_choice:
        book_title = get_book_name()

        if book_title in book_names_list:
            history = borrow_history(book_title)
            print(display_history(history))

        if book_title in checked_out_books_list:
            history = borrow_history(book_title)
            print(display_history(history))

        elif book_title not in book_names_list or checked_out_books_list:
            print('This book is not available to borrow at this library, please try again')



if __name__ == '__main__':
    run()
