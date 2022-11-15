''' this file is for IPL prj (Python Data Project) Problem 4'''
import csv
import matplotlib.pyplot as plt
import constants as const

def stacked_chart_plot(stacked_chart_data: dict, title: str):
    """Pass dict variable having keys as seasons
    and pass values that are sub dictionaries with teams and total matches played
    e.g. {s1: {RCB: 10, MI: 9, ...}, s2: {RCB: 10, MI: 9, ...}, ...}
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
            seasonwise_matches_played_by_all_teams[i].append(stacked_chart_data[season].get(team, 0))
        i+=1
        
    # Creating plot
    fig = plt.figure()
    stack_current_height = [0]*len(teams)
    for season_matches in seasonwise_matches_played_by_all_teams:
        plt.bar(teams, season_matches, bottom = stack_current_height)
        stack_current_height = [sum(x) for x in zip(season_matches, stack_current_height)]
        
    # plt.bar(teams, season2_matches_played_by_all_teams, bottom=season1_matches_played_by_all_teams)
    fig.autofmt_xdate() # gives rotation to the x axis titles
    plt.title(title)

def execute():
    ''' function to get data to plot graphs'''
    # get required data from csv in dict and then call plot function
    with open(const.CSV_FILE_PROB_4, encoding="utf-8") as inputfile:
        season_details = {}
        matches_reader = csv.DictReader(inputfile)

        for match in matches_reader:
            season_year = int(match['season'])
            team1_of_match = match['team1']
            team2_of_match = match['team2']
            season_details[season_year] = (
                                        season_details.get(season_year,{})
                                        )
            season_details[season_year][team1_of_match] = (
                                                        season_details[season_year].get(team1_of_match, 0)
                                                        + 1
                                                        )
            season_details[season_year][team2_of_match] = (
                                                        season_details[season_year].get(team2_of_match, 0)
                                                        + 1
                                                        )
        
        stacked_chart_plot(season_details, const.UMPIRES_GRAPH_TITLE)
        # show plot
        plt.show()

execute() # driver function
