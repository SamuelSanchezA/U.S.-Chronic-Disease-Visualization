import os
import webbrowser
import csv
import Definitions as dfi

def main():
    #lists and dictionaries used for this instance
    states=[]
    states2 = {}
    catagory=[]
    catagoryDict={}

    #imports the csv file and appends the data to corrisponding lists
    with open('U.S._Chronic_Disease_Indicators__CDI_.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            states.append(row[1])
            catagory.append(row[3])

    #sorts lists into dictionaries without duplicates
    dfi.classify(catagory, catagoryDict)
    dfi.classify(states, states2)

    #counts frequency of diseases and adds to corrisponding key in dictionary
    dfi.count(catagory, catagoryDict)

    #generates wordcloud using list of diseases
    dfi.wordcloud(catagory)
    #generates color plot using list of deiseases and dictionary of states
    dfi.colorize(catagory, states2)

    #opens html file
    webbrowser.open("htmlthing.html")

if __name__ == "__main__":
    main();
