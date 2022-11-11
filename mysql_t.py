import pymysql

def create_database():
	db = pymysql.connect(host='localhost', user='skf', password='123456')
	cursor = db.cursor()
	cursor.execute('SELECT VERSION()')
	data = cursor.fetchone()
	print('Database version:', data)
	cursor.execute("CREATE DATABASE IF NOT EXISTS spiders DEFAULT CHARACTER SET utf8mb4")
	db.close()

def insert_into(data:'dict', table:'str'):
	db = pymysql.connect(host='localhost', user='skf', password='123456')
	cursor = db.cursor()
	keys = ', '.join(data.keys())
	values = ', '.join(['%s'] * len(data))
	sql = f'INSERT INTO {table}({keys}) VALUES ({values})'
	try :
		if cursor.execute(sql, tuple(data.values())):
			print('Successful')
			db.commit()
	except:
		print('Failed')
		db.rollback()
	db.close()

def insert_or_update(data:'dict', table:'str'):
	db = pymysql.connect(host='localhost', user='skf', password='123456')
	cursor = db.cursor()
	keys = ', '.join(data.keys())
	values = ', '.join(['%s'] * len(data))
	sql = f'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'
	update = ', '.join([f"{key} = %ss" for key in data])
	sql += update
	try:
		if cursor.execute(sql, tuple(data.values()) * 2):
			print('Successful')
			db.commit()
	except:
		print('Failed')
		db.rollback()
	db.close()
	
def delete(table, condition):
	db = pymysql.connect(host='localhost', user='skf', password='123456')
	cursor = db.cursor()
	sql = f'DELETE FROM {table} WHERE {condition}'
	try:
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()
	db.close()

def select_obo(sql):
	try:
		db = pymysql.connect(host='localhost', user='skf', password='123456')
		cursor = db.cursor()
		cursor.execute(sql)
		print('Count:', cursor.rowcount)
		row = cursor.fetchone()
		while row:
			print('Row:', row)
			row = cursor.fetchone()
	except:
		print('Error')
		
