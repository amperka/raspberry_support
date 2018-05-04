# -*- coding: utf-8 -*-
import requests, json
import RPi.GPIO as GPIO
from math import floor

GPIO.setmode(GPIO.BCM)
# Place LED for sun and precipitation in separate lists
precipitationLED = [10, 12, 14, 15, 17, 18, 21, 24, 26]
sunLED = [13, 16, 19]
# Concat two lists (precipitationLED + sunLED) and use single loop to setup pins as OUTPUT
for led in precipitationLED + sunLED:
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, GPIO.LOW)
    # print('init led', led)

url = 'http://api.openweathermap.org/data/2.5/forecast/'
# lat и lon — coordinates
payload = {
    'lat': '55.75',
    'lon': '37.62',
    'units': 'metric',
    'appid': '' # use your OpenWeatherMap key
}

# If API is not present, quit script
if (payload['appid'] == ''):
    print('Error!')
    print('You have to setup API key first!')
    print('Open this file in editor and complete appid field.')
    quit()

maxPrecipitationPerDay = 1.5
# How many LEDs we have to light to display precipitation amount
scalePrecipitation = maxPrecipitationPerDay / len(precipitationLED)

# Select number 25 experimentally to show "non-cloudiness"
scaleSun = 25

res = requests.get(url, params=payload)
data = json.loads(res.text)
forecast = data['list']

# The service openweathermap don't provide daily forecast for free
# Therefore use a hack: summarise forecast data each 3 hours
# Totaly, we have to sum 8 precipitation and take average cloudiness in ['list'] element
precipitation = 0.0
clouds = 0.0
# For each ['list'][0]…['list'][7]
# Sum precipitation and take average cloudiness
for threeHours in range(8):
    weather = forecast[threeHours]
    if ('rain' in weather):
        precipitation = precipitation + weather['rain']['3h']
    if ('snow' in weather):
        precipitation = precipitation + weather['snow']['3h']
    if ('clouds' in weather):
        clouds = clouds + weather['clouds']['all']

# To calculate average divide sum by 8 terms
clouds = clouds / 8
print('Cloudness:', clouds)

print('Precipitation per day:', precipitation)
totalLED = int(floor(precipitation / scalePrecipitation))
# Limit amount of LEDs. Otherwise we'll catch an error
if totalLED > len(precipitationLED):
	totalLED = len(precipitationLED)

for led in range(totalLED):
    GPIO.output(precipitationLED[led], GPIO.HIGH)
    print(precipitationLED[led])

totalLED = int(floor((100 - clouds) / scaleSun))

for led in range(totalLED):
    GPIO.output(sunLED[led], GPIO.HIGH)
    print(sunLED[led])
