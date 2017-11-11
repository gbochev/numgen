import datetime

dt = datetime.datetime(1960, 1, 1)
end_date = datetime.datetime(2000, 12, 30)
step = datetime.timedelta(days = 1)

print("Generating valid dates from 1960 to 2000..")

with open("dates.txt", "a") as file:
    while dt < end_date:
        file.write(dt.strftime("%y%m%d") + "\n")
        dt += step

print("Done!")
