import os
import glob
import csv
import time

def unix_time(raw_date):
    t = time.strptime(raw_date,"%m/%d/%y %H:%M %Z")
    unix_time = time.mktime(t)
    return unix_time

ride_files = glob.glob("/Users/George/Desktop/rides/q4 rides.csv")

for file in ride_files:
    with open(file,"rb") as infile, open("rides_compiled.txt", "a") as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        next(reader)

        for row in reader:
            # print str(row[1])
            try:
                start_time = unix_time(row[1]+" EST")
                end_time = unix_time(row[2]+" EST")
                bike_id = row[3]
                from_id = row[5]
                to_id = row[7]
                customer_type = row[9]
                if row[5] == "":
                    from_id = 0
                if row[7] == "":
                    to_id = 0
                if row[9] == "":
                    customer_type = "Unknown"

                writer.writerow([row[0],start_time,end_time,bike_id,from_id,to_id,customer_type])

            except:
                print row[1]
                pass