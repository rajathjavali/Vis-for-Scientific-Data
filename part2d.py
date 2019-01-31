import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv

def merged_bar_plot():
 	f = open("data/KPHL.csv")
 	csvreader = csv.reader(f)
	next(csvreader)
	data = []
	max_temp = np.array([])
	mean_temp = np.array([])
	min_temp = np.array([])
	for row in csvreader:
		data.append(row)
		max_temp = np.append(max_temp, row[3])
		mean_temp = np.append(mean_temp, row[1])
		min_temp = np.append(min_temp, row[2])
	max_temp = max_temp.astype(int)
	mean_temp = mean_temp.astype(int)
	min_temp = min_temp.astype(int)
	## Plot the bar plots
	fig = plt.figure(figsize=(80, 20))
	ax = fig.add_subplot(111)
	instance = np.arange(len(max_temp))
	r1 = ax.bar(instance-0.2, max_temp, width=0.2, color='b', align='center')
	r2 = ax.bar(instance, mean_temp, width=0.2, color='g', align='center')
	r3 = ax.bar(instance+0.2, min_temp, width=0.2, color='yellow', align='center')
	# ax.set_xticks(instance)
	ax.autoscale(tight = True)
	plt.ylim((0,100))
	ax.legend((r1, r2, r3), ('max_temp', 'mean_temp', 'min_temp'), fontsize = 'large')
	plt.xlabel("July 2014 - June 2015")
	plt.ylabel("Temperature in Farenheit")
	plt.title("Bar Plot depecting total waterborne commerce throughout the years")
	plt.show()

def lineplot():
	f = open("data/bad_drivers.csv")
	csvreader = csv.reader(f)
	next(csvreader)
	states = np.array([])
	drivers = np.array([])
	premiums = np.array([])
	loss = np.array([])

	for row in csvreader:
		states = np.append(states, row[0])
		drivers = np.append(drivers, row[1])
		premiums = np.append(premiums, row[6])
		loss = np.append(loss, row[7])

	drivers = drivers.astype(float)
	premiums = premiums.astype(float)
	loss = loss.astype(float)
	drivers = [k * 10 for k in drivers]
	premiums = [k / 10 for k in premiums]

	r1, = plt.plot(states, drivers, 'b--')
	r2, = plt.plot(states, premiums, 'r-')
	r3, = plt.plot(states, loss, 'y-')
	plt.autoscale(tight=True)
	plt.xticks(states, rotation=90)
	plt.legend((r1, r2, r3), ('Num drivers per 100 million miles', 'Insurance Premiums (*10 $)', 'Losses to insurance companies ($)'), fontsize = 'small')
	plt.title("Bad Driver stats - statewize")
	plt.grid()
	plt.show()

def parallel_plot():
	df = pd.read_csv("data/hate_crimes.csv")
	df = df.drop(['share_non_citizen','share_white_poverty','gini_index','share_non_white','share_voters_voted_trump','hate_crimes_per_100k_splc','avg_hatecrimes_per_100k_fbi'], axis =1)
	# df = df.sample(n=100)
	# df.party = df.party.replace({"R":0 ,"D": 10,"I":20, "AL":30,'L':40,'ID':50})
	# df.state = df.incumbent.replace({"Yes":0,"No":80})
	# df.chamber = df.chamber.replace({"house":25,"senate":75})

	pd.to_numeric('median_household_income',errors='coerce')
	pd.to_numeric('share_unemployed_seasonal',errors='coerce')
	pd.to_numeric('share_population_in_metro_areas',errors='coerce')
	pd.to_numeric('share_population_with_high_school_degree',errors='coerce')
	df.median_household_income = [float(k) / 100000 for k in df.median_household_income]

	# print(df)
	plt.figure()
	pd.plotting.parallel_coordinates(
		df[['state', 'median_household_income', 'share_unemployed_seasonal', 'share_population_in_metro_areas', 'share_population_with_high_school_degree']], 
		'state')
	plt.show()

	

merged_bar_plot()
lineplot ()
parallel_plot()
