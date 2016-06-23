# -*- coding: utf-8 -*-
import config
import requests
degree_sign= u'\N{DEGREE SIGN}'
weather_key = config.weather_key

# api key  - latitude, longitude, time (epoch)
#without time parameter
# new york longitude and latitude
response = requests.get('https://api.forecast.io/forecast/' + weather_key + '/40.7144,-74.006')
#on my birthdate - time parameter
#response = requests.get('https://api.forecast.io/forecast/' + weather_key + '/39.0068,76.7791,765407717')
data = response.json()
# print(data)



max_temp = data['daily']['data'][0]['temperatureMax']

def TEMPERATURE():
 # is the current temperature
 return str(data['currently']['temperature'])

def SUMMARY():

# is what it currently looks like (partly cloudy, etc - it's "summary" in the dictionary). Lowercase, please.
    return str(data['currently']['summary'].lower())

def TEMP_FEELING():
    #is whether it will be hot, warm, cold, or moderate.
    if max_temp > 90:
        return "hot"
    elif 90 > max_temp > 70:
        return "moderate"
    else:
        return "cool"



def HIGH_TEMP():
#is the high temperature for the day.
    return str(max_temp)

def LOW_TEMP():
#is the low temperature for the day.
    return str(data['daily']['data'][0]['temperatureMin'])

def RAIN_WARNING():
    return("%.0f%%" % (100 * (data['daily']['data'][0]['precipProbability'])/1) + " chance of rain")
#is something like "bring your umbrella!" if it is going to rain at some point during the day.
    #return str(data['daily']['data'][0]['precipProbability']) + "% chance of rain."



# the current date's weath
TEMP_FEELING()
#TEMPERATURE()


print("Right now it is " + TEMPERATURE() +  degree_sign +  "  out and " + \
 SUMMARY() + ". Today will be " + TEMP_FEELING() + \
" with a high of " + HIGH_TEMP() +  degree_sign + \
" and a low of " + LOW_TEMP() +  degree_sign + ". There is a " + RAIN_WARNING() )


import config
import requests
import time
today = time.strftime("%B %e, %Y")


key = config.mailgun_key
def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/aboutmonica.com/messages",
        auth=("api", key),
        data={"from": "Daily Weather Report <weather@aboutmonica.com>",
              "to": "Monica <mmp2181@columbia.edu>",
              "subject": "8AM Weather Forecast: " + today,
              "text": "Right now it is " + TEMPERATURE() +  degree_sign + " out and " + \
               SUMMARY() + ". Today will be " + TEMP_FEELING() + \
              " with a high of " + HIGH_TEMP() + degree_sign + \
              " and a low of " + LOW_TEMP() + degree_sign + ". There is a " + RAIN_WARNING()})


send_simple_message()
