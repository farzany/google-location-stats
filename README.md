# Google Location History Stats
This repository is for a microproject of mine which allows the user to calculate their daily movement stats based on their Google Location History data. Given a Location History Zip file, this python program will calculate how far you have travelled by foot, in a vehicle, in the subway, by plane, etc. The results solely rely on the fact that you have had Google Location enabled on your portable device for the period of time that you wish to look into. Or simply select "All Time Stats" and see your total stats during every time period that Google Location was enabled.

## How can I get my Location History data?
Google allows you to very easily download any saved data that you have on your account. To get your location history data, go to your [Google Timeline](https://www.google.com/maps/timeline), click the gear icon on the bottom right, click "Download a copy of all your data", then **deselect all the categories except for Location History**. It is important to only have Location History within the Zip file.

## Usage
This python program uses Tkinter to open a simple file selection GUI. 
```
pip install tkinter
```
If you do not wish to use Tkinter, simply put the file location within the below parameter, and comment out the tkinter block of code.
```
with zipfile.ZipFile("FILE LOCATION HERE",'r') as z:
```
## How does it work?
For every trip, google stores how far you travelled, and estimates by what means (on foot, bike, vehicle, etc). These trips are stored as "activitySegments" within the location history data. This program simply looks through every nested dictionary, looking for these pieces of information, and adds them up.
