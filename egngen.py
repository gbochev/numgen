import datetime

start_date = datetime.datetime(1960, 1, 1)
end_date = datetime.datetime(1999, 12, 31)
step = datetime.timedelta(days = 1)
weights = [2, 4, 8, 5, 10, 9, 7, 3, 6]

def check_sum(EGN):
    ch_sum = 0
    for w in weights:
        ch_sum += int(EGN[weights.index(w)]) * w
    if ch_sum % 11 < 10:
        return str(ch_sum % 11)
    return "0"

print("Generating valid EGNs from 1960 to 1999..")

with open("egns.txt", "a") as file:
    dt = start_date
    while dt < end_date:
        EGN_date = dt.strftime("%y%m%d")
        for num in range(0, 999):
            EGN = EGN_date
            EGN += str(format(num, "03d"))
            EGN += check_sum(EGN)
            file.write(EGN + "\n")      
        dt += step
        print(str((dt - start_date).days) + "/" + str((end_date - start_date).days), end = "\r")
print("Done!")
