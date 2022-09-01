import re
import requests

from weatherApi import headers

myLng = -111.85604
myLat = 40.74177
state = 'UT'

url = f'https://api.weather.gov/stations?state={state}'
stationsRes = requests.get(url, headers=headers).json()
stations = stationsRes['@graph']

closestStation = None
smallestDistance = 100000000000.0

def distance(station):
  point = station['geometry']
  regex = re.search('POINT\(([\d|\.|-]*) ([\d|\.|-]*)\)', point)
  lng = float(regex.group(1))
  lat = float(regex.group(2))
  # I know this is a euclidian distance, but I don't care because it's good enough.
  return pow(pow(lng - myLng, 2) + pow(lat - myLat, 2), 0.5)

sortedStations = sorted(stations, key = lambda station: distance(station))
stationIDs = []
for station in sortedStations:
  stationIDs.append(station['stationIdentifier'])
print(stationIDs[:20])

# Closest stationID with actual observations: QHW
