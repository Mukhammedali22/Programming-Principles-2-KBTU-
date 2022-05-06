CREATE OR REPLACE PROCEDURE insert_user(
    user_first_name VARCHAR(255), 
    user_last_name VARCHAR(255),
    user_phone VARCHAR(255)
) AS $$
BEGIN
	INSERT INTO phonebook(first_name, last_name, phone) 
	VALUES(user_first_name, user_last_name, user_phone);
END;
$$
LANGUAGE plpgsql;