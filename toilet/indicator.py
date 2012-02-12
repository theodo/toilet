# -*- coding: utf-8 -*-
__author__ = 'Benjamin Grandfond <benjaming@theodo.fr>'

from toilet import Toilet
from dataloader import Dataloader
import os
import gtk
import gobject
import appindicator
import json
import urllib2
import logging

class ToiletIndicator:
    def __init__(self, toilets, loader, tempo=3000):
        self.women_toilet = toilets['women']
        self.men_toilet   = toilets['men']
        self.loader =loader
        self.tempo = tempo

        self.ind = appindicator.Indicator("toilet",
            self.update_icons(),
            appindicator.CATEGORY_APPLICATION_STATUS
        )
        self.ind.set_status(appindicator.STATUS_ACTIVE)
        self.ind.set_attention_icon(self.update_icons())
        self.create_menu()

        self.poll()

    def poll(self):
        """
        Starts polling.
        """
        # Use 0 for tempo in tests
        if self.tempo > 0:
            gobject.timeout_add(self.tempo, self.update_toilets)

    def create_menu(self):
        """
        Create a gtk Menu with toilet menu items.
        """
        self.menu = gtk.Menu()

        self.women_menu_item = gtk.MenuItem(unicode(self.women_toilet))
        self.menu.append(self.women_menu_item)
        self.women_menu_item.show()

        self.men_menu_item = gtk.MenuItem(unicode(self.men_toilet))
        self.menu.append(self.men_menu_item)
        self.men_menu_item.show()

        separator = gtk.SeparatorMenuItem()
        separator.show()
        self.menu.append(separator)

        item = gtk.MenuItem('Quit')
        item.connect("activate", gtk.main_quit, None)
        item.show()
        self.menu.append(item)

        self.ind.set_menu(self.menu)

    def update_labels(self):
        """
        Updates the labels of the menu items.
        """
        self.women_menu_item.get_child().set_label(unicode(self.women_toilet))
        self.men_menu_item.get_child().set_label(unicode(self.men_toilet))

    def update_icons(self):
        """
        Update icon with toilets status.
        """
        if self.women_toilet.is_free() is True:
            if self.men_toilet.is_free() is True:
                return self.icon_free()
            else:
                return self.icon_men()
        else:
            if self.men_toilet.is_free() is True:
                return self.icon_women()
            else:
                return self.icon_used()

    def icon_directory(self):
        """
        Returns the icons directory.
        """
        return os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "images" + os.path.sep

    def icon_free(self):
        """
        Returns the toilets free icon image.
        """
        return self.icon_directory() + "toilets.png"

    def icon_used(self):
        """
        Returns the toilets used icon image.
        """
        return self.icon_directory() + "toilets_used.png"

    def icon_men(self):
        """
        Returns the men toilets used icon image.
        """
        return self.icon_directory() + "toilets_king.png"

    def icon_women(self):
        """
        Returns the women toilets used icon image.
        """
        return self.icon_directory() + "toilets_queen.png"

    def update_toilets(self):
        """
        Update toilets' status.
        """
        try:
            datas = self.loader.load()

            self.women_toilet.update(datas[self.women_toilet.captor()])
            self.men_toilet.update(datas[self.men_toilet.captor()])

  
            self.ind.set_icon(self.update_icons())

            self.update_labels()

        except Exception as err:
            logging.error(str(err))  
        finally:
            self.poll()

if __name__ == "__main__":
    toilets = {
        'women': Toilet('Women', 'captor2', True),
        'men':   Toilet('Men', 'captor1', True)
    }
    indicator = ToiletIndicator(toilets, Dataloader())
    gtk.main()
