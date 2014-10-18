# -*- coding: utf-8 -*-
""" 
HTML tornado templates for jQuery Mobile.
+++++++++++++++++++++++++++++++++++++++++  

remember: data-ajax="false"

"""
__author__ = "Jean Pierre Huart"
__email__ = "jph@openjph.be"
__copyright__ = "Copyright 2014, Jean Pierre Huart"
__license__ = "GPLv3"
__date__ = "2014-07-03"
__version__ = "1.0"
__status__ = "Development"

DLG_BODY = u'''
{% autoescape None %}
<body>
    <div data-role="page" id="{{ page_id }}">
    
        <div data-role="header" id="myheader">
            {{ body_header }}
        </div><!-- /header -->
        
        <div data-role="content">
            {{ body_content }}
        </div><!-- /content -->
            
        <div data-role="footer">
            {{ body_footer }}
        </div><!-- /footer -->
        
    </div><!-- /page -->
</body>
'''


DLG_FRM = u'''
{% autoescape None %}
<FORM action="{{ action }}" method="{{ method }}" class="{{ myclass }}">
    {{ frm_content }}
</FORM>
''' 


DLG_FRM_BTN = u'''
{% autoescape None %}
<button type="{{ type }}" data-theme="{{ theme }}" name="{{ name }}" value="{{ value }}">{{ btnlabel }}</button>
'''


DLG_FRM_BTN_JS = u'''
<button id="{{ id }}" class="{{ myClass }}">{{ label }}</button>
'''


DLG_FRM_DATE = u'''
<div id="div_{{ id }}" class="ui-field-contain">
    <label for="{{ id }}">{{ datelabel }}</label>
    <input name="{{ name }}" id="{{ id }}" placeholder="{{ datelabel }}" data-role="date" type="text">
</div>
'''

DLG_FRM_DATE_0 = u'''
<div class="ui-field-contain">
    <input name="{{ name }}" id="{{ id }}" placeholder="{{ datelabel }}" data-role="date" type="text">
</div>
'''


DLG_FRM_INPHID = u'''
<input name="{{ id }}" id="{{ id }}" value="{{ myValue }}" type="hidden">
'''


DLG_FRM_INPTEXT = u'''
<div class="ui-field-contain">
    <label for="{{ id }}" class="{{ myClass }}">{{ myLabel }}</label>
    <input name="{{ id }}" id="{{ id }}" value="{{ myValue }}" placeholder="{{ myLabel }}" data-theme="{{ myTheme }}" type="text">
</div>
'''


DLG_FRM_RADIO = u'''
{% autoescape None %}
<fieldset id="{{ id }}" data-role="controlgroup" data-type="{{ placement }}">
        <legend>{{ legend }}</legend>
        {{ choices }}
</fieldset> 
'''  
  
  
DLG_FRM_RADIO_CHOICE = u'''
{% autoescape None %}
<input name="{{ name }}" id="{{ id }}" value="{{ value }}" {{ checked }} type="radio" data-theme="{{ theme }}">
<label for="{{ id }}">{{ chclabel }}</label>
'''

DLG_GRID = u'''
{% autoescape None %}
<div class="ui-grid-a">
{% for item in items %}
  <div class="{{ item['myblock'] }}"><div class="{{ item['myclass'] }}">{{ item['mycontent'] }}</div></div>
{% end %}
</div>
'''

DLG_BTN_GRID_2 = u'''
{% autoescape None %}
<div class="ui-grid-a ui-responsive">
{% for item in items %}
  <div class="{{ item['block'] }}"><a href="{{ item['href'] }}" class="{{ item['myclass'] }}">{{ item['label'] }}</a></div>
{% end %}
</div>
'''
    
    
DLG_BTN_GRID_3 = u'''
{% autoescape None %}
<div class="ui-grid-b ui-responsive">
{% for item in items %}
  <div class="{{ item['block'] }}"><a href="{{ item['href'] }}" class="{{ item['myclass'] }}">{{ item['label'] }}</a></div>
{% end %}
</div>
'''

