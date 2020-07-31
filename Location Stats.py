# Necessary for the program
import json
import zipfile
import sys

# Just used for file selection gui
from tkinter.filedialog import askopenfilename
from tkinter import Tk
Tk().withdraw()
history = askopenfilename(title = "Select Zip file for analysis",filetypes = (("zip files","*.zip"),("all files","*.*")))

# All variables
distance_bicycle = 0
distance_vehicle = 0
distance_foot = 0
distance_bus = 0
distance_plane = 0
distance_subway = 0
failed = 0
success = 0

# Select the time period to look through
period = input("=============\n1. All-Time (all) \n2. Specific Year (####) [Example: 2020]\n3. Specific Year/Month (####_MONTH) [Example: 2020_JANUARY]\nChoose a time period (in specified format)\t")


# Given a json.load() dict, iterates through the dicts of the first key, 
# "timelineObjects". If the dict/key is an "activitySegment", 
# looks for "distance" and "activityType" keys and their values.
# Stores the distance within the corresponding activityType variable.

def GetDistance(data):
    for i in data['timelineObjects']:
        global success, failed, distance_bicycle, distance_bus, distance_foot, distance_plane, distance_subway, distance_vehicle
        try:
            if "activitySegment" in i:
                activityType = i["activitySegment"].get("activityType")
                if (activityType == "IN_PASSENGER_VEHICLE") or (activityType == "IN_VEHICLE"):
                    distance_vehicle += i["activitySegment"].get("distance")
                if activityType == "CYCLING":
                    distance_bicycle += i["activitySegment"].get("distance")
                if (activityType == "WALKING") or (activityType == "RUNNING"):
                    distance_foot += i["activitySegment"].get("distance")
                if (activityType == "IN_BUS"):
                    distance_bus += i["activitySegment"].get("distance")
                if (activityType == "FLYING"):
                    distance_plane += i["activitySegment"].get("distance")
                if (activityType == "IN_TRAIN") or (activityType == "IN_SUBWAY"):
                    distance_subway += i["activitySegment"].get("distance")
                success += 1
            else:
                pass
        except:
            failed += 1
            pass

# Reads through every file in the Zip file, except "Location History.json" and
# "archive_browser.html". Sends the files to GetDistance.

with zipfile.ZipFile(history,'r') as z:
    for filename in z.namelist():
        try:
            print(filename)
            with z.open(filename) as f:
                if (filename != "Takeout/Location History/Location History.json") and (filename != "Takeout/archive_browser.html"):
                    if period == "all":
                        data = json.load(f)
                        GetDistance(data)
                    elif period in filename:
                        data = json.load(f)
                        GetDistance(data)
                    else:
                        pass
                else:
                    pass
        except:
            pass

# Printing the recorded values
print("=============")
print("File:\t\t" + history)
print("Biked:\t\t" + str(distance_bicycle/1000) + " km")
print("Walked/Ran:\t" + str(distance_foot/1000) + " km")
print("Driven:\t\t" + str(distance_vehicle/1000) + " km")
print("Bussed:\t\t" + str(distance_bus/1000) + " km")
print("Flew:\t\t" + str(distance_plane/1000) + " km")
print("Subway:\t\t" + str(distance_subway/1000) + " km")
print("Success Rate:\t" + str(success/(failed+success)*100) + " %")


