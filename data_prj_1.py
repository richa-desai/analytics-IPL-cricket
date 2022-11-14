#!/usr/bin/env python
# encoding: utf-8
''' this file is for IPL prj question 1'''
import csv
import matplotlib.pyplot as plt
import constants as const

def bar_plot(all_team_wise_runs: dict, xlabel: str, ylabel: str, title: str):
    """Pass keys in dict to plot on x-axis and pass values to plot on y-axis"""
    # initialisation
    teams = list(all_team_wise_runs.keys())
    tot_runs = list(all_team_wise_runs.values())
    fig = plt.figure()

    # creating the bar plot
    plt.bar(teams, tot_runs, color ='maroon',
            width = 0.2)
    fig.autofmt_xdate() # gives rotation to the x axis titles
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.tight_layout()
    plt.show()

# first get required data from csv in dict
with open('deliveries.csv', encoding="utf-8") as inputfile:
    team_wise_runs = {}
    rcb_playerwise_runs = {}
    reader = csv.DictReader(inputfile)
    next(reader, None)  # skip the header row
    for row in reader:
        runs_in_this_ball = int(row['total_runs'])
        batsman_runs_in_this_ball = int(row['batsman_runs'])

        team_wise_runs[row['batting_team']] = (team_wise_runs.get(row['batting_team'], 0) +
        runs_in_this_ball)

        if row['batting_team'] == "Royal Challengers Bangalore":
            rcb_playerwise_runs[row['batsman']] = (rcb_playerwise_runs.get(row['batsman'], 0)
                                                   + batsman_runs_in_this_ball)

    # below way of getting top 10 runs scorer will also get players with same score
    # e.g. 10th and 11th player has same runs, hence both players will be showed in the graph
    runs_by_rcb_players = list(rcb_playerwise_runs.values())
    runs_by_rcb_players.sort(reverse=True)
    top_ten_runs = runs_by_rcb_players[:10]

    rcb_top_player_runs = {}
    for value in top_ten_runs:
        key = list(rcb_playerwise_runs.keys())[list(rcb_playerwise_runs.values()).index(value)]
        rcb_top_player_runs[key] = rcb_playerwise_runs[key]

    bar_plot(team_wise_runs, const.TEAM, const.TOT_RUNS, const.TEAM_GRAPH_TITLE)
    bar_plot(rcb_top_player_runs, const.PLAYERS, const.TOT_RUNS, const.RCB_GRAPH_TITLE)
