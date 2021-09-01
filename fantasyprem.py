import json
import requests


def get_basic_info():
    url = 'https://fantasy.premierleague.com/api/element-summary/23/'

    request = requests.get(url)
    json = request.json()


print (json)




