CREATE DATABASE library_system;
USE library_system;


CREATE TABLE books (
	bookID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    book_title VARCHAR(100) NOT NULL, 
	book_out BOOL NOT NULL
    );
    
CREATE TABLE books_borrowed (
	transactionID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL, 
    bookID INT NOT NULL,
    book_title VARCHAR(100) NOT NULL,
    date_borrowed DATE NOT NULL,
    due_date DATE NOT NULL,
    returned BOOL NOT NULL,
    FOREIGN KEY (bookID) REFERENCES books(bookID)
    );
    
INSERT INTO books (book_title, book_out) VALUES 
	('Little Women', FALSE),
    ('Pride And Prejudice', FALSE),
    ('The Great Gatsby', FALSE),
    ('Dracula', FALSE),
    ('Wuthering Heights', FALSE),
    ('Frankenstein', FALSE),
    ('Jane Eyre', FALSE),
    ('To Kill A Mockingbird', FALSE),
    ('Emma', FALSE),
    ('Sense And Sensibility', FALSE),
    ('The Picture Of Dorian Grey', FALSE),
    ('Crime And Punishment', FALSE),
    ('One Hundred Years Of Solitude', FALSE),
    ('Animal Farm', FALSE),
    ('The Catcher In The Rye', FALSE),
    ('Of Mice And Men', FALSE),
    ('Don Quixote', FALSE);

DELIMITER $$

CREATE PROCEDURE borrow_book
	(first_name_insert VARCHAR(100), last_name_insert VARCHAR(100), book_title_insert VARCHAR(100))

BEGIN 

DECLARE date DATE;
DECLARE dueDate DATE;

SET SQL_SAFE_UPDATES = 0;
SET date = (SELECT CURDATE());
SET dueDate = (ADDDATE(date, INTERVAL 30 DAY));

    
	INSERT INTO books_borrowed 
    (first_name, last_name, bookID, book_title, date_borrowed, due_date, returned) 
    VALUES(first_name_insert, last_name_insert, (SELECT bookID FROM books b WHERE b.book_title = book_title_insert), book_title_insert, date, dueDate, FALSE);
        
	UPDATE books b
		SET book_out = TRUE 
		WHERE b.book_title = book_title_insert;

SET SQL_SAFE_UPDATES = 1;
END $$
DELIMITER ;





