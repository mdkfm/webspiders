import pymysql

db = pymysql.connect(host='localhost', user='skf', password='123456')
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database version:', data)
cursor.execute("CREATE DATABASE IF NOT EXISTS spiders DEFAULT CHARACTER SET utf8mb4")
db.close()
		
