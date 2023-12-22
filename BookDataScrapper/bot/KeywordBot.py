import sys, pandas as pd, time
from crawling import Data4Lib, KyoboLib
from crawling.Data4Lib import LibCategory
from crawling.KyoboLib import KyoboCategory
from Utillity import Date

class KeywordBot:
    
    pointer = -1
    max_pointer = 0
    bookData: list[dict]
    
    def __init__(self, bookData: list[dict]):
        self.bookData = bookData
        self.max_pointer = len(bookData)
        
    def hasNext(self) -> bool: return (self.pointer + 1) < self.max_pointer
    def next(self) -> pd.DataFrame:
        self.pointer += 1
        ISBN = self.bookData[self.pointer]['ISBN']
        return Data4Lib.getKeywords(ISBN)

def process(bookDataFrame: pd.DataFrame):
    
    bookData = bookDataFrame.to_dict('records')
    keybot = KeywordBot(bookData)
    dataFrames = []
    while keybot.hasNext(): 
        dataFrames.append(keybot.next())
        time.sleep(0.1)
    totalDataFrame = pd.concat(dataFrames, ignore_index=True)
    return totalDataFrame