import requests, time
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as Soup
from utilLib import Category, lastDay, get

ua = UserAgent()    
class ParserBot:
    
    base: Soup
    dateSelector: str = "#ct > div.media_end_head.go_trans > div.media_end_head_info.nv_notrans > div.media_end_head_info_datestamp > div:nth-child(1) > span"
    
    def __init__(self, url: str): 
        response = get(url, ua.random)
        self.base = Soup(response, "html.parser")
        
    def title(self): 
        return self.base.title
    
    def context(self): 
        return self.base.select("#dic_area")[0].text
    
    def year(self):
        element = self.base.select(self.dateSelector)[0]
        return element.text.split(".")[0]
    
    def month(self):
        element = self.base.select(self.dateSelector)[0]
        return element.text.split(".")[1]