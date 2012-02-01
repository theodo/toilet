from toilet import Toilet
import gobject
import gtk
import appindicator
import json
import urllib2

class ToiletIndicator:
  def __init__(self):
    datas = urllib2.urlopen('http://lights.theodo.fr')
    toilets = []
    for name, status in json.load(datas).iteritems():
      toilets.append(Toilet(name, status))
    
    self.ind = appindicator.Indicator("toilet", "indicator-messages", appindicator.CATEGORY_APPLICATION_STATUS)
    self.ind.set_status(appindicator.STATUS_ACTIVE)
    self.ind.set_attention_icon("indicator-messages-new")

    # create a menu
    menu = gtk.Menu()

    # create some 
    for toilet in toilets:
      buf = toilet.to_string()
      
      menu_items = gtk.MenuItem(buf)

      menu.append(menu_items)

      # this is where you would connect your menu item up with a function:
                                          
      # menu_items.connect("activate", menuitem_response, buf)

      # show the items
      menu_items.show()

      self.ind.set_menu(menu)
    
  def menuitem_response(w, buf):
    print buf

if __name__ == "__main__":
  indicator = ToiletIndicator()
  gtk.main()
