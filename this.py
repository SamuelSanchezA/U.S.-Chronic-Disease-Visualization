import csv
import os
from scipy.misc import imread
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


dates=[]
datesDict={}
states=[]
statesDict={}
catagory=[]
catagoryDict={}


STOPWORDS.add("chronic")
STOPWORDS.add("disease")
cloud1_coloring = imread(os.path.join(d, "CloudColor.png")).read()
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




with open('U.S._Chronic_Disease_Indicators__CDI_.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        dates.append(row[0])
        states.append(row[1])
        catagory.append(row[3])


classify(catagory, catagoryDict)
classify(dates, datesDict)
classify(states, statesDict)
count(catagory, catagoryDict)
count(dates, datesDict)
count(states, statesDict)

d = os.path.dirname(__file__)
file = open("catagory.txt", 'w')
for item in catagory:
    file.write("%s\n" % item)
thefile = open(os.path.join(d, "catagory.txt")).read()

# generate word cloud
wordcloud = WordCloud(stopwords=STOPWORDS, background_color="#FFFFF5").generate_from_text(thefile)
"""
look into how tuples work and shit.
"""


wordcloud.to_file("wordlcoud.png")
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

for i in catagoryDict:
    print (i + ": " + str(catagoryDict[i]))
print("")
for i in statesDict:
    print (i + ": " + str(statesDict[i]))
print("")
for i in datesDict:
    print (i + ": " + str(datesDict[i]))
