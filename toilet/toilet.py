# -*- coding: utf-8 -*-
__author__ = 'Benjamin Grandfond <benjaming@theodo.fr>'

class Toilet:

    FREE = 'free'
    USED = 'used'

    def __init__(self, name, captor, status=True):
        self.name    = name
        self._captor = captor
        self._status = self.convert_status(status)

    def __unicode__(self):
        return '%s is %s' % (self.name, self._status)

    def is_free(self):
        """
        Check if the toilet is free or used.
        """
        return True if self._status == self.FREE else False

    def captor(self):
        """
        Return the captor name.
        """
        return self._captor

    def update(self, status):
        status = self.convert_status(status)
        if status is not self._status:
            self._status = status

    @classmethod
    def convert_status(cls, status):
        """
        Convert a boolean or a int into a Toilet status (free or used).
        A toilet is free if the status var is True or an int > 80.
        A toilet is used if the status var is False or an int <= 80.
        """
        # Convert a bool or an int into free or false
        if status in [cls.FREE, cls.USED]:
            return status
        else:
            if isinstance(status, bool):
                return Toilet.FREE if status == True else Toilet.USED
            elif isinstance(status, int):
                return Toilet.FREE if status > 80 else Toilet.USED
            else:
                raise ValueError('status must be a boolean or an int, %s given' % type(status))
