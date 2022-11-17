''' This file has all the functions '''
import csv
import matplotlib.pyplot as plt
import constants as const

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

def get_match_ids_of_a_year(year: str):
    ''' function to get match ids of year 2016'''
    matches_reader = csv.reader(open(r"matches.csv", encoding="utf-8"))
    filtered_matches = list(filter(lambda match: year == match[1], matches_reader))

    match_ids_of_2016 = []
    for match in filtered_matches:
        match_ids_of_2016.append(match[0])
    return match_ids_of_2016

def get_top_n_batsman(playerwise_runs: dict, top_n: int):
    ''' function to get top n batsman'''
    runs_by_batsman = list(playerwise_runs.values())
    runs_by_batsman.sort(reverse = True)
    top_n_runs = runs_by_batsman[:top_n]

    # below way of getting top (say) 10 runs scorer will also get players with same score
    # e.g. 10th and 11th player has same runs, hence both players will be showed in the graph
    top_player_runs = {}
    for value in top_n_runs:
        key = list(playerwise_runs.keys())[list(playerwise_runs.values()).index(value)]
        top_player_runs[key] = playerwise_runs[key]

    return top_player_runs

def get_top_n_bowlers(bowlerwise_runs: dict, top_n: int):
    ''' function to get top n bowlers'''
    ball_count = "Ball count"
    bowler_run = "Bowler runs"
    for bowler in bowlerwise_runs:
        bowlerwise_runs[bowler] = (
            bowlerwise_runs[bowler][bowler_run] / bowlerwise_runs[bowler][ball_count]
            )

    runs_bowler = list(bowlerwise_runs.values())
    runs_bowler.sort()
    bottom_n_average = runs_bowler[:top_n]

    top_bowler_economy = {}
    for value in bottom_n_average:
        key = list(bowlerwise_runs.keys())[list(bowlerwise_runs.values()).index(value)]
        top_bowler_economy[key] = bowlerwise_runs[key]

    return top_bowler_economy
