#coding:utf-8
import sqlite3
import requests as req
from sqlinsert import SQLInsert


if __name__ == '__main__':
        url = "https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404?format=json&isbn={}&applicationId=1034070708300315308" #最後の日付はapiのバージョンっぽい
        app_id  = "1034070708300315308" #自分のapp_idを入力
        #isbn    = "9784274206504" #ベタうちならこんな感じ
        print(url)
        print("please input isbn code!:")
        while(True):
                isbn    = input() #つないだ状態でピッするならこっち
                url1 = url.format(isbn)
                if(isbn == "p"):
                        conn = sqlite3.connect('db')
                        cur = conn.cursor()
                        cur.execute('SELECT * FROM book')
# 中身を全て取得するfetchall()を使って、printする。
                        print(cur.fetchall())
                if(isbn == "c"):
                        break
                else:
                       	res = req.get(url1)
                        data = res.json()
                        data2 = data["Items"]
                #titleなど
                        title = data["Items"][0]["Item"]["title"]
                        author = data["Items"][0]["Item"]["author"]
                        isbn = data["Items"][0]["Item"]["isbn"]

                #一応ターミナルに表示してあげる
                        print(title)
                        print(author)
                        print(isbn)

                #SQLに挿入
                        SQLInsert(title, author, isbn)

