"""
  Name: Samuel Sanchez
  Date: 13 May 2016
"""
from bokeh.plotting import figure, show, output_file, hplot
from bokeh.sampledata.us_states import data as states
import pandas as pd
import unicodedata
import Tkinter as tk

def categorize(parsedObject):
  categories = sorted(set(parsedObject['Category'])) # Placing states and disease categories into sorted sets
  states = sorted(set(parsedObject['LocationAbbr']))
  states.remove('US') # US = Unites States. Only looking for state abbreviations

  #print states
  fillCategories(categories, states, parsedObject)

def fillCategories(category, state, csvFile):

  for x in range(len(state)):
    state[x] = unicodedata.normalize('NFKD', state[x]).encode('ascii', 'ignore')

  for x in range(len(category)):
    category[x] = unicodedata.normalize('NFKD', category[x]).encode('ascii', 'ignore')

  #Dictionaries that will have state abbreviations as keys
  alcohol = {}
  arthritis = {}
  asthma = {}
  cancer = {}
  cardioVasc = {}
  chronicKidDis = {}
  chronObstPulDis = {}
  diabetes = {}
  disablitly = {}
  immunization = {}
  mentalHealth = {}
  fitnessAndHealth = {}
  olderAdults = {}
  oralHealth = {}
  overArchCon = {}
  reproductiveHealth = {}
  tobacco = {}

  # Initialize all state keys to 0
  for x in range(len(state)):
    alcohol[state[x]] = 0
    arthritis[state[x]] = 0
    asthma[state[x]] = 0
    cancer[state[x]] = 0
    cardioVasc[state[x]] = 0
    chronicKidDis[state[x]] = 0
    chronObstPulDis[state[x]] = 0
    diabetes[state[x]] = 0
    disablitly[state[x]] = 0
    immunization[state[x]] = 0
    mentalHealth[state[x]] = 0
    fitnessAndHealth[state[x]] = 0
    olderAdults[state[x]] = 0
    oralHealth[state[x]] = 0
    overArchCon[state[x]] = 0
    reproductiveHealth[state[x]] = 0
    tobacco[state[x]] = 0
  
  # Assings number of states with reported category diseases by iterating through CSV file
  # 17 in Total
  for row in range(len(csvFile)):
    
    if(csvFile['Category'][row] == category[0] and csvFile['LocationAbbr'][row] in state):
       alcohol[csvFile['LocationAbbr'][row]] += 1

    elif(csvFile['Category'][row] == category[1] and csvFile['LocationAbbr'][row] in state):
       arthritis[csvFile['LocationAbbr'][row]] += 1

    elif(csvFile['Category'][row] == category[2] and csvFile['LocationAbbr'][row] in state):
       asthma[csvFile['LocationAbbr'][row]] += 1

    elif(csvFile['Category'][row] == category[3] and csvFile['LocationAbbr'][row] in state):
       cancer[csvFile['LocationAbbr'][row]] += 1

    elif(csvFile['Category'][row] == category[4] and csvFile['LocationAbbr'][row] in state):
       cardioVasc[csvFile['LocationAbbr'][row]] += 1

    elif(csvFile['Category'][row] == category[5] and csvFile['LocationAbbr'][row] in state):
       chronicKidDis[csvFile['LocationAbbr'][row]] += 1

    elif(csvFile['Category'][row] == category[6] and csvFile['LocationAbbr'][row] in state):
       chronObstPulDis[csvFile['LocationAbbr'][row]] += 1

    elif(csvFile['Category'][row] == category[7] and csvFile['LocationAbbr'][row] in state):
       diabetes[csvFile['LocationAbbr'][row]] += 1

    elif(csvFile['Category'][row] == category[8] and csvFile['LocationAbbr'][row] in state):
       diabetes[csvFile['LocationAbbr'][row]] += 1

    elif(csvFile['Category'][row] == category[9] and csvFile['LocationAbbr'][row] in state):
       immunization[csvFile['LocationAbbr'][row]] += 1

    elif(csvFile['Category'][row] == category[10] and csvFile['LocationAbbr'][row] in state):
       mentalHealth[csvFile['LocationAbbr'][row]] += 1

    elif(csvFile['Category'][row] == category[11] and csvFile['LocationAbbr'][row] in state):
       fitnessAndHealth[csvFile['LocationAbbr'][row]] += 1

    elif(csvFile['Category'][row] == category[12] and csvFile['LocationAbbr'][row] in state):
       olderAdults[csvFile['LocationAbbr'][row]] += 1

    elif(csvFile['Category'][row] == category[13] and csvFile['LocationAbbr'][row] in state):
       oralHealth[csvFile['LocationAbbr'][row]] += 1

    elif(csvFile['Category'][row] == category[14] and csvFile['LocationAbbr'][row] in state):
       overArchCon[csvFile['LocationAbbr'][row]] += 1

    elif(csvFile['Category'][row] == category[15] and csvFile['LocationAbbr'][row] in state):
       reproductiveHealth[csvFile['LocationAbbr'][row]] += 1

    elif(csvFile['Category'][row] == category[16] and csvFile['LocationAbbr'][row] in state):
       tobacco[csvFile['LocationAbbr'][row]] += 1
  
  choice = chooseCategory(category)
  customTitle = ""

  if(choice == 1):
    chosenCategory = alcohol
    customTitle = "Alchol"
  elif(choice == 2):
    chosenCategory = arthritis
    customTitle = "Arthritis"
  elif(choice == 3):
    chosenCategory = asthma
    customTitle = "Asthma"
  elif(choice == 4):
    chosenCategory = cancer
    customTitle = "Cancer"
  elif(choice == 5):
    chosenCategory = cardioVasc
    customTitle = "Cardio Vascular Disease"
  elif(choice == 6):
    chosenCategory = chronicKidDis
    customTitle = "Chronic Kidney Disease"
  elif(choice == 7):
    chosenCategory = chronObstPulDis
    customTitle = "Chronic Obstructive Pulmonary Disease"
  elif(choice == 8):
    chosenCategory = diabetes
    customTitle = "Diabetes"
  elif(choice == 9):
    chosenCategory = disablitly
    customTitle = "Disablilty"
  elif(choice == 10):
    chosenCategory = immunization
    customTitle = "Immunization"
  elif(choice == 11):
    chosenCategory = mentalHealth
    customTitle = "Mental Health"
  elif(choice == 12):
    chosenCategory = fitnessAndHealth
    customTitle = "Nutrition, Physical Activity, and Weight Status"
  elif(choice == 13):
    chosenCategory = olderAdults
    customTitle = "Older Adults"
  elif(choice == 14):
    chosenCategory = oralHealth
    customTitle = "Oral Health"
  elif(choice == 15):
    chosenCategory = overArchCon
    customTitle = "Overarching Conditions"
  elif(choice == 16):
    chosenCategory = reproductiveHealth
    customTitle = "Reproductive Health"
  elif(choice == 17):
    chosenCategory = tobacco
    customTitle = "Tobacco"
  else:
    chosenCategory = alcohol # DEFAULT

  excluded = ('GU', 'PR', 'VI', 'US') # Excluding data with locations as United States or territories

  #Colors used to fill states
  colors = ["#DFAAAA", "#DD6666", "#B84544", "#944444", "#870000", "#490000"]
  #****************************************************************************
  # Will plot Alaska and Hawaii seperately for formatting purposes
  alaska = states['AK']
  alaska_state_x = [states['AK']["lons"]]
  alaska_state_y = [states['AK']["lats"]]
  hawaii = states['HI']
  hawaii_state_x = [states['HI']["lons"]]
  hawaii_state_y = [states['HI']["lats"]]

  alaska_color = ""
  hawaii_color = ""

  alaska_cases = chosenCategory['AK']
  hawaii_cases = chosenCategory['HI']

  if(alaska_cases < 20):
    alaska_color = colors[0]
  elif(alaska_cases < 40):
    alaska_color = colors[1]
  elif(alaska_cases < 60):
    alaska_color = colors[2]
  elif(alaska_cases < 80):
    alaska_color = colors[3]
  elif(alaska_cases < 100):
    alaska_color = colors[4]
  elif(cases >= 100):
    alaska_color = colors[5]
  else:
    alaska_color = "black"

  if(hawaii_cases < 20):
    hawaii_color = colors[0]
  elif(hawaii_cases < 40):
    hawaii_color = colors[1]
  elif(hawaii_cases < 60):
    hawaii_color = colors[2]
  elif(hawaii_cases < 80):
    hawaii_color = colors[3]
  elif(hawaii_cases < 100):
    hawaii_color = colors[4]
  elif(hawaii_cases >= 100):
    hawaii_color = colors[5]
  else:
    hawaii_color = "black"  
  #****************************************************************************

  del states['AK'] # Will only show the continental U.S.
  del states['HI']

  # Obtains the longitude and latitude for states in order to create map
  continental_state_xs = [states[code]["lons"] for code in states]
  continental_state_ys = [states[code]["lats"] for code in states]

  state_colors = []

  # Following for loop will assign a color to a state depending on number of cases 
  for state_id in states:
      if state_id in excluded:
        continue
      try:
          cases = chosenCategory[state_id]
          #print ("Cases in %s" %state_id), ": " , cases
          if(cases >= 0 and cases < 20):
            state_colors.append(colors[0])
          elif(cases >= 21 and cases < 40):
            state_colors.append(colors[1])
          elif(cases >= 41 and cases < 60):
            state_colors.append(colors[2])
          elif(cases >= 61 and cases < 80):
            state_colors.append(colors[3])
          elif(cases >= 81 and cases < 100):
            state_colors.append(colors[4])
          elif(cases >= 100):
            state_colors.append(colors[5])
      except KeyError:
          state_colors.append("white")



  #***********************************************************************************************
  #Continental US glyphs and map
  continental_US = figure(title="US Chronic Diseases 2007-2013", toolbar_location="left",
             plot_width=1200, plot_height=700)

  continental_US.circle(legend="0-20 Cases", color=colors[0])
  continental_US.circle(legend="21-40 Cases", color=colors[1])
  continental_US.circle(legend="41-60 Cases", color=colors[2])
  continental_US.circle(legend="61-80 Cases", color=colors[3])
  continental_US.circle(legend="81-100 Cases", color=colors[4])
  continental_US.circle(legend="100 or Greater Cases", color=colors[5])
  continental_US.circle(legend="No data recorded", color="white")

  continental_US.patches(continental_state_xs, continental_state_ys , fill_color=state_colors, fill_alpha=100.0,
            line_color="#884444", line_width=2.5, line_alpha=5.0)
  #***********************************************************************************************
  # Alaska Plot
  alaska_figure = figure(title="Alaska", toolbar_location="left",
              plot_width=5000, plot_height=800)

  alaska_figure.circle(legend="0-20 Cases", color=colors[0])
  alaska_figure.circle(legend="21-40 Cases", color=colors[1])
  alaska_figure.circle(legend="41-60 Cases", color=colors[2])
  alaska_figure.circle(legend="61-80 Cases", color=colors[3])
  alaska_figure.circle(legend="81-100 Cases", color=colors[4])
  alaska_figure.circle(legend="100 or Greater Cases", color=colors[5])
  alaska_figure.circle(legend="No data recorded", color="white")

  alaska_figure.patches(alaska_state_x, alaska_state_y, fill_color=alaska_color, fill_alpha=100.0,
              line_color="#884444", line_width=2.5, line_alpha=5.0)
  #***********************************************************************************************
  # Hawaii Plot
  hawaii_figure = figure(title="Hawaii", toolbar_location="left",
              plot_width=900, plot_height=1000)

  hawaii_figure.circle(legend="0-20 Cases", color=colors[0])
  hawaii_figure.circle(legend="21-40 Cases", color=colors[1])
  hawaii_figure.circle(legend="41-60 Cases", color=colors[2])
  hawaii_figure.circle(legend="61-80 Cases", color=colors[3])
  hawaii_figure.circle(legend="81-100 Cases", color=colors[4])
  hawaii_figure.circle(legend="100 or Greater Cases", color=colors[5])
  hawaii_figure.circle(legend="No data recorded", color="white")

  hawaii_figure.patches(hawaii_state_x, hawaii_state_y, fill_color=hawaii_color, fill_alpha=100.0,
              line_color="#884444", line_width=2.5, line_alpha=5.0)

  output_file("density.html", title=customTitle + " Cases")

  allFigures = hplot(continental_US, hawaii_figure, alaska_figure)

  show(allFigures)
  
def chooseCategory(category):
  index = 1
  print "Choose a category to visualize by entering its value"
  for i in range(len(category)):
    print index, " ", category[i]
    index += 1 

  choice = int(raw_input("Enter Here: "))

  while(choice not in range(1,18)):
    print "Invalid Choice. Chose again"
    for i in range(len(category)):
      print index, " ", category[i]
      index += 1 

    choice = int(raw_input("Enter Here: "))

  return choice

def main():
  chronicUSDiseases = pd.read_csv("U.S._Chronic_Disease_Indicators__CDI_.csv", sep=',',encoding='utf8', low_memory=False, dtype='str')
  #plotData = zip(chronicUSDiseases[:5000]['Year'], chronicUSDiseases[:5000]['LocationAbbr'], chronicUSDiseases[:5000]['Category'])
  categorize(chronicUSDiseases)

if __name__ == '__main__':
  main()