class DataService:
  def __init__(self):
    self.data = []

  def get_data(self):
    return self.data

  def save_data(self, data):
    self.data.append(data)
    return self.data