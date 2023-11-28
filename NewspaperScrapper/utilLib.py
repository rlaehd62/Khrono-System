import calendar, requests
from enum import Enum
import datetime
from datetime import timedelta, datetime

class Category(Enum):
    ECONOMY = '101', '263'
    SCIENCE = '105', '228'

def lastDay(year: int, month: int): return calendar.monthrange(year, month)[1]
def get(url: str, userAgent: str):
    return requests.get(f"{url}", headers={'User-Agent': userAgent}).text

