# -*- coding: utf-8 -*-
__author__='Benjamin Grandfond <benjaming@theodo.fr>'

from threading import Timer

class Toilet:

    FREE = 'free'
    USED = 'used'

    def __init__(self, name, status):
        self.name   = name

        # Convert a bool or an int into free or false
        if status not in [self.FREE, self.USED]:
            convert_status(status)
        self.status = status

    def to_string(self):
        return '%s is %s' % (self.name, self.status)

    def is_free(self):
        return True if self.status == self.FREE else False

    @classmethod
    def convert_status(cls, status):
        """
        Convert a boolean or a int into a Toilet status (free or used).
        A toilet is free if the status var is True or an int > 80.
        A toilet is used if the status var is False or an int <= 80.

        """
        if isinstance(status, bool):
            return Toilet.FREE if status == True else Toilet.USED
        elif isinstance(status, int):
            return Toilet.FREE if status > 80 else Toilet.USED
        else:
            raise ValueError('status must be a boolean or an int, %s given' % type(status))
