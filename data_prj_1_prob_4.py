''' this file is for IPL prj (Python Data Project) Problem 4'''
import csv
import matplotlib.pyplot as plt
import constants as const
from functions import bar_plot, stacked_chart_plot

def execute():
    ''' function to get data to plot graphs'''
    # get required data from csv in dict and then call plot function
    with open(const.CSV_FILE_PROB_4_5, encoding="utf-8") as inputfile:
        season_details = {}
        yearwise_matches_played = {}
        matches_reader = csv.DictReader(inputfile)

        for match in matches_reader:
            season_year = int(match['season'])
            team1 = match['team1']
            team2 = match['team2']
            season_details[season_year] = (
                                        season_details.get(season_year,{})
                                        )
            season_details[season_year][team1] = (
                                                season_details[season_year].get(team1, 0)
                                                + 1
                                                )
            season_details[season_year][team2] = (
                                                season_details[season_year].get(team2, 0)
                                                + 1
                                                )
            yearwise_matches_played[season_year] = (
                                                    yearwise_matches_played.get(season_year, 0)
                                                    + 1
                                                )

        stacked_chart_plot(season_details, const.TEAM,
                            const.MATCHES_PLAYED, const.MATCHES_BY_TEAM_BY_SEASON
                            )
        bar_plot(yearwise_matches_played, const.YEAR,
                 const.MATCHES_PLAYED, const.MATCHES_BY_TEAM_BY_YEAR
                 )
        # show plot
        plt.show()

execute() # driver function
