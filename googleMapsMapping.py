"""
Author: Samuel Sanchez
GitHub: SamuelSanchezA
year: US chronic diseases reported by the CDC between 2007-2013 
			 are mapped onto a map of the United States (continental and offshore)
"""
from bokeh.io import output_file, show
from bokeh.models import GMapPlot, GMapOptions, ColumnDataSource, DataRange1d, PanTool, WheelZoomTool, BoxSelectTool, HoverTool, Diamond
import csv

def extractData(filePath, geoData, cat, year):

	with open(filePath, 'rb') as csvFile:
		parsedCSV = csv.reader(csvFile, delimiter=',')
		parsedCSV.next() # Skipping category headers
		for row in parsedCSV:
			modifiedRow = []
			for element in row[18]:
				if(element != '(' and element != ')' and element != ' '):
					modifiedRow.append(element)	
			modifiedRow = ''.join(modifiedRow)
			geoData.append(modifiedRow)
			cat.append(row[3])
			year.append(row[0])
			del modifiedRow

def plotPoints(latLonData, category, year):
	latitude = []
	longitude = []

	fillLatAndLon(latitude, longitude, latLonData)

	index = 0
	for value in longitude:
		if value == 0:
			category[index] = ''
			year[index] = ''
		index += 1

	latitude = [x for x in latitude if x != 0]
	longitude = [x for x in longitude if x != 0]
	category = [x for x in category if len(x) != 0]
	year = [x for x in year if len(x) != 0]

	dataSource = ColumnDataSource(
		data=dict(
			lat = latitude[:5000],
			lon = longitude[:5000],
			cat = category[:5000],
			year = year[:5000]
		)
	)

	hover = HoverTool(
        tooltips=[
        	("Case#", "$index"),
            ("Category", "@cat"),
            ("Year", "@year"),
        ]
    )
	
	map_options = GMapOptions(lat=47.60, lng=-122.33, map_type="hybrid", zoom=3)

	plot = GMapPlot(x_range=DataRange1d(), y_range=DataRange1d(), 
					map_options=map_options, title="U.S. Chronic Disease Locations (2008-2013)")

	diamond = Diamond(x="lon", y="lat", size=10, fill_color="red", fill_alpha=0.2, line_color='white')
	plot.add_glyph(dataSource, diamond)

	plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool(), hover)
	output_file("disease.html", title="Diseases")
	
	show(plot)
	
def fillLatAndLon(latitude, longitude, geoData):
	
	index = 0
	for row in geoData:
		if len(row) != 0:
			commaLocation = row.find(',')
			latitude.append(row[0:commaLocation])
			longitude.append(row[commaLocation + 1:len(row)])
			latitude[index] = float(latitude[index])
			longitude[index] = float(longitude[index])

		else:
			latitude.append(0)
			longitude.append(0)

		index += 1

	#print latitude
	#print longitude

def main():
	category = []
	year = []
	geoLocs = []
	extractData("U.S._Chronic_Disease_Indicators__CDI_.csv", geoLocs, category, year)
	plotPoints(geoLocs, category, year)

if __name__== "__main__":
	main()