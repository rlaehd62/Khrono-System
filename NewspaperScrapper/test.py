from newsLib import *
import pandas as pd

print("# [연도]")
year = int(input())

print("\n# [시작_월] [최대_월]")
month, maxMonth = map(int, input().split())

print("\n[카테고리]")
categoryName = input()

lister = NewsLister(year, month, maxMonth, categoryName)

paperList = []
while lister.hasNext(): 
    paperList += lister.next()
    print(paperList)

df = pd.DataFrame(paperList,  columns=['ID', 'YEAR', 'MONTH', 'TITLE', 'CONTEXT'])
df.to_csv("data.csv", index=False)
