import matplotlib.pyplot as plt
import numpy as np
import random
import pickle

# Part 1 

## Question 1 -  
## Create an array with 200 elements from 1 to 200 in order.
## Create a box plot for visualization of your data.

dataList1 = list(range(1,201))
plt.figure(1)
plt.boxplot(dataList1)
plt.ylabel("Values 1-200")
plt.title("Viz 1 - BoxPlot")
#plt.show()

## Question 2 -  
## Create an array with 10,000 random numbers. Create a histogram
## of the data using 20 bins.

dataList2 = np.random.rand(10000)
plt.figure(2)
plt.hist(dataList2, edgecolor='black', bins=20)
plt.ylabel("Random Values")
plt.xlabel("Bins (Automatic Binning)")
plt.title("Histogram of 10000 Random numbers from Uniform Distribution")
#plt.show()

## Question 3 -  
## Write a program to generate 100 random numbers Gaussian distributed between 
## 1 and 100. Write the numbers out to a binary file and use a line graph
## to draw the 100 numbers.

binFile = open("guassian.bin", "wb")

dataList3_yaxis = np.random.normal(50,25, 100)
dataList3_xaxis = list(range(1,101))

pickle.dump(dataList3_yaxis, binFile)
binFile.close()

plt.figure(3)
plt.plot(dataList3_xaxis, dataList3_yaxis)
plt.ylabel("Random numbers - Guassian Distribution")
plt.xlabel("Instances 1-100")
plt.title("Line Graph of Guassian distribution")
#plt.show()

## Question 4 -  
## Write a program to read the binary file back, divide the range between 1 and 100 
## into 7 intervals, and calculate the frequency for each interval: Display
## a histogram of your result.

binFile_read = open("guassian.bin", "rb")
dataList4 = pickle.load(binFile_read)
plt.figure(4)
n, bins, patches = plt.hist(dataList4, bins=[0,14, 28, 42, 56, 70, 84, 100], edgecolor = 'black')
plt.ylabel("Frequency")
plt.xlabel("Bins")
plt.xticks([0,14, 28, 42, 56, 70, 84, 100])
plt.title("Histogram -Guassian - divided into 7 bins")

# print("The intervals and frequencies considered here are: ")
# for i in range(1, len(bins)):
# 	print("Interval " + str(i) + " : " + str(bins[i-1]) + " - " + str(bins[i]) + " -> " + str(n[i-1]))

binFile_read.close()
plt.show()

