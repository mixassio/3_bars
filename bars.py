
import json
import codecs
import os
import chardet
import math
import sys
import argparse

def create_parser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('filepath')
    parser.add_argument ('-min', '--minimum', action='store_const', const=True)
    parser.add_argument ('-max', '--maximum', action='store_const', const=True)
    parser.add_argument ('-n', '--nearest', nargs=2) 
    return parser
    

def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'rb') as file_json:
            char_type = chardet.detect(file_json.read())['encoding']
        with codecs.open(filepath, 'rb', encoding=char_type) as file_json:
            return json.load(file_json)


def get_biggest_bar(data):
    return max(data, key=lambda x: x['SeatsCount'])


def get_smallest_bar(data):
    return max(data, key=lambda x:x['SeatsCount'])


def get_smallest_bar(data):
    return min(data, key=lambda x:x['SeatsCount'])


def get_closest_bar(data, longitude, latitude):
    mx = 0
    my = 0
    min_dist_to_bar = 1000.
    num_bar = 0
    for bar_id, bar in enumerate(data):
        mx = abs(latitude - float(bar['Latitude_WGS84']))
        my = abs(longitude - float(bar['Longitude_WGS84']))
        distance_to_bar = math.sqrt(mx**2 + my**2)
        if distance_to_bar < min_dist_to_bar:
            min_dist_to_bar = distance_to_bar
            num_bar = bar_id
    return data[num_bar]

def get_closest_bar1(data, longitude, latitude):
    return min(data, key=lambda x: abs(float(x['Longitude_WGS84'])-longitude and abs(float(x['Latitude_WGS84'])-latitude)))


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    data_bars = load_data(namespace.filepath)
    
    if namespace.maximum:
        big_bar = get_biggest_bar(data_bars)
        print('Самый большой бар - {}, по адресу {}'.format(big_bar['Name'], big_bar['Address']))
    if namespace.minimum:
        small_bar = get_smallest_bar(data_bars)
        print('Самый маленький бар - {}, по адресу {}'.format(small_bar['Name'], small_bar['Address']))
    '''if namespace.nearest:
        nearest_bar = get_closest_bar(data_bars, float(namespace.nearest[0]), float(namespace.nearest[0]))
        print('Ближайший бар - {}, по адресу {}'.format(nearest_bar['Name'], nearest_bar['Address']))'''
        
    if namespace.maximum==None and namespace.minimum==None and namespace.nearest==None:
        big_bar = get_biggest_bar(data_bars)
        print('Самый большой бар - {}, по адресу {}'.format(big_bar['Name'], big_bar['Address']))
        small_bar = get_smallest_bar(data_bars)
        print('Самый маленький бар - {}, по адресу {}'.format(small_bar['Name'], small_bar['Address']))
        print('Для поиска ближайшего бара введите координаты')
    if namespace.nearest:
        nearest_bar = get_closest_bar1(data_bars, float(namespace.nearest[0]), float(namespace.nearest[1]))
        print('Ближайший бар - {}, по адресу {}, koord {} {}'
              .format(nearest_bar['Name'], nearest_bar['Address'], nearest_bar['Longitude_WGS84'], nearest_bar['Latitude_WGS84']))
        nearest_bar = get_closest_bar(data_bars, float(namespace.nearest[0]), float(namespace.nearest[1]))
        print('Ближайший бар - {}, по адресу {}, koord {} {}'
              .format(nearest_bar['Name'], nearest_bar['Address'], nearest_bar['Longitude_WGS84'], nearest_bar['Latitude_WGS84']))
        #print(get_closest_bar1(data_bars, float(namespace.nearest[0]), float(namespace.nearest[0])))

