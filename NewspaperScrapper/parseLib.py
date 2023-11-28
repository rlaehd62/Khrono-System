import requests, time
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as Soup
from utilLib import Category, lastDay, get
from datetime import datetime, timedelta

from storage.news import *

ua = UserAgent()
dateSelector: str = "#ct > div.media_end_head.go_trans > div.media_end_head_info.nv_notrans > div.media_end_head_info_datestamp > div:nth-child(1) > span"
class ParserBot:
    
    url: str
    base: Soup
    
    def __init__(self, url: str): 
        response = get(url, ua.random)
        self.base = Soup(response, "html.parser")
        self.url = url
        
    def run(self) -> Newspaper:
        
        title = self._title()
        context = self._context()
        year = self._year()
        month = self._month()
        
        paper = Newspaper(title, context, year, month)
        paper.uniqueID = _findUniqueID(self.url)
        return paper
        
    def _title(self): 
        return self.base.title
    
    def _context(self): 
        return self.base.select("#dic_area")[0].text
    
    def _year(self):
        element = self.base.select(dateSelector)[0]
        return element.text.split(".")[0]
    
    def _month(self):
        element = self.base.select(dateSelector)[0]
        return element.text.split(".")[1]
    
def page(category: Category, date: datetime, page: int):
    year, month, day = (date.year, date.month, date.day)
    BASE = 'https://news.naver.com/main/list.naver?mode=LS2D&'
    response = get(f'{BASE}sid2={category[1]}&sid1={category[0]}&mid=shm&date={year}{month:02d}{day:02d}&page={page}', ua.random)
    print(f'{BASE}sid2={category[1]}&sid1={category[0]}&mid=shm&date={year}{month:02d}{day:02d}&page={page}')
    return response

def findArticleList(html: str) -> list:
     artList = []
     soup = Soup(html, "html.parser") 
     for element in soup.select("dt:not(.photo) a[href^='https://n.news.naver.com/mnews/article']"):
            artList.append(element.get("href"))
     return artList

def findCurrentPage(html: str) -> str:
    soup = Soup(html, "html.parser")
    currentPage = soup.select('#main_content > div.paging > strong')[0].text
    return currentPage

def _findUniqueID(url: str):
    group = url.split("?")
    ID = group[0].split("/")[-1]
    CATEGORY = group[1].split("=")[-1]
    return f"{CATEGORY}-{ID}"