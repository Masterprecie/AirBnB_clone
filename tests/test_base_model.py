#!/usr/bin/python3
""" Module of Unittests """
import unittest
from models.base_model import BaseModel
import os
from models import storage
from models.engine.file_storage import FileStorage
import datetime

class BaseModelTests(unittest.TestCase):
    """ Suite of Console Tests """
    
    my_model = BaseModel()

    def testBaseModel1(self):
        """ Test attributes value of a BaseModel instance """
