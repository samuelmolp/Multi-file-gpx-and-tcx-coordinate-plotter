import get_data as g

#pip install gmplot
import gmplot


"""It will plot the points into a map with the help of gmplot"""

#we get the coordinates calling the main function in get_data
data=g.main()
latitude= data[0]
longitude = data[1]

l=int(len(latitude))

#in this case we are taking off one out of two points because there are too many and so 
#the map couldn't load with all of them.
latitude_list1 = latitude[::2]
longitude_list1 = longitude[::2]


#we set the basemao
gmap1 = gmplot.GoogleMapPlotter(37.186528, -3.618589, 9 )

#To get a better quality map, we add the google maps api key. To get it follow the steps in: https://developers.google.com/maps?hl=es
gmap1.apikey = "AIzaSyCG7HyvcAhlSWR-CrYyO3zCAl_Usoz3o3w"

  
# scatter points on the google map
gmap1.scatter( latitude_list1, longitude_list1, '# 0000FF',
                              size = 40, marker = False )


#And we create the map
gmap1.draw( "C:\\Users\\lmoli\\Desktop\\samuel\\tercero\\programación\\strava\\map1.html" )
