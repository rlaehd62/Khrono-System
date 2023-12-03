import pandas as pd

# Big Kinds는 '일자', 현재는 테스트 전용
DATE_COLUMN: str = 'DATE'

# YEAR-MONTH-DAY 중 DAY를 제거한다
def changeDate(date):
    return str(date)[0:6]

# 뉴스 데이터를 월 기준으로 재구조화
def initNews(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df[DATE_COLUMN] = df[DATE_COLUMN].apply(changeDate)
    return df.groupby(by=['DATE'])['KEYWORD'].apply(lambda x: ' '.join(x)).reset_index()
    

def main():
    
    print("# Absolute path of keyword file")
    df_keywords = pd.read_csv(input())
    
    print("\n#Absolute path of news file")
    df_news = initNews(input())
    
    # TODO : 반복하며 Cosine Similarity 계산하기.

if __name__ == "__main__":
    main()