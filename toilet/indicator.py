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
        self.women_toilet = Toilet('Women', 'captor1')
        self.men_toilet   = Toilet('Men', 'captor2')

        self.ind = appindicator.Indicator("toilet",
            self.icon_free(),
            appindicator.CATEGORY_APPLICATION_STATUS
        )
        self.ind.set_status(appindicator.STATUS_ACTIVE)
        self.ind.set_attention_icon(self.icon_used())
        self.create_menu()

        self.update_toilets()

    def create_menu(self):
        """
        Create a gtk Menu with toilet menu items.
        """
        self.menu = gtk.Menu()

        self.women_menu_item = gtk.MenuItem(self.women_toilet.to_string())
        self.menu.append(self.women_menu_item)
        self.women_menu_item.show()

        self.men_menu_item = gtk.MenuItem(self.men_toilet.to_string())
        self.menu.append(self.men_menu_item)
        self.men_menu_item.show()

        self.ind.set_menu(self.menu)

    def update_labels(self):
        """
        Updates the labels of the menu items.
        """
        self.women_menu_item.get_child().set_label(self.women_toilet.to_string())
        self.men_menu_item.get_child().set_label(self.men_toilet.to_string())


    def icon_directory(self):
        return os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "./images" + os.path.sep

    def icon_free(self):
        return self.icon_directory() + "toilet-free.png"

    def icon_used(self):
        return self.icon_directory() + "toilet-used.png"

    def poll(self):
        print 'Toilets statuses will be updated in 1 seconds'
        Timer(3.0, self.update_toilets).start()

    def update_toilets(self):
        print 'Updating toilets statuses from http://lights.theodo.fr'
        #datas = json.load(urllib2.urlopen('http://lights.theodo.fr'))

        #self.women_toilet.update(datas[self.women_toilet.captor()])
        #self.men_toilet.update(datas[self.men_toilet.captor()])

        self.women_toilet.update(False if self.women_toilet.is_free() else True)
        self.men_toilet.update(False if self.men_toilet.is_free() else True)

        for toilet in [self.women_toilet, self.men_toilet]:
            if toilet.is_free() is False:
                self.ind.set_status(appindicator.STATUS_ATTENTION)
            else:
                self.ind.set_status(appindicator.STATUS_ACTIVE)
            print toilet.to_string()

        self.update_labels()
        self.poll()

if __name__ == "__main__":
    indicator = ToiletIndicator()
    gtk.main()
