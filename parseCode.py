import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.basemap import Basemap
import unicodedata
from googlemaps import Client

def createMap():
	gmaps = Client(key="AIzaSyCRH0Z8gMlRa2XXPA_TXhoQws9BANn6jmU")

def storeLatLong()

def main():
	#CSV is parsed and read into variable
	chronicUSDiseases = pd.read_csv("U.S._Chronic_Disease_Indicators__CDI_.csv", sep=',',encoding='utf8', low_memory=False, dtype='str')
	blankMap = createMap()
	
	lon = []
	lat = []
	index = 0
	for row in chronicUSDiseases["GeoLocation"]:
		commaLocation = 0
		counter = 0
		modifiedLatLon = []
		if((not isinstance(row, float))):
			for val in row:
				if(val != '(' and val != ')' and val != ' '):
					if(val == ','):
						commaLocation = counter
					modifiedLatLon.append(unicodedata.normalize('NFKD', val).encode('ascii', 'ignore'))
					counter += 1
		else:
			modifiedLatLon = ["0",",","0"]
			commaLocation = 1
		
		lon.append(''.join(modifiedLatLon[:commaLocation]))
		#print ("Longitude %s" % lon[index])
		lat.append(''.join(modifiedLatLon[commaLocation + 1 : len(modifiedLatLon)]))
		#print ("Latitude %s" % lat[index])
		lon[index] = float(lon[index])
		lat[index] = float(lat[index])
		index += 1

	#x, y = blankMap(lat, lon)
	#blankMap.scatter(x,y,1,marker='o',color='red')
	#plt.show()

if __name__ == "__main__":
    main()
