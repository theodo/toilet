# -*- coding: utf-8 -*-
__author__ = 'Benjamin Grandfond <benjaming@theodo.fr>'

import unittest
from mock import Mock
from toilet.toilet import Toilet
from toilet.indicator import ToiletIndicator

class TestIndicator(unittest.TestCase):
    def setUp(self):
        self.toilets = {
            'women': Toilet('Women', 'captor1', False), # used
            'men':   Toilet('Men', 'captor2', True)     # free
        }

        self.indicator = ToiletIndicator(self.toilets, 0)

        # Mock timer methods
        self.indicator.icon_directory = Mock(return_value='')
        self.indicator.update_toilets = Mock()

    def test_update_icons(self):
        self.assertFalse(self.toilets['women'].is_free())
        self.assertTrue(self.toilets['men'].is_free())
        self.assertEqual(self.indicator.update_icon(), 'toilets_queen.png')

        self.toilets['women'].update(True) # free
        self.toilets['men'].update(False)  # used
        self.assertTrue(self.toilets['women'].is_free())
        self.assertFalse(self.toilets['men'].is_free())
        self.assertEqual(self.indicator.update_icon(), 'toilets_king.png')

        self.toilets['women'].update(False) # used
        self.toilets['men'].update(False)   # used
        self.assertFalse(self.toilets['women'].is_free())
        self.assertFalse(self.toilets['men'].is_free())
        self.assertEqual(self.indicator.update_icon(), 'toilets_used.png')

        self.toilets['women'].update(True) # free
        self.toilets['men'].update(True)   # free
        self.assertTrue(self.toilets['women'].is_free())
        self.assertTrue(self.toilets['men'].is_free())
        self.assertEqual(self.indicator.update_icon(), 'toilets.png')

if __name__ == '__main__':
    unittest.main()
