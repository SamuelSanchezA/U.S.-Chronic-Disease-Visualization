import csv
import os
#from scipy.misc import imread
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import random
from PIL import Image


#sorts, adds, and creates dict of catagories without duplicates
def classify(origional, new):
    origional = sorted([i.lower() for i in origional])
    for i in range(2,len(origional)-1):
        if origional[i] != origional[i-1] and origional[i] != "category" and origional[i] != "locationabbr":
            new[origional[i]] = 0


#counts amount of each catagory and adds number to corresponding list key
def count(listi, dicti):
    listi = sorted([i.lower() for i in listi])
    leng = len(dicti)
    for i in listi:
        if i in dicti:
            dicti[i] +=1


#creates color pallette of wordcloud
def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)


#craetes wordcloud and saves it to an image
def wordcloud(wordSource):
    ##writes origional catagory list to text file
    d = os.path.dirname(__file__)
    file = open("catagory.txt", 'w')
    for item in wordSource:
        file.write("%s\n" % item)
    thefile = open(os.path.join(d, "catagory.txt")).read()

    #adds words to exclude
    STOPWORDS.add("chronic")
    STOPWORDS.add("disease")
    STOPWORDS.add("obstructive")
    STOPWORDS.add("status")

    # generate word cloud
    wordcloud = WordCloud(stopwords=STOPWORDS,
        background_color="black",
        width = 650,
        height = 250).generate_from_text(thefile)

    #re-colers and saves wordcloud as png
    wordcloud.recolor(color_func=grey_color_func, random_state=3)
    wordcloud.to_file("wordcloud.png")

    #cloud1_coloring = imread(os.path.join(d, "CloudColor.png")).read()


#converts numbers to range of 0-255 for rgb
def convert(oldMin, oldMax, oldValue):
    oldRange = (oldMax - oldMin)
    newValue = (((oldValue - oldMin) * 255) / oldRange) + 0
    return newValue


#uses values from convert() to generate the hue of a specified colorize
#saves to image
def colorize(domain, catagories):
    local = {}
    newCats = []
    with open('U.S._Chronic_Disease_Indicators__CDI_.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if (row[1].lower() == str(domain)):
                newCats.append(row[3].lower())
    classify(newCats, local)
    count(newCats, local)
    """
    local is to contain the frequency for catagory(such as diseases)
    that apply to the
    domain (such as a specific state).
    """
    #smiply checking
    for i in local:
        print (i + ": " + str(local[i]))

    newList = [0]
    for i in local:
        newList.append(local[i])
    print("newList")
    print(newList)
    #find min and max of data
    oldMin = newList[0]
    oldMax = newList[0]
    for i in newList:
        if (int(i) < oldMin):
            oldMin = int(i)
        if (int(i) > oldMax):
            oldMax = int(i)
    if oldMin == 0:
        oldmin = 1

    #use min and max to convert local's key values to rgb range
    for i in local:
        local[i] = int(convert(oldMin, oldMax, local[i]))

    print (local)
"""
    rgb = (255,255,255)
    res = (800,300)
    newimage = Image.new("RGB",res,rgb)
    newImageData = newimage.load()

    for x in range(pixstart,pixend):
        for y in range(0,300):
            newImageData[x,y] = (255, int(num),int(num))
    newimage.save("colortest.png")
"""

def printDict(Dict):
    print("")
    for i in Dict:
        print (i + ": " + str(Dict[i]))
