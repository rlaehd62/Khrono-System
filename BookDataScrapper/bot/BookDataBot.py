import sys, pandas as pd, time
from crawling import Data4Lib, KyoboLib
from crawling.Data4Lib import LibCategory
from crawling.KyoboLib import KyoboCategory
from Utillity import Date

class BookBot:
    
    year: int
    month: int
    
    startMonth: int; endMonth: int
    categories: (LibCategory, KyoboCategory)
    
    def __init__(self, year: int, startMonth: int, endMonth: int, categoryName: str):
        
        self.year = year
        self.month = startMonth-1
        self.startMonth = startMonth
        self.endMonth = endMonth
        
        if categoryName not in LibCategory._member_names_ : raise KeyError(f"Category {categoryName} Not Found")
        elif categoryName not in KyoboCategory._member_names_: raise KeyError(f"Category {categoryName} Not Found")
        self.categories = (LibCategory[categoryName], KyoboCategory[categoryName])
        
    def hasNext(self) -> bool: return self.month + 1 <= self.endMonth
    def next(self) -> pd.DataFrame:
        
        self.month += 1
        date = Date(self.year, self.month)
        
        dataFrames = []
        dataFrames.append(Data4Lib.getBookList(self.categories[0], date))
        dataFrames.append(KyoboLib.getBestList(date, self.categories[1]))
        time.sleep(0.1)
        
        totalDataFrame = pd.concat(dataFrames, ignore_index=True)    
        totalDataFrame = totalDataFrame.drop_duplicates(subset=[ 'ISBN' ])
        return totalDataFrame

def process(year: int, startMonth: int, endMonth: int, categoryName: str):
    
    dataFrames = []
    bot: BookBot = BookBot(year, startMonth, endMonth, categoryName)
    while bot.hasNext(): 
        dataFrames.append(bot.next())
        time.sleep(0.1)
    totalDataFrame = pd.concat(dataFrames, ignore_index=True)    
    totalDataFrame = totalDataFrame.drop_duplicates(subset=['ISBN', 'YEAR', 'MONTH' ])
    return totalDataFrame