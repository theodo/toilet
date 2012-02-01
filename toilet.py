import urllib2
import json

def print_toilet_status():
    datas = urllib2.urlopen('http://lights.theodo.fr')
    toilets = {} 
    for name, status in json.load(datas).iteritems():
        toilet = Toilet(name, status)
        toilet.to_string()

class Toilet:
    def __init__(self, name, status):
        self.name   = name
        self.status = 'free' if status > 80 else 'used'

    def to_string(self):
        print '%s is %s' % (self.name, self.status)

if __name__ == '__main__':
    print_toilet_status()
