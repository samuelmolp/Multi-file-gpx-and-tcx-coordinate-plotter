import os
from xml.dom import minidom
import get_tracks


"""It will read and store the coordinates from each gpx file"""

def main():
    #We call the get_tracks main function
    get_tracks.main()

    #We get the list of the gpx files from a concrete folder
    all=list(os.listdir('C:\\Users\lmoli\Desktop\SAMUEL\TERCERO\PROGRAMACIÓN\strava\\andar'))
    all_p=["C:\\Users\lmoli\Desktop\SAMUEL\TERCERO\PROGRAMACIÓN\strava\\andar\\{}".format(e) for e in all]

    lat=[]
    lon=[]

    #And we get the coordinates from each of the files and store them in two lists
    for x in range(len(all_p)):
        xml=minidom.parse(all_p[x])
        collection=xml.documentElement
        coor = collection.getElementsByTagName("trkpt")

        for i in range(len(coor)):
            at=coor[i].attributes
            la=at.getNamedItem("lat")
            lo=at.getNamedItem("lon")
            lat.append(float(la.value))
            lon.append(float(lo.value))


    return lat, lon
            
