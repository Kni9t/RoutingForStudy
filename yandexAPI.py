import requests

import jsonController

class YAAPI:
    def __init__(self):
        self.key = jsonController.Load('params/key.json')['key']
        
    def saveAllStationList(self, fileName, state, reg, city):
        url = f'https://api.rasp.yandex.net/v3.0/stations_list/?apikey={self.key}&lang=ru_RU&format=json'
        
        stationList = []
        
        for country in requests.get(url).json()["countries"]:
            if (country['title'] == state):
                for region in country['regions']:
                    if(region['title'] == reg):
                        for settle in region['settlements']:
                            if (settle['title'] == city):
                                for station in settle['stations']:
                                    if (station['station_type'] == 'bus_stop') and (station['longitude'] != '') and (station['latitude'] != ''):
                                        bufData = {
                                            'title': station['title'],
                                            'longitude': float(station['longitude']),
                                            'latitude': float(station['latitude']),
                                            'transport_type': station['transport_type'],
                                            'yandex_code': station['codes']['yandex_code']
                                            }
                                        stationList.append(bufData)
        
        jsonController.Save(fileName, stationList)