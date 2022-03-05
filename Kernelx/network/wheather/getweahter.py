
# Python program to find current
# weather details of any city
# using openweather api

# open required modules
import requests, json

# Enter your API key here
api_key = "517944f3bd339b457cedcab7b7fa10c1"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name
city_name = input('Enter city name : ')

# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

# get method of requests module
# return response object
response = requests.get(complete_url)

# json method of response object
# convert json format data info
# python format data
print('eto response')
print(response)
x = response.json()
print('eto x')
print(x)

# Now x contains list of nested dictionaries
# Check the value of "cod key is equal to
# "404", means city found otherwise,
# city is not found
if x["cod"] != "404":
    # store the value of "main"
    # key in variable y
    y = x["main"]

    # store the value corresponding
    # to the "temp" key of y
    current_temperature = y["temp"]
    current_temperature = current_temperature - 273

    # store the value corresponding
    # to the "pressure" key of y
    current_pressure = y["pressure"]

    # store the value corresponding
    # to the "humidity" key pf y
    current_humidity = y["humidity"]

    # store the value of "weather"
    # key in variable z
    z = x["weather"]

    # store the value corresponding
    # to the "description" key at
    # the 0th index of z
    weather_description = z[0]["description"]

    # print following values
    print(" Temperature (in kelvin unit) = " +
          str(current_temperature) +
          "\n atmospheric pressure (in hPa unit) = " +
          str(current_pressure) +
          "\n humidity (in percentsge) = " +
          str(current_humidity) +
          "\n description = " +
          str(weather_description))
else:
    print("City Not Found")








