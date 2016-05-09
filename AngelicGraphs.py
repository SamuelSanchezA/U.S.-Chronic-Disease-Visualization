from bokeh.charts import Bar, output_file, show
from bokeh.sampledata.autompg import autompg as df
import csv
from bokeh.charts.attributes import ColorAttr, CatAttr
from bokeh.charts.builders.bar_builder import BarBuilder
filename = "U.S._Chronic_Disease_Indicators__CDI_.csv"

def bubbleSort(alist, blist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
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
    
bubbleSort(diseaseCounter, singleDiseaseList)    

#resetting count for the next for loop
count = 0

data = {
    'Disease Name' : singleDiseaseList,
    '# of Occurances' : diseaseCounter
}

for index in singleDiseaseList:
    print "Disease : " + singleDiseaseList[count] + ". Counter : " + str(diseaseCounter[count])
    count+=1
    
p = Bar(data, values= '# of Occurances',label=CatAttr(columns=['Disease Name'], sort=False), title='U.S. Chronic Diseases (2007-2013)', color = 'blue')
#make a list for 5 top diseases and 5 least likely diseases

output_file("bar.html")

show(p)

