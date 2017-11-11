codes = ["0876", "0877", "0878", "0879", "0882", "0883", "0884", "0885", "0886", "0887", "0888", "0889", "0892", "0893", "0894", "0895", "0896", "0897", "0898", "0899", "0988"]

print("Generating valid bulgarian telephone numbers..")
with open("numbers.txt", "a") as file:
    for code in codes:
        for num in range(0, 999999):
            file.write(code + str(format(num, "06d")) + "\n")
        print("%02d%%" % ((codes.index(code)/len(codes))*100), end ="\r")
print("Done!")
