''' this file is for IPL prj question 1'''
import csv
import matplotlib.pyplot as plt

team_runs_dict = {}

# first get required data from csv in dict
with open('deliveries.csv', encoding="utf-8") as inputfile:
    reader = csv.DictReader(inputfile)
    next(reader, None)  # skip the header row
    print("hello")
    for row in reader:
        team_runs_dict[row['batting_team']] = team_runs_dict.get(row['batting_team'], 0) + 1
    print(team_runs_dict)

# use dict values to plot a bar graph
teams = list(team_runs_dict.keys())
tot_runs = list(team_runs_dict.values())
fig = plt.figure()

# creating the bar plot
plt.bar(teams, tot_runs, color ='maroon',
        width = 0.2)
fig.autofmt_xdate() # gives rotation to the x axis titles
plt.xlabel("Team")
plt.ylabel("Total Runs")
plt.title("Total runs scored by each teams over the history of IPL")
plt.tight_layout()
plt.show()
