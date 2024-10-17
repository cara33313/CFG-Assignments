import mysql.connector
from config import HOST, USER, PASSWORD


class DbConnectionError(Exception):
    pass

def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx


def get_available_books():
    book_names = []
    try:
        db_name = 'library_system'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f"Connected successfully to {db_name}")

        statement = """
        SELECT book_title, book_out FROM books;
        """


        cur.execute(statement)
        result = cur.fetchall()
        book_names = result
        cur.close()

    except Exception:
        raise DbConnectionError('Failed to read any data')

    finally:
        if db_connection:
            db_connection.close()
            print('Database connection closed')

    return book_names


def borrow_book(book_name, first_name, last_name):

    try:
        db_name = 'library_system'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f"Connected successfully to {db_name}")



        statement = """
            CALL borrow_book('{first_name}', '{last_name}', '{book_name}');
        """.format(first_name=first_name, last_name=last_name, book_name=book_name)

        cur.execute(statement)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError('Failed to read any data')

    finally:
        if db_connection:
            db_connection.close()
            print('Database connection closed')

# Get borrow history of a book
def borrow_history(book_name):
    borrow_history_list = []
    try:
        db_name = 'library_system'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f"Connected successfully to {db_name}")

        statement = """
            SELECT 
            book_title, first_name, last_name, date_borrowed, returned
            FROM 
            books_borrowed 
            WHERE 
            book_title = '{}'
        """.format(book_name)

        cur.execute(statement)
        result = cur.fetchall()
        borrow_history_list = result
        cur.close()

    except Exception:
        raise DbConnectionError('Failed to read any data')

    finally:
        if db_connection:
            db_connection.close()
            print('Database connection closed')

    return borrow_history_list


def return_book(book_name):
    try:
        db_name = 'library_system'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f"Connected successfully to {db_name}")

        statement = """
        UPDATE books_borrowed, books 
        SET books_borrowed.returned = 1,
            books.book_out = 0
        WHERE books_borrowed.book_title='{book_name}' 
        AND books.book_title='{book_name}'
        """.format(book_name=book_name)

        cur.execute(statement)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError('Failed to read any data')

    finally:
        if db_connection:
            db_connection.close()
            print('Database connection closed')


