import sqlite3

#それぞれの変数に入れてあげるとsqlに挿入される
def SQLInsert(titleName,AuthorName,ISBN): 

	connect = sqlite3.connect('db.sqlite3') 

	cur = connect.cursor()
	
	# sql = 'INSERT INTO book ( title, publisher, author, price, ISBN, date) VALUES (?,?,?, CURRENT_TIMESTAMP);'

	sql = 'insert into book ( title, author, ISBN, date) VALUES (?,?,?, CURRENT_TIMESTAMP);'

	insertData = [titleName,AuthorName,ISBN]
	# insertData = [titleName,publisherName,AuthorName,Price,ISBN]

	cur.execute(sql,insertData)
	connect.commit()
	connect.close()



SQLInsert("testName","testPub","testAuthor")