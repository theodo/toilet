from threading import Timer

class Toilet:
  FREE = 'free'
  USED = 'used'

  def __init__(self, name, status):
    self.name   = name
    self.status = self.FREE if status > 80 else self.USED
    self.timer = Timer(4.0, self.change_value())
    self.timer.start()

  def to_string(self):
    return '%s is %s' % (self.name, self.status)

  def change_value(self):
    self.status = self.FREE if self.status is self.USED else self.USED
    print self.status

  def is_free(self):
    return true if self.status is self.FREE else self.USED
