import requests

class Connection:
  def __init__(self, base_url):
    self.base_url = base_url

  def get(self, endpoint, params=None):
    response = requests.get(f"{self.base_url}/{endpoint}", params=params)
    response.raise_for_status()
    return response.json()

  def post(self, endpoint, data=None, json=None):
    response = requests.post(f"{self.base_url}/{endpoint}", data=data, json=json)
    response.raise_for_status()
    return response.json()

  def put(self, endpoint, data=None):
    response = requests.put(f"{self.base_url}/{endpoint}", data=data)
    response.raise_for_status()
    return response.json()

  def delete(self, endpoint):
    response = requests.delete(f"{self.base_url}/{endpoint}")
    response.raise_for_status()
    return response.json()