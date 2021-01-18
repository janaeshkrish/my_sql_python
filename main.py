import mysql.connector as sql

connection = sql.connect(host='localhost',user = 'janaesh',password ='12345',database ='janaeshwar')

print(connection)

cursor = connection.cursor()

#cursor.execute('CREATE DATABASE janaeshwar')

cursor.execute('CREATE TABLE table1 (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255))')
#cursor.execute('SHOW DATABASES')


'''
for x in cursor:

    print(x)
'''

query = "INSERT INTO table1 (name) VALUES (%s)"
value = ('john')
cursor.execute(query,value)