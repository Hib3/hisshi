import urllib.request
import os
headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"
        }

def getURLs():
    #URLとスレタイを取得するプログラム
    subject = "https://next2ch.net/news4vip/subject.txt"
    request = urllib.request.Request(url=subject, headers=headers)
    with urllib.request.urlopen(request) as nep:#withを使うことでcloseを省略
        text = nep.read().decode('cp932')#subject.txtはcp932なので

        global url,title
        url = [f"https://next2ch.net/news4vip/dat/{line.split('<', 1)[0].strip()}" for line in text.splitlines()]#textから一行ずつに分けて、<以前にあるものを取得してきている。
        title = [f"{line.split('>', 1)[-1].strip()}" for line in text.splitlines()]#textから一行ずつに分けて、>以降にあるものを取得してきている。

    #print(url)
    #print(title)

def datfile():
    getURLs()
    for thread_title, dat in zip(title, url):
        print(thread_title,dat)#スレタイとURL
        #with open('/Users/hbk/Documents/code/hisshi.txt','w') as file:
        #    file.write(thread_title)
        #    file.write(dat)

        subject = dat
        request = urllib.request.Request(url=subject, headers=headers)#datとheaderのデータを入れる

        with urllib.request.urlopen(request) as nep:#withを使うことでcloseを省略
            text = nep.read().decode('cp932')#subject.txtはcp932なので

            print(text)
            #ファイルの書き込み
            if os.path.exists("./hisshi.txt"):
                with open('./hisshi.txt','a') as file:
                #with open('./+str(ID)+.txt','a') as file:
                #ここに文字列検索を入れる。もし、IDが見つかったら、スレタイとURLを記載する。textからIDが見つかったら、記入、改行する。
                    file.write(thread_title)
                    file.write(dat+str('\n'))
                    file.write(text)
                    file.write(str('\n'))
            else:
                with open('./hisshi.txt','w') as file:
                #with open('./+str(ID)+.txt','w') as file:
                #ここに文字列検索を入れる。もし、IDが見つかったら、スレタイとURLを記載する。textからIDが見つかったら、記入、改行する。

                    file.write(thread_title)
                    file.write(dat+str('\n'))
                    file.write(text)
                    file.write(str('\n'))
            #continue
        #continue




'''
def makefile():
    getURLs()
    #ファイルの書き込み
    with open('/Users/hbk/Documents/code/hisshi.txt','w') as file:
        write = [i for i in url]
        file.write(str(write))

'''

#ID = input('記入方法は【ID:OOOOOOO】>>')
#getURLs()
datfile()

'''
終わったこと
subject.txtからdatを取得してURL化したurl配列が完成
ついでにスレタイもゲット

やること
input関数でIDを取得する。
IDを見つけたらその行を取得する。
<br>を¥nに変換
&gt;&gt;を>>に変換
最後にテキストデータとして書き出したい

'''
