from datetime import datetime

class TemplateData():
  code = ''
  description = ''
  name = ''
  meta_data = ''
  price = 0.0
  status = ''
  lat = 0.0
  lng = 0.0
  created_at = datetime.now()
  updated_at = datetime.now()
  def __init__(self, code, description, name, meta_data, price, lat, lng, created_at, updated_at, status):
    self.code = code
    self.description = description
    self.name = name
    self.meta_data = meta_data
    self.price = price
    self.lat = lat
    self.lng = lng
    self.created_at = created_at
    self.updated_at = updated_at
    self.status = status

  def to_dict(self):
    return {
      'code': self.code,
      'description': self.description,
      'name': self.name,
      'meta_data': self.meta_data,
      'price': self.price,
      'lat': self.lat,
      'lng': self.lng,
      'created_at': self.created_at,
      'updated_at': self.updated_at,
      'status': self.status,
    }