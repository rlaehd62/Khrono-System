import requests, bs4 as BeautifulSoup, calendar, pandas as pd

from Utillity import Date

from enum import Enum


PAGE_LIMIT = 20

KEYWORD_LIMIT = 20


BASE_URL = "https://product.kyobobook.co.kr/api/gw/pub/pdt/best-seller/total"

MONTH_BEST = f"{BASE_URL}/?page=1&per={PAGE_LIMIT}" + "&period=003&ymw={}&bsslBksClstCode={}"

KEYWORD = "https://kyobobook-rec-api.eigene.io/rec/v3/kyobo222?key={}" + f"&size={KEYWORD_LIMIT}"

class KyoboCategory(Enum):

    ECONOMY = 'K', '경제'

    SCIENCE = 'M', '과학'


def getBestList(date: Date, category: KyoboCategory):

    dataList = []

    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36" }

    document = requests.get(MONTH_BEST.format(date.toString(), category.value[0]), headers=headers).json()

    for book in document['data']['bestSeller']: dataList.append([ book['cmdtCode'], date.year, date.month ])

    return pd.DataFrame(dataList, columns = [ 'ISBN', 'YEAR', 'MONTH'])


def getKeywords(ISBN):

    dataList = []

    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36" }

    document = requests.get(KEYWORD.format(ISBN), headers=headers).json()

    for item in document['persona']: dataList.append(( ISBN, item['keyword'] ))

    return pd.DataFrame(dataList, columns = [ 'ISBN', 'KEYWORD' ])