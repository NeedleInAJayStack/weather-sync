import base64
import requests

baseUrl = 'https://data.herron.dev'

def login(username, password):
  url = f'{baseUrl}/api/auth/token'
  response = requests.get(url, auth=(username, password))
  response.raise_for_status()
  return response.json()['token']

def createHis(hisItem, token):
  url = f'{baseUrl}/api/recs/{hisItem.pointId}/history'
  headers = {'Authorization': f'Bearer {token}'}
  response = requests.post(url, headers=headers, json={"ts": hisItem.ts, "value": hisItem.value})
  response.raise_for_status()

class HisItem:
 def __init__(self, pointId, ts, value):
    self.pointId = pointId
    self.ts = ts
    self.value = value
