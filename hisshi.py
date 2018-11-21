'''
datのルール
<>はスペース1つ分
<br>は\n相当
&gt;&gt;は>>
'''

import urllib.request
import os
headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"
        }

def getURLs():
    #URLとスレタイを取得するプログラム
    subject = "https://next2ch.net/news4vip/subject.txt"
    request = urllib.request.Request(url=subject, headers=headers)#

    with urllib.request.urlopen(request) as nep:#withを使うことでcloseを省略,接続
        text = nep.read().decode('cp932')#subject.txtはcp932なので

        #global url,title
        url = [f"https://next2ch.net/news4vip/dat/{line.split('<', 1)[0].strip()}" for line in text.splitlines()]#subject.txtから一行ずつに分けて、<以前にあるものを取得してきている。
        title = [f"{line.split('>', 1)[-1].strip()}" for line in text.splitlines()]#textから一行ずつに分けて、>以降にあるものを取得してきている。
        return title,url
    #print(url)
    #print(title)

def getALL():
    title,url = getURLs()
    #print(title,url)

    i=0

    for thread_title, dat in zip(title, url):
        #print(thread_title,dat)#スレタイとURL
        if i > 3000:
            break
        subject = dat
        request = urllib.request.Request(url=subject, headers=headers)#datとheaderのデータを入れる

        with urllib.request.urlopen(request) as nep:#withを使うことでcloseを省略,接続
            text = nep.read().decode('cp932')#datファイル読み込み。cp932?
            lines = text.splitlines()

            #print(lines[0])
            #ファイルの書き込み
            #with open('./hisshi.txt','w') as file:
            with open('./'+str(ID)+'.txt','a') as file:
                for line in lines:
            #ここに文字列検索を入れる。もし、IDが見つかったら、スレタイとURLを記載する。textからIDが見つかったら、記入、改行する。
                    if line.find(ID) != -1:
                        file.write(thread_title)
                        file.write(dat+str('\n'))
                        file.write(line)
                        print(line)
                        file.write(str('\n'))
                    else:
                        i+=1
            #continue
        #continue




#ID = input('記入方法は【ID:OOOOOOO】>>')
ID = input('記入方法は【ID:iWG6wjJn】>>')
#getURLs()
getALL()

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
