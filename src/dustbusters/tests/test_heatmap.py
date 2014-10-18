# -*- coding: utf-8 -*-
"""
Module de test pour ctl_email.
"""
import unittest
from dustbusters.controllers.heatmap import HeatMap

__author__ = "Jean Pierre Huart"
__email__ = "jph@openjph.be"
__copyright__ = "Copyright 2014, Jean Pierre Huart"
__license__ = "GPLv3"
__date__ = "2014-10-17"
__version__ = "1.0"
__status__ = "Development"
   
        
class TestHeatMap(unittest.TestCase):
    
    def test_generate_points_per_polluant(self):
        
        polluants = ['C6H6','CO','NO2','O3','PM2.5','PM10','SO2']
        ctrl = HeatMap()
        for item in polluants:
            result = ctrl.generate_points_per_polluant(item)
            print result
 
        return   
    
#     def test_spiral(self):
#         ctrl = HeatMap()
#         result = list(ctrl.spiral(1000, (4.323,-3.456), 25))
#         print result
#  
#         return           
        
        
if __name__ == '__main__':
    unittest.main()
