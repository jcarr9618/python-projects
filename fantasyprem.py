import json
import requests


def get_basic_info():
    url = 'https://fantasy.premierleague.com/api/element-summary/413/'

    request = requests.get(url)
    json = request.json()


print (json)


# Opening JSON file
with open ('C:\Users\jcarr\Desktop\PythonProjects\ma.json') as f:
    data = json.load(f)

# Output here
print (data)





