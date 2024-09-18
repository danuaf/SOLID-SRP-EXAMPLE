from minimalmodbus import Instrument
from .db_controller import DbController
from time import sleep
import random # untuk testing pengganti nilai sensor

class ModbusController:
    def __init__(self, com, dbPath, deviceInfo, slave_address=1 ):
        self.com = com
        self.slave_address = slave_address
        self.instrument = Instrument(self.com, self.slave_address)
        self.instrument.serial.baudrate = 9600
        self.instrument.serial.bytesize = 8
        self.instrument.serial.stopbits = 1
        self.instrument.serial.timeout = 1

        self.db_controller = DbController(dbPath)
        self.deviceData = deviceInfo
        self.db_path = dbPath

        # Buat Table Perangakt dan Parameter di SQLite
        for device_name, device_info in self.deviceData.items():
            register_names = list(device_info["registers"].keys())
            self.db_controller.create_table(device_name, register_names)

    def read_register(self, address, decimals=0):
        try:
            value = self.instrument.read_register(address, decimals)
            return value
        except Exception as e:
            print(f"Error reading register {address}: {e}")
            return None
        
    def readAndStoreData(self):
        # Baca dan Kirim data ke SQLite
        for device_name, device_info in self.deviceData.items():
            data_to_insert = {}

            for register_name, register_info in device_info["registers"].items():
                address = register_info["address"]
                decimals = register_info["decimals"]
                slave = device_info["slave_address"]
        
                # register_value = random.randint(1,100) # Untuk testing pengganti nilai sensor
                register_value = ModbusController(self.com,self.db_path,self.deviceData,slave).read_register(address, decimals)
                sleep(0.2)

                if register_value is not None:
                    data_to_insert[register_name] = register_value
            print(f"Data to Insert : {data_to_insert}")

            if data_to_insert:
                self.db_controller.insert_data(device_name, data_to_insert)

        