import os
import json
import sys


def load_data(weather_data):
    try:
        with open(weather_data, 'r') as file:
            data = json.load(file)

        return data
    except FileNotFoundError:
        print("Error: The file weather_data.jason was not found")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Error: The file is not a valid JSON")
        sys.exit(1)

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

def convert_temp(avg_temp, convert=False):
    converted_temps = {}

    for city, temp in avg_temp.items():
        if convert:
            temp = (temp * 9/5) + 32
            unit = 'F'
        else:
            unit = 'C'
        converted_temps[city] = f"{temp:.2f} degree {unit}"

    return converted_temps



if len(sys.argv) < 2:
    print("Usage: python weather_cli.py [--city CITY] [--convert F] [--list]")
    sys.exit(1)

file_path = "./weather_data.json"
action = sys.argv[1]

if action not in ["--city", "--convert", "--list", "--help"]:
    print("ERROR: Please specify one action")
    print("--city", "--convert", "--list", "--help")
    sys.exit(1)

data = load_data(file_path)
avg_temp = calculate_avg_temp(data)

if action == "--city":
    if len(sys.argv) < 3:
        print("Error: Unknown action specified")
        sys.exit(1)

    print("Please Specify the city: ")
    city = sys.argv[2]

    if city in avg_temp:
        print(f"{city}: {avg_temp[city]:.2f} C")
    else:
        print(f"{city} not found in data")

elif action == "--convert":
    converted_temp = convert_temp(avg_temp, convert = True)
    for city, temp in converted_temp.items():
        print(f"{city}: {temp}")

elif action == "--list":
    print("Cities available in data:")
    for city in avg_temp:
        print(city)

elif action == "--help":
    print("Usage: python weather_cli.py [--city CITY] [--convert] [--list] [--help]")
    print("--city CITY   : Display the average temperature for the specified city.")
    print("--convert     : Convert all temperatures to Fahrenheit.")
    print("--list        : List all cities available in the data.")
    print("--help        : Display this help message.")