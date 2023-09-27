import requests


def get_weather(place):
    url = f'https://wttr.in/{place}?nTqu&lang=en'
    url_new = f'http://wttr.dvmn.org/{place}?nTqu&lang=en'

    response = requests.get(url)
    if response.status_code == 200:
        print(response.text)
    else:
        response = requests.get(url_new)
        print(response.text)

def get_for_place():
    places = ['london', 'svo', 'cherepovec']
    for place in places:
        get_weather(place)

if __name__ == '__main__':
    get_for_place()

