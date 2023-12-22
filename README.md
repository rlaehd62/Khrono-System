# Project Info
- 주제 선정 : 2023년 10월 20일
- 개발 기간 : 2023년 10월 27일 ~ 12월 15일

### 후기
개발 중 만들었던 내용을 한 번 갈아엎고 다시 만들어서 완성도가 매우 아쉽다. <br />
기존에 사용하고 싶었던 것들 (SupaBase, NLP 모델) 등을 사용해서 재밌었던 프로젝트.
  
### API KEY
- OPEN AI API **(gptLib.py의 변수 KEY)**
- 도서관 정보나루 API **(Data4Lib.py의 변수 KEY)**

# 제공 기능
### 인기 도서 및 키워드
- python3 BookDataProcessor.py [연도] [시작_월] [종료_월] [카테고리 : SCIENCE / ECONOMY]

### 뉴스와 키워드 간의 일치율
- **News는 빅카인즈에서 제공 한 데이터로 한정**
- **Keyword는 BookDataProcessor의 AnalyzedKeyword.csv 파일로 한정**
- python3 syncAnalyzer.py

# 서버 (SupaBase 사용)
### 데이터베이스
- Table "News" = ID (Primary Key), TYPE (Category; Text), DATE (Text), TITLE (Text), SYNC (Float), URL (TEXT)
- Table "Sync" = ID (Primary Key), TYPE (Category; Text), DATE (Text), SYNC (Float)
### 데이터 입력
- **CSV 파일과 테이블의 Column Name이 다르기에 사전에 변경**
- **totalSync.csv**를 Table "News" 에 입력
- **monthlySync.csv**를 Table "Sync" 에 입력

### 웹과 연동
- **환경변수 ".env.local" 생성**
- REACT_APP_URL = https://<PROJECT_ID>.supabase.co
- REACT_APP_KEY = [Project API Service Role]
