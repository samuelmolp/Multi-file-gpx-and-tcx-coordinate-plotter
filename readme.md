# Plotter for multiple gpx and tcx files

#### Description:

This is a gpx and tcx plotter. It will get the coordinates from one or multiple files (the files from a specific folder) and display them in a map.

1. In get_tracks.py it will convert the tcx into gpx and then it will divide the gpx into different folders depending on the sport.

2. In get_data.py it will get the coordinates of all gpx files from a concrete folder.

3. Finally, in plot.py it will display the coordinates into a map


#### Usage idea:

Displaying the coordinates from more than one file can seem stupid but it will actually be very useful in a couple of situations. Imagine for example that you download all your tracks from strava, endomondo or another platform. With this **you could plot all of those files into a single map and see the places where you still haven't runned or walked or the places where you've walked the most**. 
