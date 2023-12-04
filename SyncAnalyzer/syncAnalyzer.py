import pandas as pd
from lib.syncLib import calculate_similarity as cs

# Big Kinds는 '일자', 현재는 테스트 전용
DATE_COLUMN: str = '일자'

# YEAR-MONTH-DAY 중 DAY를 제거한다
def change_date(date):
    return str(date)[0:6]

def test(keywords, x):
    sentence1 = keywords[x].replace(",", " ")
    sentence2 = x.replace(",", " ")
    return cs(sentence1, sentence2)

# 뉴스 데이터를 월 기준으로 재구조화
def init_news(path: str, keywords) -> pd.DataFrame:
    df = pd.read_csv(path, index_col = 0)
    df['일자'] = df['일자'].apply(change_date)
    df['키워드'] = df['키워드'].apply(lambda x: str(x).replace(",", " "))
    df['비교군'] = df.apply(lambda row: keywords[int(row['일자'])].replace(",", " "), axis = 1)
    
    df['일치율'] = df.fillna('NO KEYWORDS FOUND ON THIS ROW').apply(lambda row: cs(row['비교군'], row['키워드']), axis = 1)
    df = df.drop(columns=['비교군', '언론사', '기고자', '통합 분류1', '통합 분류2', '통합 분류3', '사건/사고 분류1', '사건/사고 분류2', '사건/사고 분류3', '인물', '위치', '기관','분석제외 여부'], axis=1)
    return df.sort_values(by = ['일치율'],ascending=False)
    

def main():
    
    print("# Absolute path of keyword file")
    df_keywords = pd.read_csv(input(), index_col = 0)
    keywords = df_keywords.set_index('DATE').to_dict()['KEYWORDS']
    print(keywords[202301])
    
    
    print("\n#Absolute path of news file")
    df_news = init_news(input(), keywords)
    print(df_news[['일자', '제목', '일치율']].to_string(max_rows=100))
    # TODO : Cosine Similarity 평균 내기
    

if __name__ == "__main__":
    main()