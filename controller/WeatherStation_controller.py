import requests
from .db_controller import DbController
from time import sleep

class WeatherStationController:
    def __init__(self, apiKey, stationId, dbPath, deviceInfo):
        self.url = f'https://api.weather.com/v2/pws/observations/current?stationId={stationId}&format=json&units=m&apiKey={apiKey}'
        self.deviceData = deviceInfo
        self.db_controller = DbController(dbPath)

        for device_name, device_info in deviceInfo.items():
            data_names = list(device_info.keys())
            self.db_controller.create_table(device_name, data_names)


    def readAndStoreData(self):
        for device_name, device_info in self.deviceData.items():
            data_to_insert = {}

            for field_name, field_info in device_info.items():
                try:
                    response = requests.get(self.url)
                    data = response.json()
                    observation = data['observations'][0]
                    
                    if field_info.get('metric', False) :
                        data_to_insert[field_name] = observation['metric'][field_info["fieldName"]]
                    else:
                        data_to_insert[field_name] = observation[field_info["fieldName"]]

                except requests.exceptions.RequestException as e:
                    print(f'Error: {e}')

            print(f"Data to Insert : {data_to_insert}")
            if data_to_insert:
                self.db_controller.insert_data(device_name, data_to_insert)

        
