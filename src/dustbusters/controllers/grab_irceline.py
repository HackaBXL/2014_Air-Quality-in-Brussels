#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 17 oct. 2014

@author: patrick
'''
import sys
import os
import datetime
import StringIO
import codecs
import json
import yaml
import urllib2
import collections

import lxml.etree as ET

import yaml_orderedDict

from dustbusters.config import DATA_LOG

# http://www.portailsig.org/content/python-projections-cartographiques-definitions-et-transformations-de-coordonnees
# http://all-geo.org/volcan01010/2012/11/change-coordinates-with-pyproj/


Cfg = '''
grab_irceline:
    Web:
        site: www.irceline.be
        path_file_table_fr: tables/actair/actair.php?lan=fr
    Xpath:
        table: //table
        label_column: //table/tr[@bgcolor]
        data_row: //table/div/tr[not(@bgcolor)]
        data_row_label: ./td[not(@align)] 
        data_row_value: ./td[@align]
    Local_path:
        
        stations: irceline_stations.yaml
        values: irceline_values.yaml
        heatmap: heatmap.js
    Global_quality_appreciation_label:
        '1':
            fr: excellent
            nl:
            en:
        '2':
            fr: très bon
            nl:
            en:
        '3':
            fr: bon
            nl:
            en:
        '4':
            fr: assez bon
            nl:
            en:
        '5':
            fr: moyen
            nl:
            en:
        '6':
            fr: médiocre
            nl:
            en:
        '7':
            fr: très médiocre
            nl:
            en:
        '8':
            fr: mauvais
            nl:
            en:
        '9':
            fr: très mauvais
            nl:
            en:
        '10':
            fr: exécrable
            nl:
            en:
            
