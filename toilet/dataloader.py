# -*- coding: utf-8 -*-
__author__ = 'Benjamin Grandfond <benjaming@theodo.fr>'

import json
import urllib2

class Dataloader:
    def __init__(self):
        self.url = 'http://lights.theodo.fr';

    def load(self):
        return json.load(urllib2.urlopen(self.url))

class FakeDataloader():
    def __init__(self):
        self.captor_one = [True, False, False, True]
        self.captor_two = [True, True, False, False]
        self.iteration = 0

    def load(self):
        if self.iteration == len(self.captor_one):
            self.iteration = 0

        datas = {
            'captor1': self.captor_one[self.iteration],
            'captor2': self.captor_two[self.iteration],
        }

        self.iteration += 1

        return datas

class NoJSONDataloader:
    def load(self):
        return [] 

class StringDataloader:
    def load(self):
        return "Error occured on loading API datas." 
