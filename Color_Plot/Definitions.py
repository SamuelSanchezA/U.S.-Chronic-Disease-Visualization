import csv
import os
from wordcloud import WordCloud, STOPWORDS
import random
from PIL import Image, ImageFont, ImageDraw


#sorts and adds to dictionary of catagories without duplicates
def classify(origional, new):
    #sorts origional list in alpabetical order
    origional = sorted([i.lower() for i in origional])
    #if an item does not match the item before it, add it to the dictionary
    for i in range(2,len(origional)-1):
        if origional[i] != origional[i-1] and origional[i] != "category" and  origional[i] != "locationabbr":
            new[origional[i]] = 0
    #the exclusion of "catagory" and "locationabbr" are unique to this csv file


#counts amount of each catagory and adds number to corresponding list key
def count(listi, dicti):
    #makes certain that the passed list is sorted
    listi = sorted([i.lower() for i in listi])
    leng = len(dicti)
    for i in listi:
        if i in dicti:
            dicti[i] +=1


#creates color pallette of wordcloud
def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    #change value of colors by changing areguents of randint
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 70)
    #only shades of grey


#craetes wordcloud and saves it to png "wordcloud.png"
def wordcloud(wordSource):
    #writes origional catagory list to text file
    d = os.path.dirname(__file__)
    file = open("catagory.txt", 'w')
    for item in wordSource:
        file.write("%s\n" % item)
    thefile = open(os.path.join(d, "catagory.txt")).read()

    #adds words to exclude list
    STOPWORDS.add("chronic")
    STOPWORDS.add("disease")
    STOPWORDS.add("obstructive")
    STOPWORDS.add("status")

    # generate word cloud
    wordcloud = WordCloud(stopwords=STOPWORDS,
        background_color="white",
        width = 650,
        height = 250).generate_from_text(thefile)

    #re-colers and saves wordcloud as png
    wordcloud.recolor(color_func=grey_color_func, random_state=3)
    wordcloud.to_file("wordcloud.png")


#converts numbers to range of 0-255 for rgb
def convert(oldMin, oldMax, oldValue):
    oldRange = (oldMax - oldMin)
    newValue = (((oldValue - oldMin) * 255) / oldRange) + 0
    return newValue


#uses values from convert() to generate the hue of a specified colorize
#saves to image "colorplot.png"
def colorize(catagories, states2):
    #create two new lists
    local = {}
    newCats = []
    with open('U.S._Chronic_Disease_Indicators__CDI_.csv', newline='') as f:
        #takes user input abbrevieation of state and checks to see if usable
        while(True):
            statestr = input("Enter state abbrevieation: ")
            #garauntees that input will be lower case
            statestr = statestr.lower()
            #checks to see if input is in states2
            if statestr not in states2:
                print("Not acceptable input")
            if statestr in states2:
                break
        #if input works, append all diseases of specified inputed state
        reader = csv.reader(f)
        for row in reader:
            if (row[1].lower() == statestr):
                newCats.append(row[3].lower())
    #sort and count it
    classify(newCats, local)
    count(newCats, local)

    #local is to contain the frequency of, and diseases that apply to a specific state

    #smiply checking
    #comment this out if you dont want anything
    #to print to terminal
    #for i in local:
    #    print (i + ": " + str(local[i]))

    #new list is to contain the key values of local
    newList = [0]
    for i in local:
        newList.append(local[i])
    #find min and max of data
    oldMin = newList[0]
    oldMax = newList[0]
    for i in newList:
        if (int(i) < oldMin):
            oldMin = int(i)
        if (int(i) > oldMax):
            oldMax = int(i)
    #do not want to use 0 in the data, as it effects the resulting colors
    if oldMin == 0:
        oldmin = 1

    #use min and max to convert local's key values to rgb range
    for i in local:
        #if using black background oldMin comes before oldMax in arguments
        local[i] = int(convert(oldMax, oldMin, local[i]))

    #new local dict adjusted for RGB value scale
    #print("Adjusted for RGB")
    #print (local)

    #dynamically generate height of image using amount of stat in the string
    resBase = len(local)
    length = 0
    #image is to contain 4 color square accross
    #if amount of data is not devisible by 4, add extra row so that all may fit
    if resBase % 4 == 0:
        length = resBase / 4
        length *= 200
    elif resBase % 4 != 0:
        length = int(resBase / 4)
        length += 1
        length *= 200
    #each section of image is to be 200x200 with the total width of the image being 1000px

    #create new image wtith previously detirmined dimensions
    height = int(length)
    rgb = (255,255,255)
    res = (1000,height)
    newimage = Image.new("RGB",res,rgb)
    newImageData = newimage.load()

    #fill background with desired color
    for x in range(0, 1000):
        for y in range(0, height):
            newImageData[x,y] = (255, 255, 255)

    #write color of image in 200x200px chunks
    piCount = 1
    buffery = 0
    textHeight = 0
    #piCount is for x direction, buffery is for y direction, textHeight is y direction of text
    for i in local:
        bufferx = piCount * 200
        for x in range(bufferx,bufferx + 200):
            for y in range(buffery, buffery + 200):
                #detirmine color of squares here, lolal[i] will be the varyant
                newImageData[x,y] = (int(local[i]), int(local[i]), 255)
        #draw color and text to image
        draw = ImageDraw.Draw(newimage)
        # font = ImageFont.truetype(<font-file>, <font-size>)
        # font = ImageFont.truetype("sans-serif.ttf", 16)
        # draw.text((x, y),"Sample Text",(r,g,b))
        font = ImageFont.truetype("HelvLight Regular.ttf", 18)
        draw.text((0, textHeight),i,(0,0,0), font)

        #iterate through piCount for x direction of each square
        #textHeight iterates by 30 to achieve even distance
        #if piCount reaches 4, it means that the end of the image is met
        #if so, add 200 to buffery, effectively changing the row
        #textHeight goes up by 110 to evenl fit in each quare throughout the image
        if piCount < 4:
            piCount += 1
            textHeight += 30
        elif piCount == 4:
            buffery += 200
            piCount = 1
            textHeight += 110
    #save image
    newimage.save("colorplot.png")
