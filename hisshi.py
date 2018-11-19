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

def getALL():
    getURLs()
    for thread_title, dat in zip(title, url):#スレタイとURLが尽きるまで検索
        #print(thread_title,dat)#スレタイとURL

        subject = dat
        request = urllib.request.Request(url=subject, headers=headers)#datとheaderのデータを入れる

        with urllib.request.urlopen(request) as nep:#withを使うことでcloseを省略,接続する。
            text = nep.read().decode('cp932')#読み込み。subject.txtはcp932なので

            #print(text)
            #ファイルの確認

            #with open('./hisshi.txt','a') as file:
            with open('./'+str(ID)+'.txt','w') as file:  #IDをテキスト名に
                if str(ID) in text:
                    #ここに文字列検索を入れる。もし、IDが見つかったら、スレタイとURLを記載する。textからIDが見つかったら、記入、改行する。
                    file.write(thread_title)
                    file.write(dat+str('\n'))
                    file.write(text)
                    print(text)
                    #if str(ID) in text:#textにIDが見つかったら記入して改行する
                    #    file.write(text)
                    #    file.write(str('\n'))
                    #    print(text)
        #formatter()
'''
def formatter():
    with open('./'+str(ID)+'.txt','r') as file:
        filedata=file.read()
        filedata=filedata.replace('<br>','\n')
    with open('./'+str(ID)+'.txt','w') as file:
        file.write(filedata)

'''


ID = input('記入方法は【ID:OOOOOOO】>>')
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
