import csv
import numpy as np
import matplotlib.pyplot as plt
from math import pi
import pandas as pd

# refered Stack overflow https://stackoverflow.com/questions/42227409/tutorial-for-python-radar-chart-plot
def StarPlot_State_Age():
    file = open("data/congress_by_age.csv")
    csvreader = csv.reader(file)
    next(csvreader)

    data = []
    avg_age = []
    state_age = {}
    state_age_count = {}
    for row in csvreader:
        if len(row) > 2:
            if row[8] not in state_age:
                state_age[row[8]] = float(row[12])
                state_age_count[row[8]] = 1
            else:
                state_age[row[8]] += float(row[12])
                state_age_count[row[8]] += 1

    for key in state_age:
        data.append(key)
        avg_age.append(state_age[key]/state_age_count[key])

    length = len(data)

    x_as = [index / float(length) * 2 * pi for index in range(length)]

    # Because our chart will be circular we need to append a copy of the first
    # value of each list at the end of each list with data
    avg_age.append(avg_age[0])
    x_as.append(x_as[0])


    # Set color of axes
    plt.rc('axes', linewidth=0.5, edgecolor="#888888")


    # Create polar plot
    ax = plt.subplot(111, polar=True)


    # Set clockwise rotation. That is:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)


    # Set position of y-labels
    ax.set_rlabel_position(0)


    # Set color and linestyle of grid
    ax.xaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)
    ax.yaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)


    # Setting radial axes and remove labels
    plt.xticks(x_as[:-1], [])

    # Set yticks
    plt.yticks([10, 20, 30, 40, 50, 60], ["10", "20", "30", "40", "50", "60"])
    
    # Plot data
    ax.plot(x_as, avg_age, linewidth=0, linestyle='solid', zorder=3)

    # Fill area
    ax.fill(x_as, avg_age, 'b', alpha=0.3)

    # Set axes limits
    plt.ylim(0, 100)


    # Draw ytick labels to make sure they fit properly
    for i in range(length):
        angle_rad = i / float(length) * 2 * pi

        if angle_rad == 0 or angle_rad == pi:
            ha, distance_ax = "center", 1
        elif 0 < angle_rad < pi:
            ha, distance_ax = "left", 1
        else:
            ha, distance_ax = "right", 1

        ax.text(angle_rad, 100 + distance_ax, data[i], size=10, horizontalalignment=ha, verticalalignment="center")
    plt.title("Star plot with avg age of politicians - statewise")
    plt.show()


# reference http://benalexkeen.com/parallel-coordinates-in-matplotlib/
def parallel_plot_state_ages():
    df=pd.read_csv("data/congress_by_age.csv")
    df = df.drop(['bioguide', 'firstname', 'lastname', 'middlename', 'suffix', 'birthday', 'termstart'], axis =1)

    # df = df.sample(n=100)
    # df.party = df.party.replace({"R":0 ,"D": 10,"I":20, "AL":30,'L':40,'ID':50})
    df.incumbent = df.incumbent.replace({"Yes":0,"No":80})
    df.chamber = df.chamber.replace({"house":25,"senate":75})

    pd.to_numeric('party',errors='coerce')
    pd.to_numeric('chamber',errors='coerce')
    pd.to_numeric('congress',errors='coerce')
    pd.to_numeric('age',errors='coerce')
    # print(df)
    plt.figure()
    pd.plotting.parallel_coordinates(
        df[['age', 'congress', 'chamber', 'party', 'incumbent']], 
        'party', color=['yellow','orange','blue','green','red','black'])
    plt.show()


StarPlot_State_Age()
parallel_plot_state_ages()
# plt.show()