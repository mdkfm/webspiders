import pymysql

def save_data():
	db = pymysql.connect(host='localhost', user='skf', password='123456')
	cursor = db.cursor()
	name = '11'
	drama = '11'
	sql = f'INSERT INTO spiders.spa1 VALUES({name}, {drama})'
	try :
		if cursor.execute(sql):
			db.commit()
			logging.info('data saved successfully')
	except:
		db.rollback()
	db.close()

save_data()
