class Toilet:
  def __init__(self, name, status):
    self.name   = name
    self.status = 'free' if status > 80 else 'used'

  def to_string(self):
    return '%s is %s' % (self.name, self.status)
