import sys, pandas as pd, time
from datetime import datetime
from Utillity import Date
from bot import BookDataBot,  KeywordBot, KeywordAnalyzer

def _error(msg: str):
    print(msg)
    exit(0)

def _main():
    
    
    if len(sys.argv) < 5: _error("> [Command] [Year] [Start Month] [End Month] [ECONOMY / SCIENCE]")
    currentMonth = datetime.now().month
    
    year: int = int(sys.argv[1])
    startMonth = int(sys.argv[2]); 
    endMonth = int(sys.argv[3])
    categoryName: str = sys.argv[4]
    if endMonth >= currentMonth: _error(f"Month Out of Range (Allow : Month < {currentMonth})")
    
    # 월별 인기 도서 데이터
    bookDataFrame = BookDataBot.process(year, startMonth, endMonth, categoryName)
    print(bookDataFrame.to_string())
    
    # 도서별 키워드 데이터
    keywordFrame = KeywordBot.process(bookDataFrame)
    print(keywordFrame.to_string())
    
    # (월별, 도서별) 인기 도서 + 키워드 데이터
    totalBookDataFrame = pd.merge(bookDataFrame, keywordFrame, on = 'ISBN')
    totalBookDataFrame.to_csv("TotalBookData.csv")
    
    analyzedDataFrame = KeywordAnalyzer.process(year, startMonth, endMonth, totalBookDataFrame)
    analyzedDataFrame.to_csv("AnalyzedKeywords.csv")
    
if __name__ == '__main__': _main()