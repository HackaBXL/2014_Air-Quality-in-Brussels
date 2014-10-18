# -*- coding: utf-8 -*-
'''
dustbusters.controllers.heatmap description
'''
import os
import json
from operator import pos
from dustbusters.config import DATA_LOG

__author__ = " jph"
__email__ = "jph@openjph.be"
__copyright__ = "Copyright 2014, Jean Pierre Huart"
__license__ = "GPLv3"
__date__ = "2014-10-17"
__version__ = "1.0"
__status__ = "Development"

# POINT = "lat:{0}, lng:{1}, count: {2}"
POINT = "[{0}, {1}, {2}]"

class HeatMap(object):
    """
    var testData = {
          max: 8,
          data: [{lat: 24.6408, lng:46.7728, count: 3},{lat: 50.75, lng:-1.55, count: 1},...
        };
    """
    def __init__(self):
        pass

    def generate_points_per_polluant(self, polluant):
        '''
        read the respective file in DATA_LOG/treated
        
        C6H6, 
        '''
        references = {'C6H6':{'red':5,'yellow':2, 'green':0, 'density':10},
                      'CO':{'red':10,'yellow':5, 'green':1, 'density':20},
                      'NO2':{'red':200,'yellow':60, 'green':0, 'density':10},
                      'O3':{'red':150,'yellow':60, 'green':0, 'density':10},
                      'PM2.5':{'red':25,'yellow':12, 'green':0, 'density':10},
                      'PM10':{'red':100,'yellow':40, 'green':0, 'density':10},
                      'SO2':{'red':125,'yellow':45, 'green':0, 'density':10},
                      }
        
        datafile = os.path.join(DATA_LOG,'treated/2014-10-18T15-51-33_heatmap_{}.js'.format(polluant))
        with open(datafile, 'r') as f:
            datastr = f.read()
            
        points = json.loads(datastr)
            
        red_limit = references[polluant]['red']
        yellow_limit = references[polluant]['yellow']
        green_limit = references[polluant]['green']
         
        red_content = " var redPoints = ["
        yellow_content = " var yellowPoints = ["
        green_content = " var greenPoints = ["
 
        with open('../server/pages/static/js/bruxelles_{0}.js'.format(polluant), 'w') as f:
 
            for point in points:
#                 cloud = [(round((point[0] + x/100000.0),6), round((point[1] + x/100000.0),6), point[2]) for x in range(point[2]*density_factor)]
                cloud = self.spiral(10000, (point[0], point[1]), point[2] * references[polluant]['density'])
                for item in cloud:
                    if point[2] <= yellow_limit:
                        green_content += POINT.format(item[0], item[1], point[2]) + ","
                    elif point[2] > yellow_limit and point[2] <= red_limit:
                        yellow_content += POINT.format(item[0], item[1], point[2]) + ","
                    elif point[2] > red_limit:
                        red_content += POINT.format(item[0], item[1], point[2]) + ","
 
            red_content += "]; "
            yellow_content += "]; "
            green_content += "]; "
 
            file_content = red_content + yellow_content + green_content
            f.write(file_content)
            f.closed

        return
    
    def generate_points(self):
        density_factor = 2

        points = [(50.825128, 4.384634, 100)
                  , (50.825128, 4.384634, 200)
                  , (50.845742, 4.368667, 300)
                  , (50.858031, 4.288336, 100)
                  , (50.796632, 4.358539, 200)
                  , (50.883560, 4.382963, 300)
                  , (50.857225, 4.425704, 100)
                  , (50.895101, 4.392718, 200)
                  , (50.825128, 4.384634, 300)
                  , (50.819982, 4.311547, 100)
                  , (50.840789, 4.376149, 200)
                  , (50.838631, 4.374388, 300)
                  , (50.850811, 4.348587, 100)
                  , (50.810469, 4.327861, 200)]

        red_limit = 200
        yellow_limit = 100
        green_limit = 0
        
        red_content = " var redPoints = ["
        yellow_content = " var yellowPoints = ["
        green_content = " var greenPoints = ["

        with open('../server/pages/static/js/bruxelles_100.js', 'w') as f:

            for point in points:
#                 cloud = [(round((point[0] + x/100000.0),6), round((point[1] + x/100000.0),6), point[2]) for x in range(point[2]*density_factor)]
                cloud = self.spiral(10000, (point[0], point[1]), point[2] * density_factor)
                for item in cloud:
                    if point[2] <= yellow_limit:
                        green_content += POINT.format(item[0], item[1], point[2]) + ","
                    elif point[2] > yellow_limit and point[2] <= red_limit:
                        yellow_content += POINT.format(item[0], item[1], point[2]) + ","
                    elif point[2] > red_limit:
                        red_content += POINT.format(item[0], item[1], point[2]) + ","

            red_content += "]; "
            yellow_content += "]; "
            green_content += "]; "

            file_content = red_content + yellow_content + green_content
            f.write(file_content)
            f.closed

        return

    def spiral(self, scale, pos, end):

        def move_right(x, y):
            return x + 1, y

        def move_down(x, y):
            return x, y - 1

        def move_left(x, y):
            return x - 1, y

        def move_up(x, y):
            return x, y + 1

        moves = [move_right, move_down, move_left, move_up]

        pos = scale * pos[0], scale * pos[1]

        from itertools import cycle
        _moves = cycle(moves)
        n = 1
        times_to_move = 1

        yield pos[0] / scale, pos[1] / scale  # pos

        while True:
            for _ in range(2):
                move = next(_moves)
                for _ in range(times_to_move):
                    if n >= end:
                        return
                    pos = move(*pos)
                    n += 1
                    yield pos[0] / scale, pos[1] / scale  # pos

            times_to_move += 1

        return
