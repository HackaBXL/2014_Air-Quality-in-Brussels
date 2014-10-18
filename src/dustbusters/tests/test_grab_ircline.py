# -*- coding: utf-8 -*-
"""
Module de test pour ctl_email.
"""
import unittest
from dustbusters.controllers.grab_irceline import main

__author__ = "Jean Pierre Huart"
__email__ = "jph@openjph.be"
__copyright__ = "Copyright 2014, Jean Pierre Huart"
__license__ = "GPLv3"
__date__ = "2014-10-17"
__version__ = "1.0"
__status__ = "Development"

   
class TestGrabIrceline(unittest.TestCase):
    
    def test_main(self):
        result = main()
        print result
 
        return            
        
        
if __name__ == '__main__':
    unittest.main()
