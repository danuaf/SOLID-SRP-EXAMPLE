from controller.modbus_controller import ModbusController
from controller.WeatherStation_controller import WeatherStationController

if __name__ == "__main__":
    WeatherStationDevices = {
        "Weather_Station": {
            "Solar_Radiation": {"fieldName": 'solarRadiation', "metric": False, "unit": 'W/m²'},
            "UV_Index": {"fieldName": 'uv', "metric": False},
            "Wind_Direction": {"fieldName": 'winddir', "metric": False, "unit": '°'},
            "Humidity": {"fieldName": 'humidity', "metric": False, "unit": '%'},
            "Dew_Point": {"fieldName": 'dewpt', "metric": True, "unit": '°C'},
            "Elevation": {"fieldName": 'elev', "metric": True, "unit": 'Meter'},
            "Heat_Index": {"fieldName": 'heatIndex', "metric": True, "unit": '°C'},
            "Precipitation_Rate": {"fieldName": 'precipRate', "metric": True, "unit": 'mm/h'},
            "Precipitation_Total": {"fieldName": 'precipTotal', "metric": True, "unit": 'mm'},
            "Pressure": {"fieldName": 'pressure', "metric": True, "unit": 'hPa'},
            "Temperature": {"fieldName": 'temp', "metric": True, "unit": '°C'},
            "Wind_Chill": {"fieldName": 'windChill', "metric": True, "unit": '°C'},
            "Wind_Gust": {"fieldName": 'windGust', "metric": True, "unit": 'km/h'},
            "Wind_Speed": {"fieldName": 'windSpeed', "metric": True, "unit": 'km/h'}
        }
    }

    ModBusDevices = {
        "Pyranometer": {
            "slave_address": 12,
            "registers": {
                "UV_Radiation": {"address": 2, "decimals": 1}
            }
        },
        "RTD": {
            "slave_address": 11, "registers": {
                "Temperature": {"address": 0, "decimals": 1}
            }
        },
        "Dissolve_Oxygen": {
            "slave_address": 2, "registers": {
                "Dissolve_Oxygen": {"address": 0, "decimals": 0}
            }
        },
        "Inventer_SRNE": {
            "slave_address": 1, "registers": {
                "Load_Active_Power": {"address": 539, "decimals": 0},
                "Battery_Level": {"address": 256, "decimals": 0},
                "Battery_Voltage": {"address": 257, "decimals": 1},
                "PV_Voltage": {"address": 263, "decimals": 1},
                "PV_Current": {"address": 264, "decimals": 1},
                "PV_Power": {"address": 265, "decimals": 0},
                "Charge_Power": {"address": 270, "decimals": 0},
                "Battery_Charge_State": {"address": 267, "decimals": 0},
                "Machine_State": {"address": 528, "decimals": 0},
                "Inverter_Current": {"address": 537, "decimals": 1},
                "Main_Charge_Current": {"address": 542, "decimals": 1},
                "PV_Change_Current": {"address": 548, "decimals": 1},
                "PV_Daily_Consumption": {"address": 61487, "decimals": 1},
                "Battery_Charge_Daily": {"address": 61485, "decimals": 1},
                "Battery_Discharge_Daily": {"address": 61486, "decimals": 1},
                "Load_Daily_Consumption": {"address": 61485, "decimals": 1},
                "Uptime": {"address": 61485, "decimals": 0},
                "PV_Generated": {"address": 61496, "decimals": 1},
                "Main_Load_Power_Daily": {"address": 61501, "decimals": 1},
                "DCDC_Temperature": {"address": 544, "decimals": 1},
                "DCAC_Temperature": {"address": 545, "decimals": 1},
                "Translator_Temperature": {"address": 546, "decimals": 1},
                "Load_Percentage": {"address": 543, "decimals": 0}
            }
        },
        "VFD_NFlixin": {
            "slave_address": 9, "registers": {
                "Running_Frequency": {"address": 28672, "decimals": 2},
                "Output_Voltage": {"address": 28675, "decimals": 0},
                "Output_Current": {"address": 28676, "decimals": 2}
            }
        }
    }

    db_path = "database/testing.db" 
    modBusCom = 'COM8'
    api_key = 'ini rahasia'
    station_id = 'ini rahasia'

    ws_controller = WeatherStationController(api_key, station_id, db_path, WeatherStationDevices)
    modbus_controller = ModbusController(modBusCom,db_path,ModBusDevices,1)

    while True :
        modbus_controller.readAndStoreData()
        ws_controller.readAndStoreData()