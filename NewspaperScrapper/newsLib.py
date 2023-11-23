from fake_useragent import UserAgent
from parseLib import ParserBot
from bs4 import BeautifulSoup as Soup
from utilLib import Category, lastDay, get

ua = UserAgent()
class Newspaper:
    
    id: str
    title: str; context: str
    year: int; month: int
    
    def __init__(self, url: str):
        bot: ParserBot = ParserBot(url)
        self.id = extractUID(url)
        self.title = bot.title()
        self.context = bot.context()
        self.year = bot.year()
        self.month = bot.month()
        
    def toRow(self): 
        return (self.id, self.year, self.month, self.title, self.context)

class NewsList:
    
    page: int
    category: Category
    year: str; month: str
    day: int; maxDay: int
    
    def __init__(self, year: str, month: str, category: str):
        self.page = 0
        self.category = Category[category].value
        
        self.year = year
        self.month = month
        
        self.day = 1
        self.maxDay = lastDay(year, month)
    
    def __getPage(self, page):
        BASE = 'https://news.naver.com/main/list.naver?mode=LS2D&'
        response = get(f'{BASE}sid2={self.category[1]}&sid1={self.category[0]}&mid=shm&date={self.year}{self.month:02d}{self.day:02d}&page={page}', ua.random)
        return response
        
    def hasNextPage(self) -> bool:
        soup = Soup(self.__getPage(page = self.page + 1), "html.parser")
        currentPage = soup.select('#main_content > div.paging > strong')[0].text
        return (self.page + 1) == int(currentPage)
   
    def nextPage(self): 
        self.page += 1
        
    def hasNextDay(self):
        return (self.day < self.maxDay)
    
    def nextDay(self):
        self.day += 1
        self.page = 0
        
    def next(self):
        self.page += 1; lst = []
        soup = Soup(self.__getPage(self.page), "html.parser") 
        for element in soup.select("dt:not(.photo) a[href^='https://n.news.naver.com/mnews/article']"):
            lst.append(element.get("href"))
        return lst
            
        
def extractUID(url: str):
    group = url.split("?")
    ID = group[0].split("/")[-1]
    CATEGORY = group[1].split("=")[-1]
    return f"{CATEGORY}-{ID}"
