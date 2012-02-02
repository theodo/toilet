__author__ = 'benjamin'

from fabric.api import *
from fabric.tasks import Task

class TestTask(Task):
    name = 'test'

    def run(self):
        local('python -m unittest discover')

instance = TestTask()