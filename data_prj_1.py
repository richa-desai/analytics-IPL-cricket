''' this file is for IPL prj (Python Data Project) Problem 1 and 2'''
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

def execute():
    ''' function to get data to plot all graphs'''
    # get required data from csv in dict and then call appropriate plot functions
    with open(const.CSV_FILE_PROB_1_AND_2, encoding="utf-8") as inputfile:
        team_wise_runs = {}
        rcb_playerwise_runs = {}
        deliveries_reader = csv.DictReader(inputfile)

        for delivery in deliveries_reader:
            runs_in_this_ball = int(delivery['total_runs'])
            batsman_runs_in_this_ball = int(delivery['batsman_runs'])

            team_wise_runs[delivery['batting_team']] = (
                                                    team_wise_runs.get(delivery['batting_team'], 0)
                                                    + runs_in_this_ball
                                                   )
            # get() returns current value corresponding to batting team;
            # will return 0 if that team is not yet added

            if delivery['batting_team'] == "Royal Challengers Bangalore":
                rcb_playerwise_runs[delivery['batsman']] = (
                                                    rcb_playerwise_runs.get(delivery['batsman'], 0)
                                                    + batsman_runs_in_this_ball)

        runs_by_rcb_players = list(rcb_playerwise_runs.values())
        runs_by_rcb_players.sort(reverse=True)
        top_ten_runs = runs_by_rcb_players[:const.RCB_TOP_TEN]

        # below way of getting top (say) 10 runs scorer will also get players with same score
        # e.g. 10th and 11th player has same runs, hence both players will be showed in the graph
        rcb_top_player_runs = {}
        for value in top_ten_runs:
            key = list(rcb_playerwise_runs.keys())[list(rcb_playerwise_runs.values()).index(value)]
            rcb_top_player_runs[key] = rcb_playerwise_runs[key]

        bar_plot(team_wise_runs, const.TEAM, const.TOT_RUNS, const.TEAM_GRAPH_TITLE)
        bar_plot(rcb_top_player_runs, const.PLAYERS, const.TOT_RUNS, const.RCB_GRAPH_TITLE)
        plt.show()

execute() # driver function
