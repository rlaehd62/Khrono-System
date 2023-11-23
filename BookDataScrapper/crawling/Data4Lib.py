import requests, bs4 as BeautifulSoup, calendar

import xml.etree.ElementTree as ET, json, pandas as pd, time
from enum import Enum

from Utillity import Date


KEY = "bc9e846cbd6b5233e1399d28fd6d7c37eab3f1542ced6974021e3977b4086489"

KEYWORD_LIMIT = 10

BOOK_LIMIT = 20


class LibCategory(Enum):
    
    ECONOMY = '32', '경제',
    SCIENCE = '40;50', '과학'
    
    

def getBookList(category: LibCategory, date: Date): 

    dataList = []

    url = f"https://data4library.kr/api/loanItemSrch?authKey={KEY}&pageSize={BOOK_LIMIT}&startDt={date.firstdate()}&endDt={date.lastDate()}&addCode=0;1&age=20;30;40;50;60;-1&dtl_kdc={category.value[0]}"
    print(f"Requests to {url}")

    response = requests.get(url); response.encoding = "utf-8"

    root = ET.fromstring(response.text)[3]

    for data in root: dataList.append((data.find("isbn13").text, date.year, date.month))

    return pd.DataFrame(dataList, columns = [ "ISBN", "YEAR", "MONTH" ])


def getKeywords(ISBN: str):

    dataList = []

    url = f'https://data4library.kr/api/keywordList?authKey={KEY}&isbn13={ISBN}&additionalYN=N'
    print(f"Requests to {url}")


    response = requests.get(url); response.encoding = "utf-8"

    root = ET.fromstring(response.text)[2]

    for item in root[:KEYWORD_LIMIT]: dataList.append((ISBN, item.find("word").text))

    return pd.DataFrame(dataList, columns=[ 'ISBN', 'KEYWORD'])