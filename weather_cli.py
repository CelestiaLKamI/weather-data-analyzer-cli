import os
import json
import sys


def load_data(weather_data):
    with open(weather_data, 'r') as file:
        data = json.load(file)

    return data


def calculate_avg_temp(data):
    cities = {}
    for each in data:
        city = each["city"]
        temperature = each["temperature"]
        
        if city not in cities:
            cities[city] = []
        
            cities[city].append(temperature)


    avg_temp = {} 

    for city, temps in cities.items():
            
            average_temp = sum(temps) / len(temps)
            avg_temp[city] = average_temp

    return avg_temp