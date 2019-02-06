import os
import glob
import csv
import time

weather_files = glob.glob("/Users/George/Desktop/weather data/*")
#weather_files = weather_files[:1]
i = 0
for file in weather_files:
    with open(file,"rb") as infile, open("weather_compiled.txt", "a") as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        next(reader)
        next(reader)
        next(reader)
        next(reader)
        next(reader)
        next(reader)

        for row in reader:
            if len(row) > 1:
                year = row[1][:4]
                month = row[1][4:][:2]
                day = row[1][4:][2:]
                hour = row[2][:2]
                concat_date = str(year) + " " + str(month) + " " + str(day) + " " + str(hour) + " EST"
                date = time.strptime(concat_date,"%Y %m %d %H %Z")
                unix_time = time.mktime(date)
                temp = row[10]
                writer.writerow([i,unix_time, temp])
                i=i+1