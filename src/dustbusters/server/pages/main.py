# -*- coding: utf-8 -*-
"""
HTML pages.
-----------

Collection of the available HTML5 pages.

These pages use Tornado templates specific to JQuery Mobile syntax to build the HTML5.
All these templates are in the ``energizair.server.dialogs.html_tornado_templates.py`` module.

"""

from tornado import template

from dustbusters.server.pages.html_tornado_templates import *

__author__ = "Jean Pierre Huart"
__email__ = "jph@openjph.be"
__copyright__ = "Copyright 2014, Jean Pierre Huart"
__license__ = "GPLv3"
__date__ = "2014-10-18"
__version__ = "1.0"
__status__ = "Development"

class Dialog(object):
    """
    Abstract class for all HTML pages

    :param user: description of the current user.
    :type user: dict
    """

    def __init__(self):
        """
        Initialize global properties
        """
        pass

        return

#     def _build_footer(self):
#         """
#         Tool to have a similar footer on all pages
#         """
# 
#         t = template.Template(DLG_LINK_BTN)
# 
#         footer = t.generate(href=u"http://www.youtube.com/user/EnergizAIRproject", myclass="youtube ui-shadow ui-btn ui-corner-all ui-btn-inline ui-btn-icon-notext ui-icon-youtube", target="_blank", btnlabel="YouTube")
#         footer += t.generate(href=u"http://www.energizair.eu", myclass="ui-shadow ui-btn ui-corner-all ui-btn-inline ui-btn-icon-left ui-mini ui-icon-heart", target="_blank", btnlabel=u"my www")
#         footer += t.generate(href= u"/", myclass="ui-shadow ui-btn ui-corner-all ui-btn-inline ui-btn-icon-left ui-mini ui-icon-home", target="_self", btnlabel=u"Homepage")
#         if blnUsrPref:
#             footer += self._build_user_preferences_popup()
#         if blnquit:
#             footer += t.generate(href= u"/bye?widget=bye", myclass="ui-shadow ui-btn ui-corner-all ui-btn-inline ui-btn-icon-left ui-mini ui-icon-power", target="_self", btnlabel=u"Quit")
# 
# 
#         return footer


class DialogHome(Dialog):
    """
    Homepage.

    :param title: title to be displayed.
    :type title: string
    :param description: description to be displayed.
    :type description: string
    :param widget: identifier of the page.
    :type widget: string

    """

    def __init__(self, title, polluant):

        super(DialogHome, self).__init__()
        """ header """
        self.title = u'<div id="title"><h1>{0}</h1></div><div id="cont-ind"><div id="indicator"></div></div>'.format(title)
        
        t = template.Template(DLG_HEAD)
        myhead = t.generate(header_title=u"Dustbusters demo",datajs='bruxelles_{0}.js'.format(polluant))
        
        """ body"""
        mycontent = u'''
        <div id="cont-cont">
            <div id="cont-map">
                <div id="map"></div>
            </div>
            <div id="cont-legend"> 
                        
            <a href="/" class="linkbtn" target="_self">All</a>
            <a href="/?polluant=C6H6" class="linkbtn" target="_self">C6H6</a>
            <a href="/?polluant=CO" class="linkbtn" target="_self">CO</a>
            <a href="/?polluant=NO2" class="linkbtn" target="_self">NO2</a>
            <a href="/?polluant=O3" class="linkbtn" target="_self">O3</a>
            <a href="/?polluant=PM2.5" class="linkbtn" target="_self">PM2.5</a>
            <a href="/?polluant=PM10" class="linkbtn" target="_self">PM10</a>
            <a href="/?polluant=SO2" class="linkbtn" target="_self">SO2</a>
            
            </div> 
        </div>
        
        <script>
            var map = L.map(\'map\').setView([ 50.844947, 4.350579 ], 11);
            
            var tiles = L.tileLayer(\'http://{s}.tiles.mapbox.com/v3/{id}/{z}/{x}/{y}.png\',
                            {
                                attribution : \'<a href="https://www.mapbox.com/about/maps/">Terms and Feedback</a>\',
                                id : \'examples.map-20v6611k\'
                            }).addTo(map);
                                         
            //var heat_red = L.heatLayer(redPoints, {"radius":30, "gradient": {0.25: \'yellow\', 1: "red"} }).addTo(map);
            //var heat_yellow = L.heatLayer(yellowPoints, {\'radius\':30, \'gradient\': { 0.2: \'blue\',0.5: \'lime\',1: \'yellow\'} }).addTo(map);
            //var heat_green = L.heatLayer(greenPoints, {\'radius\':30, \'gradient\': { 0.2: \'black\',0.5: \'blue\',1: \'lime\'} }).addTo(map);
            
            var heat_red = L.heatLayer(redPoints, {"radius":30, "gradient": {1: "#C00000"} }).addTo(map);
            var heat_yellow = L.heatLayer(yellowPoints, {\'radius\':30, \'gradient\': { 1: \'#F8E748\'} }).addTo(map);
            var heat_green = L.heatLayer(greenPoints, {\'radius\':30, \'gradient\': { 1: \'#00FF00\'} }).addTo(map);
         
        </script>
        '''
        myfooter = u'''
        <div id="myfooter"> The Dustbastards </div>
        '''
        t = template.Template(DLG_BODY)
        mybody = t.generate(page_id="homepage", body_header=self.title, body_content=mycontent, body_footer=myfooter)

        html_content = myhead + mybody
        t = template.Template(DLG_HTML)
        self.page = t.generate(html_content=html_content)

        return
    
class DialogZZZ(Dialog):
    """
    Generic HTML page for under construction pages.

    :param title: title to be displayed.
    :type title: string
    :param description: description to be displayed.
    :type description: string
    :param widget: identifier of the page.
    :type widget: string

    """

    def __init__(self, title, description):

        super(DialogZZZ, self).__init__()

        self.title = u'<h1>{0}</h1>'.format(title)
        self.description = u'<p class="simpletext">{0}</p>'.format(description)

        t = template.Template(DLG_HEAD)

        myhead = t.generate(header_title=u"Dustbusters demo")

        t = template.Template(DLG_BODY)
        mybody = t.generate(page_id="bye", body_header=self.title, body_content=self.description, body_footer='')

        html_content = myhead + mybody
        t = template.Template(DLG_HTML)
        self.page = t.generate(html_content=html_content)

        return

if __name__ == '__main__':
    pass
