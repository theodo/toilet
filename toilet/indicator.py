# -*- coding: utf-8 -*-
__author__ = 'Benjamin Grandfond <benjaming@theodo.fr>'

from toilet import Toilet
from threading import Timer
import os
import gtk
import appindicator
import json
import urllib2

class ToiletIndicator:
    def __init__(self):
        self.ind = appindicator.Indicator("toilet",
                                          self.icon_free(),
                                          appindicator.CATEGORY_APPLICATION_STATUS)
        self.ind.set_status(appindicator.STATUS_ACTIVE)
        self.ind.set_attention_icon(self.icon_used())

        self.initialize_toilets()
        self.ind.set_menu(self.create_menu())

        #self.poll()

    def create_menu(self):
        """
        Create a gtk Menu with toilet menu items.
        """
        menu = gtk.Menu()
        menu.append(self.wemen_toilet.menu_item)
        self.wemen_toilet.menu_item.show()

        menu.append(self.men_toilet.menu_item)
        self.men_toilet.menu_item.show()

        return menu

    def icon_directory(self):
        return os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "./images" + os.path.sep

    def icon_free(self):
        return self.icon_directory() + "toilet-free.png"

    def icon_used(self):
        return self.icon_directory() + "toilet-used.png"

    def initialize_toilets(self):
        self.wemen_toilet = Toilet('Wemen', 'captor1')
        self.wemen_toilet.menu_item = gtk.MenuItem(self.wemen_toilet.to_string())

        self.men_toilet   = Toilet('Men', 'captor2')
        self.men_toilet.menu_item = gtk.MenuItem(self.men_toilet.to_string())

        self.update_toilets()

    def poll(self):
        print 'Toilets statuses will be updated in 1 seconds'
        Timer(3.0, self.update_toilets).start()

    def update_toilets(self):
        print 'Updating toilets statuses from http://lights.theodo.fr'
        #datas = json.load(urllib2.urlopen('http://lights.theodo.fr'))

        #self.wemen_toilet.update(datas[self.wemen_toilet.captor()])
        #self.men_toilet.update(datas[self.men_toilet.captor()])

        self.wemen_toilet.update(False if self.wemen_toilet.is_free() else True)
        self.men_toilet.update(False if self.men_toilet.is_free() else True)

        for toilet in [self.wemen_toilet, self.men_toilet]:
            if toilet.is_free() is False:
                self.ind.set_status(appindicator.STATUS_ATTENTION)
            else:
                self.ind.set_status(appindicator.STATUS_ACTIVE)
            print toilet.to_string()

        #self.poll()
        Timer(3.0, self.update_toilets).start()


if __name__ == "__main__":
    indicator = ToiletIndicator()
    gtk.main()
