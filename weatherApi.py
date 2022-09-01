import requests

headers = {
  'accept': 'application/ld+json',
  'user-agent': '(jayherron.org, NeedleInAJayStack@protonmail.com)' 
}

def latestObservations(stationId):
  url = f'https://api.weather.gov/stations/{stationId}/observations/latest'
  latestObservation = requests.get(url, headers=headers).json()

  timestamp = latestObservation['timestamp']

  observations = []
  for propertyName, object in latestObservation.items():
    if (not propertyName.startswith('@')) and isinstance(object, dict) and object.get('value') != None:
      value = object['value']
      observations.append(Observation(propertyName, timestamp, value))

  return observations

class Observation:
 def __init__(self, name, ts, value):
    self.name = name
    self.ts = ts
    self.value = value
