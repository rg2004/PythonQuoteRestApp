import cx_Oracle
# Connect as user "hr" with password "welcome" to the "oraclepdb" service running on this computer.
connection = cx_Oracle.connect("system", "system", "localhost/xe")

cursor = connection.cursor()

querystring = "select * from employees"

cursor.execute(querystring)
for row in cursor:
    print("Values:", row)
