import os
import csv
import time
from datetime import datetime
import calendar
from pprint import pprint

sum_day = dict()

with open("rides_day.csv",'rb') as infile:
    reader = csv.reader(infile)
    next(reader)
    for row in reader:
        r_date = datetime.fromtimestamp(float(row[0]))
        day = calendar.day_name[r_date.weekday()]
        if day in sum_day:
            sum_day[day] = int(sum_day[day]) + int(row[1])
        else:
            sum_day[day] = row[1]

days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
#
# with open("punch_day.csv",'a') as out:
#     writer = csv.writer(out)
#     writer.writerow(["Day, Count"])
#     for day in days:
#         count = sum_day[day]
#         writer.writerow([day,count])


# sum_hour_day = dict()
#
# with open("rides_hour.csv",'rb') as infile:
#     reader = csv.reader(infile)
#     next(reader)
#     for row in reader:
#         r_date = datetime.fromtimestamp(float(row[0]))
#         day = calendar.day_name[r_date.weekday()]
#         hour = r_date.hour
#         if day in sum_hour_day:
#             sum_hour_day[day][hour] = int(sum_hour_day[day][hour]) + int(row[1])
#         else:
#             l = list()
#             for x in range(0,24):
#                 l.append(int(0))
#             sum_hour_day[day] = l
#             sum_hour_day[day][hour] = row[1]
#
#
# days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
# with open("punch_hour.csv",'a') as out:
#     writer = csv.writer(out)
#     l = list()
#     l.append("")
#     for x in range(0,24):
#         l.append(x)
#     writer.writerow(l)
#     for day in days:
#         sum_hour_day[day].insert(0,day)
#         writer.writerow(sum_hour_day[day])