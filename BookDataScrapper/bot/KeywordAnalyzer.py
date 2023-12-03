import sys, pandas as pd, time
from crawling.gptLib import extractKeywords
from Utillity import Date

class Analyzer:
    
    year: int
    month: int
    
    startMonth: int
    endMonth: int
    
    totalBookDataFrame: pd.DataFrame
    
    def __init__(self, year: int, startMonth: int, endMonth: int, totalBookDataFrame: pd.DataFrame):
        self.year = year
        self.month = startMonth - 1
        self.startMonth = startMonth
        self.endMonth = endMonth
        self.totalBookDataFrame = totalBookDataFrame
        
    def hasNext(self): return self.month + 1 <= self.endMonth
    def next(self):
        self.month += 1
        df: pd.DataFrame = self.totalBookDataFrame
        filtered_df = df[(df['YEAR'] == self.year) & (df['MONTH'] == self.month)]
        
        keywords = filtered_df['KEYWORD'].tolist()
        keywords = extractKeywords(' '.join(keywords))
        return (f"{self.year}{self.month:02d}", ','.join(keywords))
        
        # print(keywords)
        
        # dataList = []
        # for keyword in keywords: dataList.append([ self.year, self.month, keyword ])
        # return pd.DataFrame(dataList, columns = [ 'YEAR', 'MONTH', 'KEYWORD '])
    

def process(year: int, startMonth: int, endMonth: int, totalBookDataframe: pd.DataFrame):
    # dataFrames = []
    rows = []
    analyzer = Analyzer(year, startMonth, endMonth, totalBookDataframe)
    while analyzer.hasNext(): rows.append(analyzer.next())
    # return pd.concat(dataFrames, ignore_index=True)
    return pd.DataFrame(rows, columns = ['DATE', 'KEYWORDS'])