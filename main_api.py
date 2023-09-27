import requests


def get_weather(place):
    try:
        url = f'https://wttr.in/{place}?nTq&lang=ru&M'
        url_new = f'http://wttr.dvmn.org/{place}?nTq&lang=ru&M'

        response = requests.get(url)
        response.raise_for_status()
        if response.status_code == 200:
            print(response.text)
        else:
            response = requests.get(url_new)
            response.raise_for_status()
            print(response.text)
    except Exception as e:
        print(e)


def get_weather_for_place():
    places = ['london', 'svo', 'cherepovec']
    for place in places:
        get_weather(place)


if __name__ == '__main__':
    get_weather_for_place()
