import base64
import requests

baseUrl = 'https://utility-api.jayherron.org'

def login(username, password):
  url = f'{baseUrl}/auth/token'
  response = requests.get(url, auth=(username, password))
  response.raise_for_status()
  return response.json()['token']

def createHis(hisItem, token):
  url = f'{baseUrl}/his/{hisItem.pointId}'
  headers = {'Authorization': f'Bearer {token}'}
  response = requests.post(url, headers=headers, json={"ts": hisItem.ts, "value": hisItem.value})
  response.raise_for_status()
  return response.json()['success']

class HisItem:
 def __init__(self, pointId, ts, value):
    self.pointId = pointId
    self.ts = ts
    self.value = value
