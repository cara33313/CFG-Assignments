from flask import Flask, jsonify, request
from db_utils import get_available_books, borrow_book, return_book, borrow_history

app = Flask(__name__)

# get book names
@app.route('/books_available', methods=['GET'])
def get_book_names():
    res = get_available_books()
    return jsonify(res)

# borrow a book
@app.route('/borrow_book', methods=['POST'])
def user_borrow_book():
    book = request.get_json()
    print(book['book_name'])
    print(book['first_name'])
    print(book['last_name'])
    borrow_book(
        book_name=book['book_name'],
        first_name=book['first_name'],
        last_name=book['last_name']
    )
    return book

# return a book
@app.route('/return_book', methods=['PUT'])
def book_return():
    returned_book = request.get_json()
    return_book(
        book_name=returned_book['book_name']
    )
    return returned_book

# view the borrow history for a book
@app.route('/borrow_history/<book_name>', methods=['GET'])
def view_borrow_history(book_name):
    res = borrow_history(book_name)
    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True, port=5001)