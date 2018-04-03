# coding: UTF-8
import urllib, urllib.request
from bs4 import BeautifulSoup
import pandas as pd

input_file = ''#Fileパス
input_book = pd.ExcelFile(input_file)

#sheet_namesメソッドでExcelブック内の各シートの名前をリストで取得できる
input_sheet_name = input_book.sheet_names
num_sheet = len(input_sheet_name)#lenでシートの総数を確認
input_sheet_df = input_book.parse(input_sheet_name[0]) #DataFrameとして一つ目のsheetを読込
#別例
#input_sheet_df = input_book.parse(input_sheet_name[0], skiprows = 5,skip_footer = 2,parse_cols = "B:H,J:O",names =  range(0,13))
input_sheet_df.head(10) #読み込んだシートの先頭10行を表示


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

"""
proxy処理が必要かも
import urllib.request
proxies ={'http':'http://proxy.-----.co.jp/proxy.pac'}
proxy_handler = urllib.request.ProxyHandler(proxies)
opener = urllib.request.build_opener(proxy_handler)
urllib.request.install_opener(opener)
html = urllib.request.urelopen("http://wwww.pythonscraping.com/pages/page1.html")
print(html.read())
"""


