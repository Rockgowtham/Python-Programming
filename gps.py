import csv
from gmplot import gmplot

gmap=gmplot.GoogleMapPlotter(11.6722,78.1460,10)
gmap.coloricon="http://www.googlemapsmarkers.com/v1/%s/"
with open("route3.csv","r") as f:
    read=csv.reader(f)
    k=0
    for row in read:
        lat=float(row[0])
        long=float(row[1])
        if(k==0):
            gmap.marker(lat,long,"yellow")
            k=1
        else:
            gmap.scatter(lat, long, color='#3B0B39')
            gmap.marker(lat,long,"blue")
gmap.marker(lat,long,"red")
gmap.draw("mymap.html")