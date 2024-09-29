-- CREATE DATABASE film_tracker;
-- USE film_tracker;

-- -- Creating three tables 
-- CREATE TABLE films (
-- 	film_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
--     film_name VARCHAR(100),
--     release_year YEAR,
--     genre VARCHAR(100),
--     watches INT, 
--     likes INT
--     );
--     
-- CREATE TABLE users (
-- 	user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
--     user_name VARCHAR(100),
--     user_email VARCHAR(100) UNIQUE
--     ); add unique variable to email?

-- CREATE TABLE films_watched (
-- 	user_ID INT NOT NULL,
--     film_id INT NOT NULL,
--     FOREIGN KEY (user_ID) REFERENCES users(user_id),
--     FOREIGN KEY (film_id) REFERENCES films(film_id),
--     film_like BOOL
--     );

-- -- Populating tables with data  
-- INSERT INTO films(film_name, release_year, genre, watches, likes)
-- VALUES
--    ("The Godfather", 1972, "action", 4, 0)
--    ("Arrival", 2016, "sci-fi", 2, 0),
--    ("Ex Machina", 2014, "sci-fi", 2, 0),
--    ("Interstellar", 2014, "sci-fi", 5, 0),
--    ("Never Let Me Go", 2010, "sci-fi", 3, 0),
--    ("Citizen Kane", 1941, "action", 0, 0),
--    ("Parasite", 2019, "thriller", 10, 0),
--    ("Trainspotting", 1996, "dark comedy", 2, 0),
--    ("Sicario", 2015, "action", 0, 0),
--    ("2001: A Space Odyssey", 1968, "sci-fi", 0, 0)
-- ;

-- INSERT INTO users(user_name, user_email)
-- VALUES
--    ("Charlotte", "charlotte@gmail.com"),
--    ("Betty", "betty33@gmail.com"),
--    ("Aled", "aledw@gmail.com"),
--    ("Maddie", "maddie334@gmail.com"),
--    ("Olivia", "olivia@gmail.com"),
--    ("Sam", "sam1@gmail.com"),
--    ("Charlie", "charlie991@gmail.com"),
--    ("Charlotte", "charlotte@gmail.com"),
--    ("Poppy", "poppym@gmail.com"),
--    ("Alfie", "alfie200@gmail.com"),
--    ("Jake", "jake100@gmail.com"),
--    ("Sophie", "sophie88@gmail.com")
-- ;

-- INSERT INTO films_watched(user_id, film_id, film_like)
-- VALUES
--    (3, 2, TRUE),
--    (3, 3, TRUE),
--    (3, 10, FALSE),
--    (8, 4, FALSE),
--    (4, 2, FALSE),
--    (5, 2, TRUE),
--    (5, 4, FALSE),
--    (7, 3, FALSE),
--    (10, 2, TRUE),
--    (12, 10, FALSE),
--    (12, 6, TRUE),
--    (1, 5, TRUE),
--    (1, 9, TRUE),
--    (2, 7, TRUE),
--    (2, 8, TRUE),
--    (7, 7, TRUE),
--    (11, 9, TRUE)
-- ;

-- -- Stored procedure user to insert all relevent information when a user watches a film
-- -- Takes the email the user logged into the account with, the name of the film they watched, and wether they liked the film
-- -- Retrieves the user and film id from the user table and film table, and creates a column entry in films watched with the user_id, film_id and wether they liked the film 
-- -- Updates the film column to increase the view count for the film by 1, and if the user liked the film also increases the like count 

-- DELIMITER $$ 
-- CREATE PROCEDURE film_watched_insert
-- 	(email_address_insert VARCHAR(100), film_name_insert VARCHAR(100), like_film BOOL)
--     
-- BEGIN
--         
-- 	INSERT INTO films_watched (user_id, film_id, film_like)
--         SELECT u.user_ID, f.film_id, FALSE
--         FROM users u, films f
--         WHERE u.user_email = email_address_insert AND f.film_name = film_name_insert;
-- 	
--     SET @film_id = (
-- 		SELECT film_id 
--         FROM films 
--         WHERE film_name = film_name_insert
--         );
-- 	
--     SET @film_like = like_film;
--         
--     UPDATE films 
-- 		SET 
-- 			watches = watches + 1,
-- 			likes = CASE WHEN @film_like = TRUE THEN likes + 1 ELSE likes END
-- 		WHERE film_id = @film_id;

-- END $$

-- DELIMITER ;

-- -- Calls the film_watched_insert stored procedure with the example of betty33@gmail.com email who watched 'Sicario' and liked it
-- CALL film_watched_insert("betty33@gmail.com", "Sicario", TRUE);

-- -- Stored procedure for inserting a new user into the database, taking the user name and user email as inputs 
-- DELIMITER $$
-- CREATE PROCEDURE insert_user
-- 	(user_name_input VARCHAR(100), user_email_input VARCHAR(100))
--     
-- BEGIN
--     INSERT INTO users(user_name, user_email)
--     VALUES 
-- 		(user_name_input, user_email_input);
-- 	

-- END $$

-- DELIMITER ;

-- -- Calls the insert_user stored procedure with the example of a user called cara with an email of carae@gmail.com
-- CALL insert_user("cara", "carae@gmail.com");


-- -- When a user logs into account, selects a list of the films they have watched on that account (in this instance with the user with the email 'betty33@gmail.com'
-- SELECT f.film_name FROM films f WHERE f.film_id IN (
-- 	SELECT w.film_id FROM films_watched w WHERE w.user_id IN (
-- 		SELECT u.user_id FROM users u WHERE u.user_email = "betty33@gmail.com"
-- 		)
-- 	)
-- ORDER BY f.film_name;
--     
-- -- A more comprehensive list of films a user has watched on an account, takes in the user_id and returns the user name, the films they have watched and wether they liked them or not 
-- SELECT f.film_name, f.watches, u.user_name, w.film_like
-- FROM users u 
-- INNER JOIN films_watched w
-- ON u.user_id = w.user_id
-- INNER JOIN films f
-- ON f.film_id = w.film_id
-- WHERE u.user_id = 1
-- ORDER BY f.film_name;


-- -- Displays the most popular film on the site and returns the name, release year, and the genre (in upper case)
-- SELECT f.film_name, f.release_year, UPPER(f.genre)
-- FROM films f
-- JOIN (SELECT MAX(f.watches) AS max_watches
-- 	FROM films f) s ON s.max_watches = f.watches;

-- -- Tells you the number of films in the database
-- SELECT COUNT(film_id) FROM films;

-- -- Delete a users information
-- DELETE FROM users WHERE user_email = 'betty33@gmail.com';