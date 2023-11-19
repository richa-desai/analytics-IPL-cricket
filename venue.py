''' Max matched played at which venue? '''
import csv

def calculate():
    ''' create dict '''
    with open("matches.csv", encoding="utf-8") as inputfile:
        venuewise_matches = {}
        venue_reader = csv.DictReader(inputfile)

        for venue in venue_reader:
            match_played_in = venue['venue']
            venuewise_matches[match_played_in] = (
                venuewise_matches.get(match_played_in, 0) + 1
            )
    return venuewise_matches

def transform(venuewise_matches: dict):
    ''' Get most played venue'''
    all_values = venuewise_matches.values()
    max = 0
    for value in all_values:
        if value > max:
            max = value
    max_played_venue = list(venuewise_matches.keys())[list(venuewise_matches.values()).index(max)]
    return max_played_venue

def execute():
    ''' function to get data'''
    # get required data from csv in dict
    venuewise_matches = calculate()
    print(venuewise_matches)
    max_played_venue = transform(venuewise_matches)
    print(max_played_venue)

execute()  # driver function
