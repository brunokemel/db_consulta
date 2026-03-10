python -m venv venv
venv\Scripts\activate
 Py 3.12.2


 Agora criamos banco de dados usando programação de banco de dados em Python
<!-- import mysql.connector
    db_connection = mysql.connector.connect(
    host= "localhost",
    user= "root",
    passwd= "root"
    )
# creating database_cursor to perform SQL operation
db_cursor = db_connection.cursor()
# executing cursor with execute method and pass SQL query
db_cursor.execute("CREATE DATABASE my_first_db")
# get list of all databases
db_cursor.execute("SHOW DATABASES")
#print all databases
for db in db_cursor:
	print(db) -->


Precisa comparar os processo pra NULL e FAIL já que ele apenas considera IDs na hora do check,