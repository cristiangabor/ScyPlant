#search.py
import sqlite3

def search_plant(name):
	with sqlite3.connect('poze.db') as db:
		cursor=db.cursor()
		data=(name.title(),)
		sql="SELECT * FROM INFORMATION WHERE Popular=?"
		cursor.execute(sql,data)
		product=cursor.fetchall()
		db.commit()
		return product

