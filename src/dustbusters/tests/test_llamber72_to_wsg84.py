# -*- coding: utf-8 -*-
"""
Module de test pour ctl_email.
"""
import unittest
from dustbusters.controllers.llamber72_to_wsg84 import get_stations

__author__ = "Jean Pierre Huart"
__email__ = "jph@openjph.be"
__copyright__ = "Copyright 2014, Jean Pierre Huart"
__license__ = "GPLv3"
__date__ = "2014-10-17"
__version__ = "1.0"
__status__ = "Development"

   
class TestGrabIrceline(unittest.TestCase):
    
    def test_get_stations(self):
        list_stations = get_stations()
#         print list_stations['Ibge_stations']
#         for station in list_stations['Ibge_stations']:
#             print station['geo_epsg-wsg84']
        print [(station['geo_epsg-wsg84'], 100) for station in list_stations['Ibge_stations']]
 
        return            
        
        
if __name__ == '__main__':
    unittest.main()
