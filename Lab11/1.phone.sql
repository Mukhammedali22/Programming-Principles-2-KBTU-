CREATE OR REPLACE FUNCTION phone()
  RETURNS TABLE(user_phone VARCHAR(255)) AS
$$
BEGIN
 RETURN QUERY

 SELECT phone
 FROM users;

END; $$

LANGUAGE plpgsql;