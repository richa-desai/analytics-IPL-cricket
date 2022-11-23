''' this file is for IPL prj (Python Data Project) Problem 1, 2, 7 and 8'''
import csv
import matplotlib.pyplot as plt
import constants as const
from functions import bar_plot, get_match_ids_of_a_year, get_top_n_batsman, get_top_n_bowlers


def execute():
    ''' function to get data to plot all graphs'''
    match_ids_of_2016 = get_match_ids_of_a_year("2016", "matches.csv")
    match_ids_of_2015 = get_match_ids_of_a_year("2015", "matches.csv")

    # get required data from csv in dict and then call appropriate plot functions
    with open(const.CSV_FILE_PROB_1_2_7_8, encoding="utf-8") as inputfile:
        team_wise_runs = {}
        rcb_playerwise_runs = {}
        extra_runs_in_2016 = {}
        bowlerwise_runs_2015 = {}
        deliveries_reader = csv.DictReader(inputfile)
        ball_count = "Ball count"
        bowler_run = "Bowler runs"

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
                bowlerwise_runs_2015[delivery_bowler][bowler_run] = (
                    bowlerwise_runs_2015[delivery_bowler].get(
                        bowler_run, 0
                    )
                    + int(delivery['total_runs'])
                )
                bowlerwise_runs_2015[delivery_bowler][ball_count] = (
                    bowlerwise_runs_2015[delivery_bowler].get(
                        ball_count, 0
                    )
                    + 1
                )

        rcb_top_player_runs = get_top_n_batsman(
            rcb_playerwise_runs, const.RCB_TOP_TEN)
        top_bowlers_of_2015 = get_top_n_bowlers(
            bowlerwise_runs_2015, const.RCB_TOP_TEN)

        bar_plot(team_wise_runs, const.TEAM,
                 const.TOT_RUNS, const.TEAM_GRAPH_TITLE)
        bar_plot(rcb_top_player_runs, const.PLAYERS,
                 const.TOT_RUNS, const.RCB_GRAPH_TITLE)
        bar_plot(extra_runs_in_2016, const.TEAM,
                 const.TOT_EXTRA_RUNS, const.EXTRA_RUNS_2016)
        bar_plot(top_bowlers_of_2015, const.PLAYERS,
                 const.ECONOMY, const.TOP_BOWLER_2015)
        plt.show()


execute()  # driver function
