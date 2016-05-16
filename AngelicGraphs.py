from bokeh.charts import Bar, output_file, show
from bokeh.sampledata.autompg import autompg as df
import csv
from bokeh.charts.attributes import ColorAttr, CatAttr
from bokeh.charts.builders.bar_builder import BarBuilder
filename = "U.S._Chronic_Disease_Indicators__CDI_.csv"
#Ascending bubbleSort
def bubbleSortA(alist, blist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp1 = alist[i]
                temp2 = blist[i]
                alist[i] = alist[i+1]
                blist[i] = blist[i+1]
                alist[i+1] = temp1
                blist[i+1] = temp2
def bubbleSortD(alist, blist):
    for passnum in range(len(alist)-1,0,-1):
            for i in range(passnum):
                if alist[i]<alist[i+1]:
                    temp1 = alist[i]
                    temp2 = blist[i]
                    alist[i] = alist[i+1]
                    blist[i] = blist[i+1]
                    alist[i+1] = temp1
                    blist[i+1] = temp2

def getCategory(chronicUSDiseases):
    categoryList = []
    
    count = 0;
    #disease = "alcohol"
    
    with open(chronicUSDiseases, 'rb') as csvFile:
        parsedCSV = csv.reader(csvFile, delimiter = ',')
        parsedCSV.next()
        for index in parsedCSV:
                categoryList.append(index[3])
      
    return categoryList
    
#get the list
#get a counter for each disease
#count how many items are in the list specifically
#list them somehow?

uneditedList = getCategory(filename)
singleDiseaseList = []
diseaseCounter = []
listIndex = 0
count = 0
#this is to seperate out the long list into single "disease" categories
#also gets the count whenever it already has one in it's list (stored in diseaseCounter)
singleDiseaseList.append(uneditedList[count]) #always need the first one because it'll be empty otherwise
diseaseCounter.append(1) #since the first one is taken in outside of the for loop, need to manually add one to the first element

for index in uneditedList:
    #this will be used later
    isAdding = True
    #if it finds the same name, adds one to it's counter in diseaseCounter
    if(singleDiseaseList[listIndex] == uneditedList[count]):
        diseaseCounter[listIndex]+=1  
    #we found a new one, so we automatically go to the next index
    else:
        #making sure we don't already a specified disease in the list
        for index in singleDiseaseList:
            if (uneditedList[count] == "Nutrition, Physical Activity, and Weight Status"): #Weight and Physical is captial sometimes
                isAdding = False
                diseaseCounter[13]+=1 #this is  Nutrition, physical activity, and weight status
            checkList = 0
            while (isAdding == True and checkList <= listIndex):
                if (singleDiseaseList[checkList] == uneditedList[count]):
                    isAdding = False
                    diseaseCounter[listIndex]+=1 #this was skipped earlier because it skipped the if statement
                checkList +=1
        if (isAdding == True):
            listIndex+=1
            singleDiseaseList.append(uneditedList[count])
            diseaseCounter.append(1)
        
    #basically same as index, but index is a list and not an int
    count+=1
singleDiseaseList[13] = "Nutrition, Physical Activity, and Weight Status"
userFlag = 't'
userColor = "blue"


dataOptions = 2# 1 alphabetical list, 2 ascending list, 3 descending list


while (userFlag != 'q' and userFlag != 'Q'):
    print "What would you like to do:"
    print "1. Change the color of the graph"
    print "2. Make the graph ascending order"
    print "3. Make the graph descending order"
    print "4. See the list of chronic diseases"
    print "5. Show the graph"
    print "Q. quit"
    userFlag = raw_input('Choice : ')
    print userFlag
    if (userFlag == '1'):
        userColor = raw_input("Write a color name ")
        if (userColor == 'white' or userColor == 'White'):
            print ""
            print "nice meme."
            print "It's like you already know the background is white and you just want to mess with the graph."
            print "... this is why we can't have nice things."
            print ""
    elif (userFlag == '2'):
        dataOptions = 2
    elif (userFlag == '3'):
        dataOptions = 3
    elif (userFlag == '4'):
        count = 0 # don't want to go outside of the list
        alphabeticalData = {
            'Disease Name' : singleDiseaseList,
            '# of Occurances' : diseaseCounter
            }
        sorted(alphabeticalData)
        print "*******************************"
        print "**Disease Names and Occurance**" 
        print "*******************************"
        for index in singleDiseaseList:
            print singleDiseaseList[count] + " : " + str(diseaseCounter[count])
            count+=1
    elif (userFlag == '5'):
            
        if (dataOptions == 2):
            bubbleSortA(diseaseCounter, singleDiseaseList) 

            ascendingData = {
                'Disease Name' : singleDiseaseList,
                '# of Occurances' : diseaseCounter
            }

            asc = Bar(ascendingData, values= '# of Occurances',label=CatAttr(columns=['Disease Name'], sort=False), title='U.S. Chronic Diseases(2007-2013)', color = userColor)
            output_file("bar2.html")
            show(asc)
        elif (dataOptions == 3):
            bubbleSortD(diseaseCounter, singleDiseaseList) 
            descendingData = {
                'Disease Name' : singleDiseaseList,
                '# of Occurances' : diseaseCounter
            }
            des = Bar(descendingData, values= '# of Occurances',label=CatAttr(columns=['Disease Name'], sort=False), title='U.S. Chronic Diseases(2007-2013)', color = userColor)
            output_file("bar3.html")
            show(des)
            
