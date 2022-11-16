''' This file has all the functions '''

import matplotlib.pyplot as plt

def bar_plot(bar_plot_data: dict, xlabel: str, ylabel: str, title: str):
    """Pass dict variable having keys to plot on x-axis and pass values to plot on y-axis"""
    # initialisation
    x_axis_keys = list(bar_plot_data.keys())
    y_axis_values = list(bar_plot_data.values())
    fig = plt.figure()

    # creating the bar plot
    plt.bar(x_axis_keys, y_axis_values)
    fig.autofmt_xdate() # gives rotation to the x axis titles
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.tight_layout()
    plt.xticks(x_axis_keys)

def stacked_chart_plot(stacked_chart_data: dict, x_lable:str, y_lable:str, title: str):
    """Pass dict variable having keys as seasons
    and pass values that are sub dictionaries with teams and total matches played
    e.g. {2008: {RCB: 10, MI: 9, ...}, 2017: {RCB: 10, MI: 9, ...}, ...}
    """
    # get all teams
    teams = set()
    for values in stacked_chart_data.values():
        for keys in values.keys():
            teams.add(keys)
    teams=list(teams)
    # get season 1 team wise total matches played
    all_seasons = sorted(stacked_chart_data.keys())
    seasonwise_matches_played_by_all_teams = []
    i=0
    for season in all_seasons:
        seasonwise_matches_played_by_all_teams.append([])
        for team in teams:
            seasonwise_matches_played_by_all_teams[i].append(stacked_chart_data[season].get(team,0))
        i+=1

    # Creating plot
    fig = plt.figure()
    stack_current_height = [0]*len(teams)
    for season_matches in seasonwise_matches_played_by_all_teams:
        plt.bar(teams, season_matches, bottom = stack_current_height)
        stack_current_height = [sum(x) for x in zip(season_matches, stack_current_height)]

    fig.autofmt_xdate() # gives rotation to the x axis titles
    plt.title(title)
    plt.legend(all_seasons)
    plt.xlabel(x_lable)
    plt.ylabel(y_lable)
    plt.tight_layout()

def piechart_plot(pie_plot_data: dict, title: str):
    """Pass dict variable having keys to set the label of each wedge
    and pass values that represents the array of data values to be plotted
    """
    # Creating plot
    plt.pie(pie_plot_data.values(), labels = pie_plot_data.keys(), autopct='%1.0f%%')
    plt.title(title)
