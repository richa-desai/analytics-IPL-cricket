''' this file is for IPL prj (Python Data Project) Problem 3'''
import csv
import matplotlib.pyplot as plt
import constants as const
from functions import piechart_plot

def execute():
    ''' function to get data to plot graphs'''
    # get required data from csv in dict and then call plot function
    with open(const.CSV_FILE_PROB_3, encoding="utf-8") as inputfile:
        country_wise_umpire = {}
        umpires_reader = csv.DictReader(inputfile)

        for umpire in umpires_reader:
            country_of_umpire = umpire[' country'].strip()
            if country_of_umpire != const.INDIA :
                country_wise_umpire[country_of_umpire] = (
                                                        country_wise_umpire.get(country_of_umpire,0)
                                                        + 1
                                                    )
        piechart_plot(country_wise_umpire, const.UMPIRES_GRAPH_TITLE)
        # show plot
        plt.show()

execute() # driver function
