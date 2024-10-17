from datetime import date
from functools import reduce
def numOfDays (date1, date2):
    return reduce (lambda x, y: (y-x).days, [date1, date2])

date1 = date (2024, 9, 11)
date2 = date (2024, 10, 16)
print (numOfDays(date1, date2), "days")