#coding:utf-8
import requests as req

if __name__ == '__main__':
        url = "https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404?format=json&isbn={}&applicationId=1034070708300315308" #最後の日付はapiのバージョンっぽい
        app_id  = "1034070708300315308" #自分のapp_idを入力
        #isbn    = "9784274206504" #ベタうちならこんな感じ
        print(url)
        print("please input isbn code!:")
        while(True):
                isbn    = input() #つないだ状態でピッするならこっち
                url1 = url.format(isbn)
 # payload = {
#     'format':'json',
#         'isbn':isbn,
#     'applicationId':app_id
#         }
                res = req.get(url1)
                data = res.json()
                data2 = data["Items"]

                #titleなど
                title = data["Items"][0]["Item"]["title"]
                author = data["Items"][0]["Item"]["author"]
                isbn = data["Items"][0]["Item"]["isbn"]


                # print(data)
                # print(type(data))
                # print(data2)
                # print('title' in data2[0]["Item"])#成功
                # print(data2[0]["Item"]["title"])
                print(title)
                print(author)
                print(isbn)

                
                # print(data["page"])

# print(url1)
                if(isbn == "c"):
                        break	
