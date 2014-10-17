# -*- coding: utf-8 -*-
""" 
All what concerns User Interface needs an access to the static files.
    For that a symlink has to be created in folder ``/var/log/dustbusters`` pointing to the development folder::
    
        sudo ln -s /opt/venvpy/dustbusters-env/dustbusters/src/dustbusters/server/dustbusters/static
        
"""

import tornado.httpserver
import tornado.web
import logging
from dustbusters.config import TORNADO_PORT

__author__ = "dustbusters"
__email__ = "openjph@gmail.com"
__copyright__ = "Copyright 2014, Jean Pierre Huart"
__license__ = "GPLv3"
__date__ = "2014-10-17"
__version__ = "1.0"
__status__ = "Development"

# The default server port.
#TORNADO_PORT = 9393
#The message displayed at the root level
HELLO_MSG = """

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>dustbusters available webservices</title>
</head>
<body>
    <div>
        <p>Hello, this is the root connection string to the dustbusters webservices.</p>
    </div>
</body>
</html>

"""

## HANDLERS ########################################################

class MainHandler(tornado.web.RequestHandler):
    """ 
    Display all applications available at this address 
    """
    def get(self):
        """
        init function for a Tornado application.
        It will prepare arguments and launch the application.
        """
        self.write(HELLO_MSG)
        return       
     

 # SERVER ##########################################################################
        
class TornadoServer():
    """ 
    
    .. _TornadoServer: 
       
    The Tornado server: implementation of the python library Tornado.
    
    The launch of the server is done through a shell script: 'startwsdustbusters' 
    """
    logger = logging.getLogger('tornado.dustbusters')
    static_file_path = '/var/log/dustbusters/static/'
    application = tornado.web.Application([
                                (r"/", MainHandler),
                                (r'.*/static/(.*)', tornado.web.StaticFileHandler, {'path': static_file_path}),                            
                            ])
    http_server = None
    ioloop = tornado.ioloop.IOLoop.instance()
    
    def __init__(self, port=int(TORNADO_PORT)):
        self.logger.debug('init Tornado Server')
        self.port = port
        self.http_server = tornado.httpserver.HTTPServer(self.application) 
        self.http_server.listen(self.port) 
        
        return
    
    def start(self):
        """ Start the server """
        try:
            self.logger.debug('Starting Tornado Server')
            self.ioloop.start()
        
        except (KeyboardInterrupt, SystemExit):
            self.stop()
            return 
        
        return
    
    def stop(self):
        """ Stop the server """
        try:
            self.logger.debug('Stopping Tornado Server')
            self.ioloop.stop()
            self.http_server.stop()
            self.logger.debug('Tornado Server Stopped')
        except:
            raise
        
        return

if __name__ == '__main__':
    print TornadoServer.__doc__
    