import calendar, time
class Date:
    
    year: int
    month: int
    textFormat: str
    
    def __init__(self, year: int, month: int, textFormat: str = "{}-{:02d}-{:02d}"):
        self.year = year
        self.month = month
        self.textFormat = textFormat
        
    def firstdate(self):
        return self.textFormat.format(self.year, self.month, 1)
    
    def lastDate(self):
        lastDay = calendar.monthrange(self.year, self.month)[1]
        return self.textFormat.format(self.year, self.month, lastDay)
    
    def toString(self): return f"{self.year}{self.month:02d}"