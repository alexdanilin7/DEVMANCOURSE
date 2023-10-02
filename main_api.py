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

    response = requests.get(url, params=params)
    response.raise_for_status()
    
    print(response.text)
        


def get_weather_for_place():
    places = ['london', 'svo', 'cherepovec']
    for place in places:
        get_weather(place)


if __name__ == '__main__':
    get_weather_for_place()