DLG_HEAD = u'''
{% autoescape None %}
<head>
    <title>{{ header_title }}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">    
    <link rel="stylesheet" href="/static/themes/jquery.mobile.icons.min.css" />
    <link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet-0.7.2/leaflet.css" /> 
    <link rel="stylesheet" href="/static/css/jquery.mobile.structure-1.4.3.min.css" /> 
    <link rel="stylesheet" href="/static/css/global.css" />   
        
    <script src="/static/js/jquery-1.11.1.min.js"></script>
    <!-- <script src="/static/js/jquery.mobile-1.4.3.min.js"></script> -->
    
    <script src="http://cdn.leafletjs.com/leaflet-0.7.2/leaflet.js"></script>
    <script src="/static/js/leaflet-heat.js"></script> 
    <script src="/static/js/{{ datajs }}"></script>    
        
</head>
'''


DLG_HTML = u'''
{% autoescape None %}
<!doctype html>
<html>
    {{ html_content }}
</html>
'''


DLG_LINK_BTN = u'''
{% autoescape None %}
<a href="{{ href }}" class="{{ myclass }}" target="{{ target }}">{{ btnlabel }}</a>
'''


DLG_DWNL_BTN = u'''
{% autoescape None %}
<a href="{{ href }}" class="{{ myclass }}" data-ajax="false">{{ btnlabel }}</a>
'''

DLG_POPUP_MSG = u'''
{% autoescape None %}
<div data-role="popup" id="{{ popupId }}" data-theme="{{ myTheme }}" class="ui-corner-all">
    <a id="btnClose{{ popupId }}" href="#" data-rel="back" class="{{ btnCloseClass }}">{{ btnCloseLabel }}</a>    
    <div style="padding:10px 20px;">                    
        <h3>{{ popupTitle }}</h3>            
        <div id="{{ popupId }}Message">{{ popupItems }}</div>         
    </div>
</div>
'''

DLG_POPUP_SAVE = u'''
{% autoescape None %}
<a href="#{{ popupId }}" data-rel="popup" data-position-to="window" class="{{ btnClass }}" data-transition="pop">{{ btnLabel }}</a>
<div data-role="popup" id="{{ popupId }}" data-theme="{{ myTheme }}" class="ui-corner-all">
    <a id="btnClose{{ popupId }}" href="#" data-rel="back" class="{{ btnCloseClass }}">{{ btnCloseLabel }}</a>
    
        <div style="padding:10px 20px;">                    
            <h3>{{ popupTitle }}</h3>            
            {{ popupItems }}            
            <button id="btnSave{{ popupId }}" class="{{ btnSaveClass }}">{{ btnSaveLabel }}</button>
        </div>

</div>
'''


DLG_SELECT_1 = u'''
{% autoescape None %}
<div data-role="ui-field-contain">
   <label for="{{ name }}" class="select">{{ label }}</label>
   <select name="{{ name }}" id="{{ name }}" data-theme="{{ theme }}">
        {% for item in options %}           
          <option value="{{ item[0] }}" {{ item[2] }}>{{ item[1] }}</option>
        {% end %}
   </select>
</div>
'''

DLG_SELECT_STP = u'''
{% autoescape None %}
<div data-role="ui-field-contain">
   <label for="{{ name }}" class="select">{{ label }}</label>
   <select name="{{ name }}" id="{{ name }}" data-theme="{{ theme }}">
        {% for item in options %}           
          <option date_start="{{ item[2] }}" value="{{ item[0] }}" {{ item[3] }}>{{ item[1] }}</option>
        {% end %}
   </select>
</div>
'''


DLG_TABS_NAV_0 = u'''
{% autoescape None %}
<div data-role="tabs" id="tabs">
  <div data-role="navbar">
    <ul>
    {% for item in mytabs %}
          <li><a href="#{{ item['id'] }}" data-ajax="false" class="{{ item['mybtnclass'] }}" >{{ item['tab_title'] }}</a></li>
    {% end %}
    </ul>
    <br />
  </div>
  {% for item in mytabs %}
     <div id="{{ item['id'] }}" class="{{ item['mytabclass'] }}">
        {{ item['content'] }}
      </div>
  {% end %}
</div>
'''


DLG_TABLE_FILTER = u'''
<frm>
    <input id="{{ name }}" name="{{ name }}" data-type="search">
</frm>
'''


DLG_TABLE = u'''
{% autoescape None %}
<div>
    <table data-role="table" id="{{ id }}" data-mode="columntoggle" class="ui-responsive table-stroke table-stripe" {{ filter }}>
         <thead>
             {{ tblhead }}       
         </thead>
         <tbody>
            {{ tblbody }}
        </tbody>
    </table>
</div>
'''
