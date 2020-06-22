import mysql.connector

cnx = mysql.connector.connect(host='localhost',
                              username='root',
                              database='sql-antipatterns')

cursor = cnx.cursor()
cursor.execute('Show tables')
tables = cursor.fetchall()
print(tables[0:])

