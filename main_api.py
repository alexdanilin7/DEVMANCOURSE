import requests


def get_weather(place):
  
    params = {
        "n":"",
        "T":"",
        "q":"",
        "lang":"ru",
        "M":""
    }
    url = f'https://wttr.in/{place}'
    url_new = f'http://wttr.dvmn.org/{place}'
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
    except requests.HTTPError as e:
        response = requests.get(url_new, params=params)
        response.raise_for_status()
    
    print(response.text)
        


def get_weather_for_place():
    places = ['london', 'svo', 'cherepovec']
    for place in places:
        get_weather(place)


if __name__ == '__main__':
    get_weather_for_place()
