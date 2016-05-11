"""
  Name: Samuel Sanchez
  Date: 
"""
from bokeh.plotting import figure, show, output_file
from bokeh.sampledata.us_states import data as states
import pandas as pd
import unicodedata

def categorize(parsedObject):
  categories = sorted(set(parsedObject['Category'])) # Placing states and disease categories into sorted sets
  states = sorted(set(parsedObject['LocationAbbr']))
  states.remove('US') # US = Unites States. Only looking for state abbreviations

  #print states
  fillMap(categories, states, parsedObject)

def fillMap(category, state, csvFile):

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
  
  # Assings number of states with reported category diseases
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
  

  
  state_xs = [states[code]["lons"] for code in states]
  state_ys = [states[code]["lats"] for code in states]

  colors = ["#FFFFFF", "#DD6666", "#BB5555", "#994444", "#770000", "#550000"]

  maxVal = alcohol[max(alcohol.iterkeys(), key=lambda k: alcohol[k])]

  print maxVal / 6

  state_colors = []
  for state_id in states:
      try:
          cases = alcohol[state_id]
          print ("Cases in %s" %state_id), ": " , cases
          idx = cases / (maxVal / 6) - 1
          print "idx ", idx
          state_colors.append(colors[idx])
      except KeyError:
          state_colors.append("black")


  p = figure(title="US Chronic Diseases (Alcohol) 2007-2013", toolbar_location="left",
             plot_width=2800, plot_height=800)

  p.patches(state_xs, state_ys, fill_color=state_colors, fill_alpha=100.0,
            line_color="#884444", line_width=2, line_alpha=5.0)

  output_file("density.html", title="density.py example")

  show(p)
  
def main():
  chronicUSDiseases = pd.read_csv("U.S._Chronic_Disease_Indicators__CDI_.csv", sep=',',encoding='utf8', low_memory=False, dtype='str')
  #plotData = zip(chronicUSDiseases[:5000]['Year'], chronicUSDiseases[:5000]['LocationAbbr'], chronicUSDiseases[:5000]['Category'])
  categorize(chronicUSDiseases)

if __name__ == '__main__':
  main()