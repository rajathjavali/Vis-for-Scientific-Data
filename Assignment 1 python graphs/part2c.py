import csv
import numpy as np
import matplotlib.pyplot as plt

f = open("data/us_birth.csv")
csvreader = csv.reader(f)

#skip the first header information line
next(csvreader)

year = np.array([])
date_of_month ={}
for i in range(1, 32):
    date_of_month[i] = 0

data = []
for row in csvreader:
    data.append(row)
    year = np.append(year, row[0])
    date_of_month[int(row[2])] += int(row[4])

max_value = max(date_of_month.values())
date = [k for k, v in date_of_month.items() if v == max_value]
print("The day with highest number of births is: %s and the birth count is %d\n"% (date[0], max_value))

min_value = min(date_of_month.values())
min_date = [k for k, v in date_of_month.items() if v == min_value]
print("The day with lowest number of births is: %s and the birth count is %d\n"% (min_date[0], min_value))

counter_summer, counter_winter = 0, 0
counter_summer = sum(int(row[4]) for row in data if row[1] == '5' or row[1] == '6' or row[1] == '7' or row[1] == '8')
counter_winter = sum(int(row[4]) for row in data if row[1] == '1' or row[1] == '2' or row[1] == '11' or row[1] == '12')

print("Number of Birthdays in Winter %d and number of Birthdays in Summers are %d. "
      "It can be concluded that winters have less births than summers.\n" % (counter_winter, counter_summer))

fri_13 = sum(int(p[4]) for p in data if p[2] == '13' and p[3] == '5')
#print(friday13)
print("Number of Birthdays on Friday the 13th: %d" % fri_13)
