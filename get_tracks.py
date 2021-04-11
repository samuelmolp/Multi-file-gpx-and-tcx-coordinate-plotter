import os
import json

#pip install tcx2gpx
from tcx2gpx import tcx2gpx


"""It will take tcx files (from a folder) and convert them to gpx. 
Then it will divide the gpx files into different categories"""

def main():

    #We create the folders for the different categories. Note that they can be others. 
    os.mkdir("running")
    os.mkdir("andar")
    os.mkdir("other")
    os.mkdir("andar_short")


    #We create a list with the path of each tcx file in a conrete folder
    all=list(os.listdir('C:\\Users\lmoli\Desktop\SAMUEL\TERCERO\PROGRAMACIÓN\strava\endomondo-2021-03-19\Workouts'))
    tcx=list(filter(lambda a: a.endswith(".tcx"), all))
    path=["C:\\Users\lmoli\Desktop\SAMUEL\TERCERO\PROGRAMACIÓN\strava\endomondo-2021-03-19\Workouts\\{}".format(e) for e in tcx]


    #We convert the tcx files into gpx files with the tcx2gpx module
    for e in path:
        gps_object = tcx2gpx.TCX2GPX(tcx_path=e)
        gps_object.convert()


    #We create a list with the path of each gpx file in the folder
    all=list(os.listdir('C:\\Users\lmoli\Desktop\SAMUEL\TERCERO\PROGRAMACIÓN\strava\endomondo-2021-03-19\Workouts'))
    gpx=list(filter(lambda a: a.endswith(".gpx"), all))
    path=["C:\\Users\lmoli\Desktop\SAMUEL\TERCERO\PROGRAMACIÓN\strava\endomondo-2021-03-19\Workouts\\{}".format(e) for e in gpx]


    """In the next lines we divide all the gpx files in the different categories and move them to the neccesary folders. 
    In this case we have json files for each gpx so we'll read the sport from those files.
    Note that if we don't have jsons it could be easily modified to read the information from the gpx files. 
    (the problem is that when converting a tcx to a gpx, in the gpx may always show "other" in the sport part"""
    for x in range(len(gpx)):
            current=gpx[x][:-4]
            p="C:/Users/lmoli/Desktop/SAMUEL/TERCERO/PROGRAMACIÓN/strava/endomondo-2021-03-19/Workouts/{}.json".format(current)
            
            with open(p,"r") as file:
                data = json.load(file)
                index=0
                while index<5:
                    try:

                        if data[index]["sport"]=="AEROBICS" or data[index]["sport"]=="STEP_COUNTER" or data[index]["sport"]=="OTHER" or data[index]["sport"]=="CYCLING_TRANSPORTATION":
                            os.replace(path[x], "C:\\Users\lmoli\Desktop\SAMUEL\TERCERO\PROGRAMACIÓN\strava\\other\\{}.gpx".format(x+1))
                            break
                            

                        elif data[index]["sport"]=="RUNNING":
                            os.replace(path[x], "C:\\Users\lmoli\Desktop\SAMUEL\TERCERO\PROGRAMACIÓN\strava\\running\\{}.gpx".format(x+1))
                            break
                        

                        else:
                            try:
                                if data[index+6]["distance_km"]<10:
                                    os.replace(path[x], "C:\\Users\lmoli\Desktop\SAMUEL\TERCERO\PROGRAMACIÓN\strava\\andar_short\\{}.gpx".format(x+1))
                                    break

                                os.replace(path[x], "C:\\Users\lmoli\Desktop\SAMUEL\TERCERO\PROGRAMACIÓN\strava\\andar\\{}.gpx".format(x+1))
                                break
                            
                            except KeyError as e:
                                print("ERROR")
                                break
                        
                    except KeyError as e:
                        index+=1
