DROP TABLE IF EXISTS USERS;

CREATE TABLE USERS (
    user_name TEXT, 
    user_tel TEXT, 
    user_addr TEXT,
    user_email TEXT primary key, 
    user_status TEXT
);