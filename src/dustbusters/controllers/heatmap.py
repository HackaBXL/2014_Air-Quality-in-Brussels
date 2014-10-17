# -*- coding: utf-8 -*-
'''
dustbusters.controllers.heatmap description
'''
from operator import pos
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

    def generate_points(self):
        density_factor = 2
        points = [(50.845435, 4.368734, 300),
                  (50.824888, 4.384960, 120),
                  (50.849608, 4.333822, 150),
                  (50.858759, 4.288101, 90),
                  (50.798823, 4.358099, 10), 
                  (50.893809, 4.398908, 250),
                  (50.833451, 4.431915, 30)]
        
        red_content = " var redPoints = ["
        yellow_content = " var yellowPoints = ["
        green_content = " var greenPoints = ["
        
        with open('../server/dustbusters/static/js/bruxelles.100.js', 'w') as f:
            
            for point in points:
#                 cloud = [(round((point[0] + x/100000.0),6), round((point[1] + x/100000.0),6), point[2]) for x in range(point[2]*density_factor)]
                cloud = self.spiral(10000, (point[0],point[1]), point[2]*density_factor)
                for item in cloud:
                    if point[2] <= 100:
                        green_content += POINT.format(item[0],item[1],point[2]) + ","
                    elif point[2] > 100 and point[2] <= 200:
                        yellow_content += POINT.format(item[0],item[1],point[2]) + ","
                    elif point[2] > 200:
                        red_content += POINT.format(item[0],item[1],point[2]) + ","
            
            red_content += "]; "
            yellow_content += "]; "
            green_content += "]; "
            
            file_content = red_content + yellow_content + green_content
            f.write(file_content)
            f.closed

        return
    
    def spiral(self, scale, pos, end):
        
        def move_right(x,y):
            return x+1, y
        
        def move_down(x,y):
            return x,y-1
        
        def move_left(x,y):
            return x-1,y
        
        def move_up(x,y):
            return x,y+1
        
        moves = [move_right, move_down, move_left, move_up]        
        
        pos = scale*pos[0],scale*pos[1]
        
        from itertools import cycle
        _moves = cycle(moves)
        n = 1
        times_to_move = 1
    
        yield pos[0]/scale,pos[1]/scale #pos
    
        while True:
            for _ in range(2):
                move = next(_moves)
                for _ in range(times_to_move):
                    if n >= end:
                        return
                    pos = move(*pos)
                    n+=1
                    yield pos[0]/scale,pos[1]/scale #pos
    
            times_to_move+=1
        
        return
