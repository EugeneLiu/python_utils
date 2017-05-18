# coding: utf-8
import datetime
import calendar
from dateutil.rrule import *

def beteen_two_day_have_many_sunday(start_date, end_date):
    return rrule(DAILY, dtstart=start_date, until=end_date, byweekday=6).count()

def between_two_date_days(start_date, end_date):
    # 计算两个日期之间有多少天
    return (end_date - start_date).days

def get_month_days(year, month):
    # 获取某年某月有多少天
    return calendar.monthrange(year, month)[1]

if __name__ == '__main__':
    pass
