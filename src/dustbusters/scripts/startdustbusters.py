# -*- coding: utf-8 -*-
""" 
Script to launch TornadoServer_ (see here above) via the console. Several options are available:

-d    include extra debugging output in log
-l    define a custom file used for logging
-p    define a custom port for the server
--debug    alias of -d
--logfilename    alias of -l
--port    alias of -p

:Example:

>>> startdustbusters -d
    
"""
import argparse
import logging
import os
from dustbusters.server.tornado_server import TornadoServer
from dustbusters.config import TORNADO_PORT, TORNADO_LOG

__author__ = "Jean Pierre Huart"
__email__ = "jph@openjph.be"
__copyright__ = "Copyright 2013, Jean Pierre Huart"
__license__ = "GPLv3"
__date__ = "2014-08-29"
__version__ = "1.0"
__status__ = "Development"

# The welcome message written to stdout (in verbose mode only).
WELCOME_MESSAGE = """\

Welcome to the dustbusters Tornado Server!

The server is now running on this machine, 

providing webservices on port: {0}

providing logfile : {1}


To stop it just hit ctrl-c

Have a nice day!
"""

def _parse_arguments():
    """ Parse command line arguments using 'argparse'. """

    parser = argparse.ArgumentParser(
        prog        = 'startwsdustbusters',
        description = 'Start a Tornado server for the dustbusters webservices'
    )
    parser.add_argument(
        '-d', '--debug',
        action = 'store_true',
        help   = 'include extra debugging output in log',
    )
    parser.add_argument(
        '-l', '--logfilename',
        help    = 'file used for logging',
        default = ''
    )
    parser.add_argument(
        '-p', '--port',
        help    = 'the server port (defaults to {0})'.format(TORNADO_PORT),
        default = TORNADO_PORT,
        type    = int
    )

    return parser.parse_args()

    
def main():
    arguments   = _parse_arguments()
    myport      = arguments.port
    
    """ check that log directory exists """
    if not (os.path.isdir(TORNADO_LOG)):
        os.makedirs(TORNADO_LOG, 0755)
        
    logfilename = os.path.join(TORNADO_LOG, arguments.logfilename + 'server_' + str(myport) + '.log')   
    loglevel    = logging.DEBUG if arguments.debug else logging.WARNING

    logging.basicConfig(
        level    = loglevel,
        filename = logfilename,
        format   = "%(asctime)s:%(levelname)s:%(name)s %(message)s"
    )
    
    server = TornadoServer(port=myport)
    print WELCOME_MESSAGE.format(server.port, logfilename)
    server.start()
    
    return

if __name__ == '__main__':
    main()
