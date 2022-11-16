''' this file is for IPL prj (Python Data Project) Problem 1 and 2'''
import csv
import matplotlib.pyplot as plt
import constants as const
from functions import bar_plot, get_match_ids_of_a_year

def execute():
    ''' function to get data to plot all graphs'''
    match_ids_of_2016 = get_match_ids_of_a_year("2016")
    match_ids_of_2015 = get_match_ids_of_a_year("2015")

    # get required data from csv in dict and then call appropriate plot functions
    with open(const.CSV_FILE_PROB_1_2_7, encoding="utf-8") as inputfile:
        team_wise_runs = {}
        rcb_playerwise_runs = {}
        extra_runs_in_2016 = {}
        bowlerwise_runs_2015 = {}
        deliveries_reader = csv.DictReader(inputfile)

        for delivery in deliveries_reader:
            runs_in_this_ball = int(delivery['total_runs'])
            batsman_runs_in_this_ball = int(delivery['batsman_runs'])
            extra_runs_in_this_ball = int(delivery['extra_runs'])
            delivery_bowler = delivery['bowler']
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

            if delivery['match_id'] in match_ids_of_2016:
                extra_runs_in_2016[delivery['bowling_team']] = (
                                                            extra_runs_in_2016.get(
                                                                delivery['bowling_team'], 0
                                                            )
                                                            + extra_runs_in_this_ball
                                                            )
            if delivery['match_id'] in match_ids_of_2015:
                bowlerwise_runs_2015[delivery_bowler] = (
                                                            bowlerwise_runs_2015.get(
                                                                delivery_bowler, {}
                                                            )
                                                            )

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
        bar_plot(extra_runs_in_2016, const.TEAM, const.TOT_EXTRA_RUNS, const.EXTRA_RUNS_2016)
        plt.show()

execute() # driver function