'''

class Yaml_helpers(object):
    
    def read(self, str_path_file):
        _yml_data = None
        if os.path.exists(str_path_file):
            with codecs.open(str_path_file, 'r', 'utf-8') as _file:
                _yml_data = yaml.load(_file.read(), Loader=yaml_orderedDict.OrderedLoader)
        return _yml_data
    
    
    def write(self, yml_data, str_path_file):
        if len(yml_data) != 0:
            _str_yaml = yaml.dump(yml_data, default_flow_style=False, width=1024, explicit_start=True, explicit_end=True, Dumper=yaml_orderedDict.OrderedDumper)
            _str_yaml_unicode = _str_yaml.encode('utf-8').decode('unicode-escape')
            with codecs.open(str_path_file, 'w', 'utf-8') as _file:
                _file.write(_str_yaml_unicode)

class Json_helpers(object):
    def read(self, str_path_file):
        _jsn_data = None
        if os.path.exists(str_path_file):
            with codecs.open(str_path_file, 'r', 'utf-8') as _file:
                _jsn_data = json.loads(_file.read(), object_pairs_hook=collections.OrderedDict)
        return _jsn_data
    
    
    def write(self, jsn_data, str_path_file):
        if len(jsn_data) != 0:
            with codecs.open(str_path_file, 'w', 'utf-8') as _file:
                # do not sort_keys=True, we use odct
                _str_json = json.dumps(jsn_data, ensure_ascii=False, indent=2) # encoding='utf-8',  python2
                _file.write(_str_json)


def get_web_file(str_url):
        _str_html = None
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        try:
            _result = opener.open(str_url)
        except urllib2.HTTPError, e:
            print 'The server couldn\'t fulfill the request for %(file)s'%{'file':str_url}
            print 'Error code: ', e.code
        except urllib2.URLError, e:
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
        else:
            _str_html = _result.read()
        
        # memory
        _str_filename_store = os.path.join(DATA_LOG, datetime.datetime.now().strftime('%Y-%m-%dT%H-%M-%S') + '_ircline.html')
        with open(_str_filename_store, 'w') as _file:
            _file.write(_str_html)
            
        return _str_html


def get_el_page(str_url, _str_local_folder=None):
    
    #print str_url
    
    _el_root = None
    _str_html = None

        
    if _str_html == None:
        _str_html = get_web_file(str_url)

    if _str_html != None:
        parser = ET.HTMLParser()
        _etree   = ET.parse(StringIO.StringIO(_str_html), parser)
        _el_root = _etree.getroot()
    return _el_root


def data_2_js(dct_cfg, _dct_stations, _dct_values):
    
    _str_out = ''
    with open(datetime.datetime.now().strftime('%Y-%m-%dT%H-%M-%S') + '_' + dct_cfg['grab_irceline']['Local_path']['heatmap'], 'w') as _file:
        _file.write(_str_out)


def add_wsg84():
    #with  as _file:
    pass


def parse_table(dct_cfg, el_page):
    
    _dct_stations = {'irceline_stations':[]}
    _lst_el_table_row_heads = el_page.xpath(dct_cfg['grab_irceline']['Xpath']['label_column'])
    for _int_row, el_row in enumerate(_lst_el_table_row_heads):
        _str_row = ET.tostring(el_row)
        _lst_cells = el_row.xpath('./td')
        if len(_lst_cells) > 2:
            if _int_row == 0:
                _dct_stations_label = []
                for _el_cell in _lst_cells: 
                    _dct_stations_label.append(' '.join(_el_cell.itertext()))
            elif _int_row == 1:
                _dct_stations_label_note = [None, None]
                for _int_cell, _el_cell in enumerate(_lst_cells): 
                    if _int_cell != 0:
                        _dct_stations_label_note.append(' '.join(_el_cell.itertext()))
            elif _int_row == 2:
                _dct_stations_label_unit = [None, None]
                for _int_cell, _el_cell in enumerate(_lst_cells): 
                    if _int_cell != 0:
                        _dct_stations_label_unit.append(' '.join(_el_cell.itertext()))
    
    Yaml_helpers().write(_dct_stations, dct_cfg['grab_irceline']['Local_path']['stations'])
    
    _dct_values = {'irceline_values':[]}
    _lst_el_table_row_datas = el_page.xpath(dct_cfg['grab_irceline']['Xpath']['data_row'])
    for _int_row, el_row in enumerate(_lst_el_table_row_datas):
        _lst_cells_number = el_row.xpath('./td')
        if len(_lst_cells_number) > 2: # head region
            _lst_cells_head = el_row.xpath(dct_cfg['grab_irceline']['Xpath']['data_row_label'])
            _dct_values = collections.OrderedDict()
            for _int_cell, _cell_head in enumerate(_lst_cells_head):
                if _int_cell == 0:
                    _dct_values[_dct_stations_label[0]] = ''.join(_cell_head.itertext())
                elif _int_cell == 1:
                    _dct_values[_dct_stations_label[1]] = ''.join(_cell_head.itertext())                    
            _lst_cells_data = el_row.xpath(dct_cfg['grab_irceline']['Xpath']['data_row_value'])
            for _int_cell, _cell_data in enumerate(_lst_cells_data):
                _str_value = ''.join(_cell_data.itertext())
                if _str_value == '&nbsp;':
                    _str_value = ''
                _dct_values[_dct_stations_label[_int_cell+2]] = ''.join(_cell_data.itertext())
            print(_dct_values)
    Yaml_helpers().write(_dct_stations, datetime.datetime.now().strftime('%Y-%m-%dT%H-%M') + '_' +dct_cfg['grab_irceline']['Local_path']['values'])
    
    data_2_js(dct_cfg, _dct_stations, _dct_values)

    
def main():
    global Cfg
    
    _dct_cfg = yaml.load(Cfg)
    _str_url = 'http://' + os.path.join(_dct_cfg['grab_irceline']['Web']['site'], _dct_cfg['grab_irceline']['Web']['path_file_table_fr'])
    
    _el_page = get_el_page(_str_url)
    _str_page = ET.tostring(_el_page)
    #print(_str_page)
    parse_table(_dct_cfg, _el_page)

if __name__ == '__main__':
    """
    """
    _str_prg = sys.argv[0]
    _dtNow_begin = datetime.datetime.now()
    print('Begin %s ' % os.path.split(_str_prg)[1] + _dtNow_begin.strftime('%Y-%m-%d %H:%M:%S'))
    main()
    _dtNow_end = datetime.datetime.now()
    print('End %s ' % os.path.split(_str_prg)[1] + _dtNow_end.strftime('%Y-%m-%d %H:%M:%S'))
    _dt_delta = _dtNow_end-_dtNow_begin
    print('Delta %s' % str(_dt_delta))