#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 17 oct. 2014

@author: patrick
'''

'''
Created on 18 oct. 2014

@author: patrick
'''
import sys
import os
import datetime
import codecs
import yaml

# http://all-geo.org/volcan01010/2012/11/change-coordinates-with-pyproj/
#import mpl_toolkits.basemap.pyproj as pyproj # Import the pyproj module
import pyproj
 
import yaml_orderedDict

Dct_station_ibge = '''
Ibge_stations:
    - station_ibge_id: R001
      place_fr: Molenbeek - Ecluse
      place_nl: Molenbeek - Sluis
      geo_epsg-31370: 151119,168300

    - station_ibge_id: R002
      place_fr: Ixelles - Av. de la Couronne
      place_nl: Elsene - Kroonlaan
      geo_epsg-31370: 151119,168300

    - station_ibge_id: B003
      place_fr: Bruxelles - Arts-Loi
      place_nl: Brussel - Kunst-Wet
      geo_epsg-31370: 149994,170593

    - station_ibge_id: B011
      place_fr: Berchem - Drève des Maricolles
      place_nl: Berchem - Maricollendreef
      geo_epsg-31370: 144338,171963

    - station_ibge_id: R012
      place_fr: Uccle - site IRM
      place_nl: Ukkel - site KMI
      geo_epsg-31370: 149280,165130

    - station_ibge_id: N043
      place_fr: Bruxelles Avant Port (Haren)
      place_nl: Brussel Voorhaven (Haren)
      geo_epsg-31370: 151000,174800

    - station_ibge_id: WOL1
      place_fr: Woluwe-St-Lambert - Gulledelle (IBGE)
      place_nl: St.-Lambr.-Woluwe - Gulledelle (BIM)
      geo_epsg-31370: 154010,171872

    - station_ibge_id: MEU1
      place_fr: Bruxelles (N.O.H.) - Parc Meudon
      place_nl: Brussel (N.O.H) - Meudonpark
      geo_epsg-31370: 151686,176084

    - station_ibge_id: IHE03
      place_fr: Ixelles - Av. de la Couronne
      place_nl: Elsene - Kroonlaan
      geo_epsg-31370: 151119,168300

    - station_ibge_id: AND3
      place_fr: Anderlecht - Blv. De l&#39;Humanité
      place_nl: Anderlecht - Humaniteitslaan
      geo_epsg-31370: 145969,167729

    - station_ibge_id: B008
      place_fr: Belliard - Remard
      place_nl: Belliard - Remard
      geo_epsg-31370: 150521,170042

    - station_ibge_id: B006
      place_fr: Parlement européen &quot;Spinelli&quot;
      place_nl: Europees Parlement &quot;Spinelli&quot;
      geo_epsg-31370: 150397,169802

    - station_ibge_id: B004
      place_fr: Bruxelles - métro Ste Catherine
      place_nl: Brussel - metrostation St.-Katelijne
      geo_epsg-31370: 148580,171157

    - station_ibge_id: E013
      place_fr: Forest (club de tennis)
      place_nl: Vorst (tennisclub)
      geo_epsg-31370: 147118,166670

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

def get_stations():
    # Define some common projections using EPSG codes
    wgs84=pyproj.Proj("+init=EPSG:4326") # LatLon with WGS84 datum used by GPS units and Google Earth
    lamb72=pyproj.Proj("+init=EPSG:31370") # coordinaite used bu the Belgium IBGE 


    _lst_stations = yaml.load(Dct_station_ibge)
    for _station in _lst_stations['Ibge_stations']:
        _x, _y = _station['geo_epsg-31370'].split(',')
        _lat, _long = pyproj.transform(lamb72, wgs84, _x, _y)
        _station['geo_epsg-wsg84'] = ' %(long)f, %(lat)f' % {'lat':_lat, 'long': _long}
        
    return _lst_stations

def main():
    # Define some common projections using EPSG codes
    wgs84=pyproj.Proj("+init=EPSG:4326") # LatLon with WGS84 datum used by GPS units and Google Earth
    lamb72=pyproj.Proj("+init=EPSG:31370") # coordinaite used bu the Belgium IBGE 


    _lst_stations = yaml.load(Dct_station_ibge)
    for _station in _lst_stations['Ibge_stations']:
        _x, _y = _station['geo_epsg-31370'].split(',')
        _lat, _long = pyproj.transform(lamb72, wgs84, _x, _y)
        print(_lat, _long)
        _station['geo_epsg-wsg84'] = '%(lat)f, %(long)f' % {'lat':_lat, 'long': _long}
    #print(_lst_stations)
    Yaml_helpers().write(_lst_stations, 'ibge_wsg84.yaml')
        
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
