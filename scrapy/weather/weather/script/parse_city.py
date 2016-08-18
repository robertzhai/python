# -*- coding: utf-8 -*-

fh = open("city.txt", "w");

cities = [str(line) for line in open("oil_station.csv", "r")]
print cities
for city in cities:
    city = city.strip('"\n')
    city = city.replace('市', '');
    print city,
    fh.write(city + '\n')

fh.close()