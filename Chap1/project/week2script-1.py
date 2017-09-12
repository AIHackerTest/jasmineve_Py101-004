# -*- coding: utf-8 -*-

# First import three modules we are gonna use in this exercise
import requests
import json
import datetime


def weather_lookup(city):
    server_response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&APPID=e72cd327cedf7504346372ce30d4c47f&units＝metric')
    response = server_response.json()
    a = 'The weather condition in ' + city + ' now is ' + response['weather'][0]['description']+ '.'
    print(a)
    print('This is updated on', datetime.datetime.fromtimestamp(int(response['dt'])).strftime('%Y-%m-%d %H:%M:%S'))
    global history
    history = history.append(a)


# parameters: APPID = APIKey; q = cityname; mode = xml/html; units =metric/imperial
# ask for user input



# we get the server_response, then convert to json style and print it out



# print(datetime.datetime.fromtimestamp(int(response['dt'])).strftime('%Y-%m-%d %H:%M:%S'))


history = []
while True:
    w = input("Please type in the name of your city or the commands: ")
    if w == 'help':
        print(
'''输入城市名，查询该城市的天气；
输入 help，获取帮助文档；
输入 history，获取查询历史；
输入 quit，退出天气查询系统。'''
        )
    elif w == 'quit':
        break
    elif w == 'history':
        print(history)
    else:
        server_response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + w + '&APPID=e72cd327cedf7504346372ce30d4c47f&units＝metric')
        response = server_response.json()
        a = 'The weather condition in ' + w + ' now is ' + response['weather'][0]['description']+ '.'
        print(a)
        print('This is updated on', datetime.datetime.fromtimestamp(int(response['dt'])).strftime('%Y-%m-%d %H:%M:%S'))
        history.append(a)


quit()
