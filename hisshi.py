

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

        #global url,title　戻り値を使え！
        url = [f"https://next2ch.net/news4vip/dat/{line.split('<', 1)[0].strip()}" for line in text.splitlines()]#subject.txtから一行ずつに分けて、<以前にあるものを取得してきている。
        title = [f"{line.split('>', 1)[-1].split('(',1)[0].strip()}" for line in text.splitlines()]#textから一行ずつに分けて、>以降にあるものを取得してきている。また、（以前の物
        return title,url


def getALL():
    title,url = getURLs()#戻り値から入手

    i=0

    for thread_title, dat in zip(title, url):#スレッドセット（スレタイとURL）
        #print(thread_title,dat)

        if i > 2000:#体感8レス以降は取得しないようにした。3000にすると若干ラグを感じる
            break

        rescount = 0#スレッドセットを読み込む度に初期化→１回目のレスには絶対スレタイURLが必要なので
        subject = dat
        request = urllib.request.Request(url=subject, headers=headers)#datとheaderのデータを入れる

        with urllib.request.urlopen(request) as nep:#withを使うことでcloseを省略,接続
            text = nep.read().decode('cp932')#datファイル読み込み。cp932?
            text = text.splitlines()#データロードしたらこれをやれ

            with open('./'+str(ID)+'.txt','a') as file:


                for line in text:#スレッドのレスずつに分けている。


                    if line.find(ID) != -1:#IDがあった時（-1とは存在しないこと）
                        if rescount == 0:
                            file.write(thread_title+str('\t'))
                            file.write(dat+str('\n'))#スレタイとURLを書く

                            if line.find(thread_title) != -1:#datルール上、>>1の書き込みの末尾にはスレタイがついているので消す必要がある
                                fix = line.replace(thread_title,'')
                                file.write(fix)#replaceは新しい文字列を作るだけなので！
                                print('fixed\n')
                                print(fix)
                            else:
                                file.write(line)#普通に書き込む
                                print(line)

                            file.write(str('\n'))
                            rescount+=1

                        else:
                            #2レス目以降にスレタイ不要
                            file.write(line)
                            print(line)
                            file.write(str('\n'))

                    else:
                        i+=1

def format():
    with open('./'+str(ID)+'.txt','r') as file:
        raw = file.read()
        format = raw.replace('<br>','\n').replace('<><>','\b').replace('<>','\n').replace('&gt;&gt;','>>').replace('/dat','').replace('.dat','')
    with open('./'+str(ID)+'.txt','w') as file:
        file.write(format)
        '''
        datのルール
        <>はスペース1つ分
        <br>は\n相当
        &gt;&gt;は>>
        URLをアクセスできるものに修正
        '''

ID = input('記入方法は【ID:OOOOOOO】>>')
getALL()
format()

'''
処理手順
subject.txtにアクセスして、必要なデータ(datURL一覧、スレタイ一覧)を集める→splitなどを駆使して空白や改行を消す
行分割されたdatのURLとスレタイを配列に格納されている

datのURLから、中のレスを取り出す→全文同じ配列番地にあるのでsplitlines()で行分割して再格納
forループで1つずつ順に取り出して行く
レスの検査、若干修正

書き終えたファイルから、ゴミを取り除く
完成
'''
