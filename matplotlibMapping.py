"""
Author: Samuel Sanchez
GitHub: SamuelSanchezA
Created: 18 April 2016
"""
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.basemap import Basemap
import unicodedata
import numpy as np
import time

def createMap():

	newMap = Basemap(width=12000000,height=9000000,
            rsphere=(6378137.00,6356752.3142),\
        	area_thresh=1000.,projection='lcc',\
            lat_1=45.,lat_2=55,lat_0=50,lon_0=-107.)
	newMap.drawcoastlines()
	newMap.fillcontinents(color='coral',lake_color='aqua')
	# draw parallels and meridians.
	newMap.drawparallels(np.arange(-80.,81.,20.))
	newMap.drawmeridians(np.arange(-180.,181.,20.))
	newMap.drawmapboundary(fill_color='aqua')

	return newMap


def getLatLon():

	chronicUSDiseases = pd.read_csv("U.S._Chronic_Disease_Indicators__CDI_.csv", sep=',',encoding='utf8', low_memory=False, dtype='str')

	usMap = createMap()

	for row in chronicUSDiseases["GeoLocation"]:
	 	# commaLocation Used to seperate lat lon into two strings
		counter = 0
		modifiedLatLon = [] # used to store edited row
		if((not isinstance(row, float))):
			for val in row:
				if(val != '(' and val != ')' and val != ' '):
					if(val == ','):
						commaLocation = counter
					modifiedLatLon.append(unicodedata.normalize('NFKD', val).encode('ascii', 'ignore')) # Converts unicode to ascii
					counter += 1
		else:
			modifiedLatLon = ["0",",","0"]
			commaLocation = 1
		
		lat = float(''.join(modifiedLatLon[:commaLocation]))
		
		lon = float(''.join(modifiedLatLon[commaLocation + 1 : len(modifiedLatLon)]))

		if(lat != 0 and lon != 0):
			plotPoint(lon,lat,usMap)
			print time.clock()

	#plt.autoscale(enable=True, axis='both',tight=True)
	plt.title("U.S. Chronic Disease Locations (2008-2013)")
	plt.show()
	
def plotPoint(lon, lat, m):
	xpt,ypt = m(lon,lat)
	# convert back to lat/lon
	#lonpt, latpt = m(xpt,ypt,inverse=True)
	m.plot(xpt,ypt,'bo')  # plot a blue dot there

def main():
	#CSV is parsed and read into variable
	getLatLon()

if __name__ == "__main__":
    main()
