from operator import index
import pandas as pd
import numpy as np
from lib.syncLib import calculate_similarity as cs

# Big Kinds는 '일자', 현재는 테스트 전용
DATE_COLUMN: str = '일자'

# YEAR-MONTH-DAY 중 DAY를 제거한다
def changeDate(date):
    return str(date)[0:6]

def formatKeywords(x: pd.Series):
    array = [val for val in x.values if not pd.isnull(val)]
    return str(''.join(array))

# 뉴스 데이터를 월 기준으로 재구조화
def initNews(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, index_col = 0)
    df['일자'] = df['일자'].apply(changeDate)
    return df.groupby(by=['일자'])['특성추출(가중치순 상위 50개)'].apply(formatKeywords).reset_index()
    

def main():
    
    print("# Absolute path of keyword file")
    df_keywords = pd.read_csv(input(), index_col = 0)
    keywords = df_keywords.set_index('DATE').to_dict()['KEYWORDS']
    print(keywords[202301])
    
    
    print("\n#Absolute path of news file")
    df_news = initNews(input())
    df_news['일치율'] = df_news['일자'].apply(lambda x: cs(keywords[int(x)].replace(",", " "), ''.join(df_news['특성추출(가중치순 상위 50개)'].values).replace(",", " ")))
    print(df_news['일치율'].to_string())
    
    # TODO : 반복하며 Cosine Similarity 계산하기.

if __name__ == "__main__":
    main()