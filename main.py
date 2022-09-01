import os
from dotenv import load_dotenv

from weatherApi import latestObservations
from jaysApi import login, createHis, HisItem

load_dotenv()

stationId = 'QHW'
observations = latestObservations(stationId)

properties = {
  'temperature': 'C5D85FAF-4C60-431C-AB8D-F7FD10B993C9',
  'dewpoint': 'D7EC0816-2CF8-4E9C-8F04-5B73A0D0128D',
  'windDirection': '3BD48B4B-2262-4FD0-83AA-AA7D47C98E7B',
  'windSpeed': '7654684B-2A42-4F1E-8D84-5D20398B3086',
  'barometricPressure': 'C017CBAF-0D9C-48A6-A2B0-34D36A669789',
  'relativeHumidity': '34A4A24E-A4F1-4464-86B2-4D0FC1900FEB'
}

hisItems = []
for observation in observations:
  if properties.get(observation.name) == None:
    continue
  pointId = properties[observation.name]
  hisItems.append(HisItem(pointId, observation.ts, observation.value))

jayApiUser = os.environ['JAY_API_USER']
jayApiPassword = os.environ['JAY_API_PASSWORD']
token = login(jayApiUser, jayApiPassword)
for hisItem in hisItems:
  success = createHis(hisItem, token)
  if success:
    print(f'Success: {hisItem.pointId} at {hisItem.ts}')
  else:
    print(f'Failed: {hisItem.pointId} at {hisItem.ts}')