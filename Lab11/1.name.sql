CREATE OR REPLACE FUNCTION username()
  RETURNS TABLE(first_name VARCHAR(255), last_name VARCHAR(255)) AS
$$
BEGIN
 RETURN QUERY

 SELECT first_name, last_name
 FROM phonebook;

END; $$

LANGUAGE plpgsql;