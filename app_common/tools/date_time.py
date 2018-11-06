#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: date.py
@time: 2017/6/10 下午6:00
"""


import time
import pytz
import calendar
from datetime import datetime, timedelta, date


def get_current_day_time_ends(type=0):
    """
    获取当天开始结束时刻
    :return:
    """
    today = datetime.today()
    if type == 1:
        start_time = datetime(today.year, today.month, today.day, 0, 0, 0)
        return start_time
    elif type == 2:
        end_time = datetime(today.year, today.month, today.day, 23, 59, 59)
        return end_time
    else:
        start_time = datetime(today.year, today.month, today.day, 0, 0, 0)
        end_time = datetime(today.year, today.month, today.day, 23, 59, 59)
        return start_time, end_time


def get_current_month_time_ends():
    """
    获取当月开始结束时刻
    :return:
    """
    today = datetime.today()
    _, days = calendar.monthrange(today.year, today.month)
    start_time = datetime(today.year, today.month, 1, 0, 0, 0)
    end_time = datetime(today.year, today.month, days, 23, 59, 59)
    return start_time, end_time


def get_current_week_time_ends():
    """
    获取当周开始计数时刻
    :return:
    """
    today = datetime.today()
    week_day_offset = datetime.today().weekday()
    week_start = today - timedelta(days= week_day_offset)
    week_end = today + timedelta(days=(6-week_day_offset))
    start_time = datetime(week_start.year, week_start.month, week_start.day, 0, 0, 0)
    end_time = datetime(week_end.year, week_end.month, week_end.day, 23, 59, 59)
    return start_time,end_time


def get_current_year_time_ends():
    """
    获取当年开始结束时刻
    :return:
    """
    today = datetime.today()
    start_time = datetime(today.year, 1, 1, 0, 0, 0)
    end_time = datetime(today.year, 12, 31, 23, 59, 59)
    return start_time, end_time


def get_hours(zerofill=True):
    """
    列出1天所有24小时
    :return:
    """
    if zerofill:
        return ['%02d' % i for i in range(24)]
    else:
        return range(24)


def get_days(year=1970, month=1, zerofill=True):
    """
    列出当月的所有日期
    :param year:
    :param month:
    :param zerofill:
    :return:
    """
    year = int(year)
    month = int(month)
    _, days = calendar.monthrange(year, month)
    if zerofill:
        return ['%02d' % i for i in range(1, days+1)]
    else:
        return range(1, days+1)


def get_weeks():
    """
    列出所有星期
    :return:
    """
    return [u'周一', u'周二', u'周三', u'周四', u'周五', u'周六', u'周日']


def get_months(zerofill=True):
    """
    列出1年所有12月份
    :return:
    """
    if zerofill:
        return ['%02d' % i for i in range(1, 13)]
    else:
        return [i for i in range(1, 13)]


def time_local_to_utc(local_time):
    """
    本地时间转UTC时间
    :param local_time:
    :return:
    """
    # 字符串处理
    if isinstance(local_time, str) and len(local_time) == 10:
        local_time = datetime.strptime(local_time, '%Y-%m-%d')
    elif isinstance(local_time, str) and len(local_time) >= 19:
        local_time = datetime.strptime(local_time[:19], '%Y-%m-%d %H:%M:%S')
    elif not (isinstance(local_time, datetime) or isinstance(local_time, date)):
        local_time = datetime.now()
    # 时间转换
    utc_time = local_time + timedelta(seconds=time.timezone)
    return utc_time


def time_utc_to_local(utc_time):
    """
    UTC时间转本地时间
    :param utc_time:
    :return:
    """
    # 字符串处理
    if isinstance(utc_time, str) and len(utc_time) == 10:
        utc_time = datetime.strptime(utc_time, '%Y-%m-%d')
    elif isinstance(utc_time, str) and len(utc_time) >= 19:
        utc_time = datetime.strptime(utc_time[:19], '%Y-%m-%d %H:%M:%S')
    elif not (isinstance(utc_time, datetime) or isinstance(utc_time, date)):
        utc_time = datetime.utcnow()
    # 时间转换
    local_time = utc_time - timedelta(seconds=time.timezone)
    return local_time


def date_to_timestamp(date):
    """
    # 转换成时间戳
    :param date:
    :return:
    """
    timeArray = time.strptime(str(date), "%Y-%m-%d %H:%M:%S")
    timestamp = time.mktime(timeArray)
    return int(timestamp)


def get_utc_timestamp():
    """
    获取当前utc时间戳
    :return:
    """
    return time.time() - 28800


def get_offset_time():
    """
    获取UTC时间和本地时间的偏移量
    :return:
    """
    now_time = time.time()
    local_time = datetime.fromtimestamp(now_time)
    utc_time = datetime.utcfromtimestamp(now_time)
    if local_time >= utc_time:
        offset = int((local_time - utc_time).total_seconds())
    else:
        offset = 0-int((utc_time - local_time).total_seconds())
    return offset


if __name__ == '__main__':
    print (get_current_week_time_ends())
