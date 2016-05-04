import os
import webbrowser
import csv

import Definitions as dfi

def main():
    dates=[]
    datesDict={}
    states=[]
    statesDict={}
    catagory=[]
    catagoryDict={}

    with open('U.S._Chronic_Disease_Indicators__CDI_.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            dates.append(row[0])
            states.append(row[1])
            catagory.append(row[3])

    dfi.classify(catagory, catagoryDict)
    dfi.classify(dates, datesDict)
    dfi.classify(states, statesDict)
    dfi.count(catagory, catagoryDict)
    dfi.count(dates, datesDict)
    dfi.count(states, statesDict)


    dfi.wordcloud(catagory)
    dfi.colorize("al", catagory)

    #opens html file
    webbrowser.open("htmlthing.html")

if __name__ == "__main__":
    main();
