# -*- coding: utf-8 -*-
__author__ = 'Benjamin Grandfond <benjaming@theodo.fr>'

import unittest
from mock import Mock
from toilet.toilet import Toilet
from toilet.indicator import ToiletIndicator
from toilet.dataloader import FakeDataloader, NoJSONDataloader, StringDataloader

class IndicatorTestCase(unittest.TestCase):
    def setUp(self):
        self.toilets = {
            'women': Toilet('Women', 'captor1', False), # used
            'men':   Toilet('Men', 'captor2', True)     # free
        }

        self.dataloader = FakeDataloader()

        ToiletIndicator.icon_directory = Mock(return_value='')
        self.indicator = ToiletIndicator(self.toilets, self.dataloader, tempo=0)
        self.indicator.poll = Mock()

    def test_update_iconss(self):
        self.assertFalse(self.toilets['women'].is_free()) # used
        self.assertTrue(self.toilets['men'].is_free())    # free
        self.assertEqual(self.indicator.update_icons(), 'toilets_queen.png')

        self.toilets['women'].update(True) # free
        self.toilets['men'].update(False)  # used
        self.assertTrue(self.toilets['women'].is_free())
        self.assertFalse(self.toilets['men'].is_free())
        self.assertEqual(self.indicator.update_icons(), 'toilets_king.png')

        self.toilets['women'].update(False) # used
        self.toilets['men'].update(False)   # used
        self.assertFalse(self.toilets['women'].is_free())
        self.assertFalse(self.toilets['men'].is_free())
        self.assertEqual(self.indicator.update_icons(), 'toilets_used.png')

        self.toilets['women'].update(True) # free
        self.toilets['men'].update(True)   # free
        self.assertTrue(self.toilets['women'].is_free())
        self.assertTrue(self.toilets['men'].is_free())
        self.assertEqual(self.indicator.update_icons(), 'toilets.png')

    def test_update_toilets(self):
        self.indicator.poll = Mock()

        self.assertFalse(self.toilets['women'].is_free())
        self.assertTrue(self.toilets['men'].is_free())
        self.assertEqual(self.indicator.ind.get_icon(), 'toilets_queen.png')

        self.indicator.update_toilets()
        self.assertTrue(self.toilets['women'].is_free())
        self.assertTrue(self.toilets['men'].is_free())
        self.assertEqual(self.indicator.ind.get_icon(), 'toilets.png')

        self.indicator.update_toilets()
        self.assertFalse(self.toilets['women'].is_free())
        self.assertTrue(self.toilets['men'].is_free())
        self.assertEqual(self.indicator.ind.get_icon(), 'toilets_queen.png')

        self.indicator.update_toilets()
        self.assertFalse(self.toilets['women'].is_free())
        self.assertFalse(self.toilets['men'].is_free())
        self.assertEqual(self.indicator.ind.get_icon(), 'toilets_used.png')

        self.indicator.update_toilets()
        self.assertTrue(self.toilets['women'].is_free())
        self.assertFalse(self.toilets['men'].is_free())
        self.assertEqual(self.indicator.ind.get_icon(), 'toilets_king.png')

    def test_update_toilets_error(self):

        try:
            self.indicator.dataloader = NoJSONDataloader()
            self.indicator.update_toilets()

            self.indicator.dataloader = StringDataloader()
            self.indicator.update_toilets()
        except Exception, err:
          self.fail('An error occurs : %s' % str(err))
        
if __name__ == '__main__':
    unittest.main()
