from toilet.toilet import Toilet
from threading import Timer
import gtk
import appindicator
import json
import urllib2

class ToiletIndicator:
  def __init__(self):
    datas = urllib2.urlopen('http://lights.theodo.fr')
    self.toilets = []
    for name, status in json.load(datas).iteritems():
      self.toilets.append(Toilet(name, status))
    
    self.ind = appindicator.Indicator("toilet", "indicator-messages", appindicator.CATEGORY_APPLICATION_STATUS)
    self.ind.set_status(appindicator.STATUS_ACTIVE)
    self.ind.set_attention_icon("indicator-messages-new")

    # create a menu
    menu = gtk.Menu()

    # create some 
    for toilet in self.toilets:
      buf = toilet.to_string()
      
      menu_items = gtk.MenuItem(buf)

      menu.append(menu_items)

      # this is where you would connect your menu item up with a function:
                                          
      # menu_items.connect("activate", menuitem_response, buf)

      # show the items
      menu_items.show()

      self.ind.set_menu(menu)

    self.timer = Timer(5.0, self.update())
    self.timer.start()

  def menuitem_response(w, buf):
    print buf

  def update(self):
    for toilet in self.toilets:
      if toilet.is_free() is False:
        self.ind.set_status(appindicator.STATUS_ATTENTION)
        print 'ATTENTION'
      else:
        self.ind.set_status(appindicator.STATUS_ACTIVE)
        print 'ACTIVE'

if __name__ == "__main__":
  indicator = ToiletIndicator()
  gtk.main()
