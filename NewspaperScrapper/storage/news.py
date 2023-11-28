class Newspaper:
    
    uniqueID: str
    title: str
    context: str
    year: str
    month: str
    
    def __init__(self, title: str, context: str, year: str, month: str):
        self.title = title
        self.context = context
        self.year = year
        self.month = month    
    
    def toRow(self):
        return (self.uniqueID, self.year, self.month, self.title, self.context)