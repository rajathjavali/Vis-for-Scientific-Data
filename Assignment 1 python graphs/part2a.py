import csv
import numpy as np
import matplotlib.pyplot as plt

f = open("data/NOAA-Temperatures.csv")
csvreader = csv.reader(f)

# ignoring header lines
for i in range(1, 6):
    next(csvreader)

year, valueDegC, valueDegF = np.array([]), np.array([]), np.array([])

# copy year, value from csv
for row in csvreader:
    year = np.append(year, float(row[0]))
    valueDegC = np.append(valueDegC, float(row[1]))


#conversion of temperature values from celsius to fahrenheit
for i in range(0, len(valueDegC)):
    valueDegF = np.append(valueDegF, 1.8 * valueDegC[i] + 32)

#ploting farenheit scale
plt.bar(year, valueDegF, align='center', width=0.5, edgecolor='b')
plt.ylim((28,34))
plt.xlabel("Year")
plt.ylabel("F +/- from the average")
plt.title("Bar plot depicting Temperature Changes through years 1880-2017")
plt.show()

# Looking at the data on the whole scale it appears as though there is slight increase in average temperature. 
# But since temperature increase has an adverse efect on all biological aspects on earth, we had to take a closer
# look at the plot. By limiting the range frp, 28 to 34 we can see and increasing temperature trend.
# If this keeps up then its going to cause major problems in the upcoming years. 