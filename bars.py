# -*- coding: utf-8 -*-
import json
import codecs
import chardet
import math


def load_data(filepath):
    # Проверяем кодировку файла, если она не 'utf-8' - перекодируем файл
    char_type = chardet.detect(open(filepath, "rb").read())['encoding']
    if char_type != 'utf-8':
        with codecs.open(filepath, 'rb', encoding=char_type) as f, codecs.open("new.json", 'wb',encoding='utf-8') as g:
            for i in f:
                print(i, file=g)
    with open('new.json', 'r', encoding='utf-8') as fh:  # открываем файл на чтение
        data = json.load(fh)
    return data


def get_biggest_bar(data):
    max_seats_counts = 0
    num_bar = 0
    for i in range(0,len(data)):
        if data[i]['SeatsCount'] > max_seats_counts:
            max_seats_counts = data[i]['SeatsCount']
            num_bar = i
    return data[num_bar]


def get_smallest_bar(data):
    min_seats_counts = 1000
    num_bar = 0
    for i in range(0,len(data)):
        if 0 < int(data[i]['SeatsCount']) < min_seats_counts:
            min_seats_counts = data[i]['SeatsCount']
            num_bar = i
    return data[num_bar]


def get_closest_bar(data, longitude, latitude):
    mx = 0
    my = 0
    min_dist = 1000.
    num_bar = 0
    for i in range(0,len(data)):
        mx = abs(latitude - float(data[i]['Latitude_WGS84']))
        my = abs(longitude - float(data[i]['Longitude_WGS84']))
        dist = math.sqrt(mx**2 + my**2)
        if dist < min_dist:
            min_dist = dist
            num_bar = i
    return num_bar, data[num_bar]


if __name__ == '__main__':
    data = load_data('data.json')
    print(get_biggest_bar(data))
    print(get_smallest_bar(data))
    print(get_closest_bar(data, 37.618762, 55.625307))
