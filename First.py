import csv
import os
#from scipy.misc import imread
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import random
import webbrowser
from PIL import Image


dates=[]
datesDict={}
states=[]
statesDict={}
catagory=[]
catagoryDict={}


def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)


STOPWORDS.add("chronic")
STOPWORDS.add("disease")
STOPWORDS.add("obstructive")
STOPWORDS.add("status")
#cloud1_coloring = imread(os.path.join(d, "CloudColor.png")).read()
#sorts and adds and creates dict of catagories without duplicates
def classify(origional, new):
    origional = sorted([i.lower() for i in origional])
    for i in range(2,len(origional)-1):
        if origional[i] != origional[i-1] and origional[i] != "category" and origional[i] != "locationabbr":
            new[origional[i]] = 0
#counts amount of each catagory and adds number to corresponding list key
def count(list, dict):
    list = sorted([i.lower() for i in list])
    leng = len(dict)
    for i in list:
        if i in dict:
            dict[i] +=1

classify(catagory, catagoryDict)
classify(dates, datesDict)
classify(states, statesDict)
count(catagory, catagoryDict)
count(dates, datesDict)
count(states, statesDict)
#end of organizing lists and dictionaries ######################################################

#wordcloud stuff ##############################################################
with open('U.S._Chronic_Disease_Indicators__CDI_.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        dates.append(row[0])
        states.append(row[1])
        catagory.append(row[3])

##writes origional catagory list to text file
d = os.path.dirname(__file__)
file = open("catagory.txt", 'w')
for item in catagory:
    file.write("%s\n" % item)
thefile = open(os.path.join(d, "catagory.txt")).read()

# generate word cloud
wordcloud = WordCloud(stopwords=STOPWORDS, background_color="black", width = 650, height = 250).generate_from_text(thefile)

#### show wordcloud ####################
wordcloud.recolor(color_func=grey_color_func, random_state=3)
wordcloud.to_file("wordcloud.png")

#End of wordcloud###################################################


def convert(oldMin, oldMax, oldValue):
    oldRange = (oldMax - oldMin)
    newValue = (((oldValue - oldMin) * 255) / oldRange) + 0
    return newValue

def colorize(pixstart, pixend, domain, amounts, catagories):
    local = {}
    classify(catagories, local)
    with open('U.S._Chronic_Disease_Indicators__CDI_.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if (row[1] == domain):
                local[row[3].lower] += 1

    for i in local:
        print (i + ": " + str(local[i]))

    newList = []
    for i in local:
        newList.append(i)

    oldMin = newList[0]
    newMax = newList[0]
    for i in newList:
        if (i < oldMin):
            oldMin = i
        if (i > oldMax):
            oldMax = i

    convert(oldMin, oldMax, oldValue)

    rgb = (255,255,255)
    res = (800,300)
    newimage = Image.new("RGB",res,rgb)
    newImageData = newimage.load()

    for x in range(pixstart,pixend):
        for y in range(0,300):
            newImageData[x,y] = (255, int(num),int(num))
    newimage.save("colortest.png")

########################################

#opens html file
webbrowser.open("htmlthing.html")

#prints info
print ("")
for i in catagoryDict:
    print (i + ": " + str(catagoryDict[i]))
print("")
for i in statesDict:
    print (i + ": " + str(statesDict[i]))
print("")
for i in datesDict:
    print (i + ": " + str(datesDict[i]))
