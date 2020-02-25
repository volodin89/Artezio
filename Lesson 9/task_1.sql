CREATE DATABASE IF NOT EXISTS company;
USE company;
CREATE TABLE IF NOT EXISTS staff (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT primary key,
	first_name VARCHAR(30) NOT NULL,
	last_name VARCHAR(30) NOT NULL,
	post VARCHAR(30) NOT NULL,
	salary INT UNSIGNED NOT NULL
);
INSERT INTO staff (id, first_name, last_name, post, salary) VALUES (null, 'Robert', 'Downey', 'Director', 70000);
INSERT INTO staff (id, first_name, last_name, post, salary) VALUES (null, 'Antonio', 'Banderas', 'Manager', 40000);
INSERT INTO staff (id, first_name, last_name, post, salary) VALUES (null, 'Michael', 'Sheen', 'Designer', 30000);
INSERT INTO staff (id, first_name, last_name, post, salary) VALUES (null, 'Jim', 'Broadbent', 'Designer', 25000);
INSERT INTO staff (id, first_name, last_name, post, salary) VALUES (null, 'Jessie', 'Buckley', 'Courrier', 15000);
