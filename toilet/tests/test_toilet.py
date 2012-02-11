# -*- coding: utf-8 -*-
__author__ = 'Benjamin Grandfond <benjaming@theodo.fr>'

import unittest
from toilet.toilet import Toilet

class ToiletTestCase(unittest.TestCase):
    def setUp(self):
        self.toilet = Toilet('toilet', 'captor', Toilet.FREE)

    def test_captor(self):
        self.assertEqual('captor', self.toilet.captor())

    def test_convert_status(self):
        self.assertEqual(Toilet.FREE, Toilet.convert_status(True))
        self.assertEqual(Toilet.USED, Toilet.convert_status(False))
        self.assertEqual(Toilet.FREE, Toilet.convert_status(1000))
        self.assertEqual(Toilet.USED, Toilet.convert_status(70))

    def test_convert_status_string_raise_error(self):
        try:
            Toilet.convert_status("70")
            self.fail('convert_status does not raise ValueError when converting string into status')
        except ValueError as err:
            self.assertIsInstance(err, ValueError)

    def test_is_free(self):
        self.assertTrue(self.toilet.is_free())

    def test_is_not_free(self):
        self.toilet.update(False)
        self.assertFalse(self.toilet.is_free())

    def test_unicode(self):
        self.assertEqual('toilet is free', unicode(self.toilet))

        self.toilet.update(Toilet.USED)
        self.assertEqual('toilet is used', unicode(self.toilet))

        self.toilet.update(False)
        self.assertEqual('toilet is used', unicode(self.toilet))

if __name__ == '__main__':
    unittest.main()
