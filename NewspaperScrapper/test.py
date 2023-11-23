from newsLib import NewsList

nl = NewsList(2023, 1, "SCIENCE")
newsList = []
while nl.hasNextDay():
    print(f"\n# {nl.year}/{nl.month}/{nl.day}")
    while nl.hasNextPage(): 
        newsList += nl.next()
        print(f"> Page {nl.page} ({len(newsList)})")
    nl.nextDay()
