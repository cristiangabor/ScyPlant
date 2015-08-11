import sqlite3
import os.path
from os import listdir, getcwd




def create_table(db_name,table_name,sql):
	with sqlite3.connect(db_name) as db:
		cursor=db.cursor()
		cursor.execute('PRAGMA foreign_keys=ON')
		cursor.execute("select name from sqlite_master where name=?",(table_name,))
		result=cursor.fetchall()
		kepp_table=True
		if len(result) == 1:
			response = raw_input("The table {0} alerady exists, do yoy wish to recreate it (y/n):".format(table_name))
			if response=='y':
				kepp_table=False
				print 'The {0} table will be recreated- all existing data will be lost'.format(table_name)
				cursor.execute('drop table if exists {0}'.format(table_name))
				db.commit()
			else:
				print "The existing table was kept"
		else:
			kepp_table=False
		if not kepp_table:		
			cursor.execute(sql)
			db.commit()

def create_table_for_doc(db_name):
	
	sql='''CREATE TABLE IF NOT exists INFORMATION(
			ID INTEGER,
			Popular text,
			Stiintific text,
			Importanta text,
			Descriere text,
			Poza blob,
			primary key(ID))'''

	create_table(db_name,'INFORMATION',sql)


def main():
	create_table_for_doc('poze.db')
#main()



def insert_text(popular,stiintific,importanta,descriere,poza):
		#print poza
		with sqlite3.connect('poze.db') as db:
			cursor=db.cursor()
			data=(popular,stiintific,importanta,descriere,sqlite3.Binary(poza))
			sql="INSERT INTO INFORMATION(Popular,Stiintific,Importanta,Descriere,Poza) values (?,?,?,?,?)"
			cursor.execute(sql,data)
			db.commit()

