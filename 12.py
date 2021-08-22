
import sqlite3

connect = sqlite3.connect('db') 

cur = connect.cursor()

# sql = 'INSERT INTO book ( title, publisher, author, price, ISBN, date) VALUES (?,?,?, CURRENT_TIMESTAMP);'

sql = 'insert into book ( title, author, ISBN, date) VALUES (?,?,?, CURRENT_TIMESTAMP);'

# insertData = [titleName,publisherName,AuthorName,Price,ISBN]

cur.execute('insert into book ( title, author, ISBN, date) VALUES ("titleName","AuthorName","ISBN", CURRENT_TIMESTAMP);')
connect.commit()
connect.close()