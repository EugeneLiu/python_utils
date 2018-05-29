#Python常用时间处理

```python
import datetime

# 当前时间
print(datetime.datetime.now())

# 当前日期
print(datetime.datetime.today().date())
print(datetime.datetime.now().date())
print(datetime.date.today())

# 获取昨天，明天
today = datetime.date.today()
yesterday = today-datetime.timedelta(days=1)
tomorrow = today+datetime.timedelta(days=1)

# 获取当天的开始时间和结束时间
first_time = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
last_time = datetime.datetime.combine(datetime.date.today(), datetime.time.max)

# 获取某个月有多少天
import calendar
_, monthRange = calendar.monthrange(year, month)

# 获取某个月的最后一天
lastDay = datetime.datetime.date(year=year, month=month, day=monthRange)

from dateutil.relativedelta import relativedelta
from dateutil.rrule import rrule, DAILY

start_date = datetime.date(2018, 1, 1)
last_date = datetime.date(2018, 12, 31)

# 计算两个日期之间有多少个周天
sunday_count = rrule(DAILY, dtstart=start_date, until=last_date, byweekday=6).count()

# 计算两个日期之间有多少天
days = (last_date-start_date).days+1

# 计算某个日期100天后的日期
after_date = start_date + relativedelta(days=+100)

# 计算某个日期20个月后的日期
after_date = start_date + relativedelta(months=+20)

# datetime和字符串之间的转换
datetime_format_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
datetime_obj = datetime.datetime.strptime(datetime_format_str, "%Y-%m-%d %H:%M:%S")

# datetime和时间戳的相互转换
import time
import datetime
now = datetime.datetime.now()
timestamp = time.mktime(now.timetuple())

datetime_obj = datetime.datetime.fromtimestamp(timestamp)
```

