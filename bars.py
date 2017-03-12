# -*- coding: utf-8 -*-
"""
The module is designed to work with a resource https://data.mos.ru/opendata/7710881420-bary.
The module allows you to find the smallest bar using the function get_biggest_bar(data),
the largest bar, using the function get_biggest_bar(data)
and the nearest bar using coordinates, using the function get_closest_bar(data, longitude, latitude).
To work the module you need a file ".json" that you need to download from https://data.mos.ru/opendata/7710881420-bary.
Use the function load_data(filepath) to load data.
"""
import json
import codecs
import os
import chardet
import math


def load_data(filepath):
    """
    Function is designed to process the downloaded file into a format json
    :param filepath: Path to file on your computer
    :return: json-object
    """
    if os.path.exists(filepath):
        char_type = chardet.detect(open(filepath, "rb").read())['encoding']
        with codecs.open(filepath, 'rb', encoding=char_type) as f, codecs.open("new.json", 'wb',encoding='utf-8') as g:
            for i in f:
                print(i, file=g)
        with open('new.json', 'r', encoding='utf-8') as fh:
            return json.load(fh)


def get_biggest_bar(data):
    """
    The function finds the biggest bar. The number of seats is considered
    :param data: json-object with bars
    :return: Message with the name of the bar and address
    """
    max_seats_counts = 0
    num_bar = 0
    for bar_id, bar in enumerate(data):
        if bar['SeatsCount'] > max_seats_counts:
            max_seats_counts = bar['SeatsCount']
            num_bar = bar_id
    return 'Самый большой бар - ' + data[num_bar]['Name'] + ', по адресу ' + data[num_bar]['Address']


def get_smallest_bar(data):
    """
    The function finds the smallest bar. The number of seats is considered
    :param data: json-object with bars
    :return: Message with the name of the bar and address
    """
    min_seats_counts = 1000
    num_bar = 0
    for bar_id, bar in enumerate(data):
        if 0 < bar['SeatsCount'] < min_seats_counts:
            min_seats_counts = bar['SeatsCount']
            num_bar = bar_id
    return 'Самый маленький бар - ' + data[num_bar]['Name'] + ', по адресу ' + data[num_bar]['Address']


def get_closest_bar(data, longitude, latitude):
    """
    The function finds the nearest bar at the current coordinates
    :param data: json-object with bars
    :param longitude: current longitude coordinates
    :param latitude: current latitude coordinates
    :return: Message with the name of the bar and address
    """
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
    return 'Ближайший бар - ' + data[num_bar]['Name'] + ', по адресу ' + data[num_bar]['Address']


if __name__ == '__main__':
    data_bars = load_data('data.json')
    print(get_biggest_bar(data_bars))
    print(get_smallest_bar(data_bars))
    print(get_closest_bar(data_bars, 37.618762, 55.625307))
