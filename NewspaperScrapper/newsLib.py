from parseLib import *
from utilLib import *
from datetime import datetime, timedelta

class NewsLister:
    
    page: int; category: Category
    date: datetime; outboundMonth: str
    
    def __init__(self, year: str, month: int, maxMonth: int, category: str):
        self.page = 0
        self.category = Category[category].value
        self.date = datetime.fromisoformat(f"{year}-{month:02d}-01")
        self.outboundMonth = maxMonth + 1
    
    def _firstDay(self):
        currDate = self.date
        return currDate.day == 1
    
    def _updatePage(self):
        currPage = self.page
        category = self.category
        currDate = self.date
        html = page(category, currDate, currPage)
        
        print(self.date, "Update Page")
        if (currPage != findCurrentPage(html)):
            self.date += timedelta(days = 1)
            self.page = 1
            
        
    
    def _nextPage(self):
        if self._firstDay(): self.page = 1
        else: self.page += 1
        self._updatePage() 
    
    def hasNext(self):
        currDate = self.date
        year = currDate.year
        month = currDate.month
        return (currDate.year == year) and (self.outboundMonth != month)
    
    def next(self):
        self._nextPage()
        
        currPage = self.page
        category = self.category
        currDate = self.date
        
        html = page(category, currDate, page)
        print(html)
        
        newsList = findArticleList(html)
        paperList = []
        
        print(newsList)
        for link in newsList:
            bot = ParserBot(link)
            paperList.append(bot.run())
            
        return paperList 
