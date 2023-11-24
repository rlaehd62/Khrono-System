from newsLib import *

print("# 연도")
year = int(input())

print("\n# 월")
month = int(input())

print("\n카테고리")
categoryName = input()

nl = NewsList(year, month, categoryName)

newsList = []
while nl.hasNextDay():
    print(f"\n# {nl.year}/{nl.month}/{nl.day}")
    while nl.hasNextPage(): 
        newsList += nl.next()
        print(f"> Page {nl.page} ({len(newsList)})")
        break
    nl.nextDay()
    break

cnt = 0
newspapers = []
for url in newsList:
    paper = Newspaper(url)
    print(paper.toRow())
    cnt += 1
    
print(cnt)
