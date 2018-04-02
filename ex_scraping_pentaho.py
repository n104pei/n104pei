# coding: UTF-8
import urllib, urllib.request
from bs4 import BeautifulSoup

#アクセス先URL
url = 'http://help.pentaho.com/Documentation/7.1/0L0/0A0/0'

#URLアクセス
req = urllib.request.Request(url=url)
try:
    html = urllib.request.urlopen(req)
    #print(f.read().decode('utf-8'))
    # htmlをBeautifulSoupで扱う
    soup = BeautifulSoup(html, "html.parser")

    # タイトル要素を取得する → <title>経済、株価、ビジネス、政治のニュース:日経電子版</title>
    title_tag = soup.title

    # 要素の文字列を取得する → 経済、株価、ビジネス、政治のニュース:日経電子版
    title = title_tag.string

    print("####タイトル####")
    print(title_tag)
    print("####タイトル####")
    print(title)
except urllib.error.HTTPError as e: # HTTPレスポンスのステータスコードが404, 403, 401などの例外処理
    print(e.reason)
except urllib.error.URLError as e: # アクセスしようとしたurlが無効なときの例外処理
    print(e.reson)


