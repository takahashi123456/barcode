import requests as req

#import chromedriver_binary
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options # オプションを使うために必要


if __name__ == '__main__':
        url = "https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404?format=json&isbn={}&applicationId=1034070708300315308" #最後の日付はapiのバージョンっぽい
        app_id  = "1034070708300315308" #自分のapp_idを入力
        #isbn    = "9784274206504" #ベタうちならこんな感じ

        # login処理
        option = Options()                          # オプションを用意
        #option.add_argument('--headless')          # ヘッドレスの設定を付与
        driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver',options=option)   # Chromeを準備(optionでヘッドレスモードにしている）
        
        # driver = webdriver.Chrome()   # Chromeを準備(optionでヘッドレスモードにしていないバージョン）
        driver.get('http://34.239.157.242/index.php/login')
        time.sleep(2)
        login_box = driver.find_element_by_id('email')
        login_box.send_keys('aaa@aa')
        pass_box = driver.find_element_by_id('password')
        pass_box.send_keys('test1234')
        sub_box = driver.find_element_by_class_name('btn-primary')
        sub_box.submit()
        time.sleep(2)
        

        print("please input isbn code!:")
        while(True):
                driver.get('http://34.239.157.242/index.php/nankore/collection/create')
                isbn    = input() #つないだ状態でピッするならこっち
                url1 = url.format(isbn)
                res = req.get(url1)
                data = res.json()
                data2 = data["Items"]
                title = data["Items"][0]["Item"]["title"]
                author = data["Items"][0]["Item"]["author"]
                isbn = data["Items"][0]["Item"]["isbn"]
                print(title)
                print(author)
                print(isbn)

                time.sleep(2)
                login_box = driver.find_element_by_id('title')
                login_box.send_keys(title)
                pass_box = driver.find_element_by_id('author')
                pass_box.send_keys(author)
                pass_box = driver.find_element_by_id('isbn')
                pass_box.send_keys(isbn)
                sub_box = driver.find_element_by_class_name('btn-primary')
                sub_box.submit()
                time.sleep(2)
