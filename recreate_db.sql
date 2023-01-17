CREATE SCHEMA sql_login;

USE sql_login;

CREATE TABLE users (
	id int(11) AUTO_INCREMENT PRIMARY KEY,
	username varchar(100) NOT NULL,
    	email varchar(100) NOT NULL,
	password text NOT NULL,
    	first_name varchar(100) NOT NULL,
    	last_name varchar(100) NOT NULL
);
