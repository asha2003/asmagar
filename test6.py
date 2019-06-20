import time
from datetime import date
date1 = date(2017, 6, 24)

date2 = date(2017, 6, 30)


difference = abs(date2 - date1)
print(difference.days)