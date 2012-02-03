# -*- coding: utf-8 -*-
__author__ = 'Benjamin Grandfond <benjaming@theodo.fr>'

from fabric.api import *
from fabric.tasks import Task

class TestTask(Task):
    """
    Run toilet tests.
    """
    name = 'test'

    def run(self):
        local('python -m unittest discover')

instance = TestTask()