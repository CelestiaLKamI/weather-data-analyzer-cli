import os
import json
import sys


def load_data(weather_data):
    with open(weather_data, 'r') as file:
        data = json.load(file)

    return data


def calculate_avg_temp(temp_list):
    cities = {}
    for each in temp_list:
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

def convert_temp(avg_temp, convert = None):

    for city in avg_temp:
            avg_temp[city] = (avg_temp[city] * 9/5) + 32

    for city, temp in avg_temp.items():

        if convert:
            temp = convert_temp(temp)
            unit = 'F'
        else:
            unit = 'C'
        return f"{city}: {temp} degree {unit}"


def main():
    if len(sys.argv) != 2:
        print("Usage: python weather_cli.py [--city CITY] [--convert F] [--list]")
        sys.exit(1)

    file_path = "./weather_data.json"
    action = sys.argv[1]

    if action not in ["--city", "--convert", "--list", "--help"]:
        print("ERROR: Please specify one action")
        print("--city", "--convert", "--list", "--help")
        sys.exit(1)

    if action == "--city":
        print("Please Specify the city: ")
        city = sys.argv[2]
    
    elif action == "--convert":
        print




