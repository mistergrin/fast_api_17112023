from abc import ABC, abstractmethod
import config
import pymongo
from uuid import uuid4


class StorageData:
    @abstractmethod
    def add_car_data(self, data: dict):
        pass

    @abstractmethod
    def get_car_by_country(self):
        pass

    @abstractmethod
    def update_data_car(self):
        pass

    @abstractmethod
    def remove_car(self):
        pass


class MongoStorage:
    def __init__(self):
        url = (
            "mongodb+srv://mistergrin43:{password}@mistergrin43.jxrypgw.mongodb.net/?retryWrites=true&w=majority".format
            (user=config.USER,
             password=config.PASSWORD,
             ))

        client = pymongo.MongoClient(url)
        db = client['User_car_data']
        self.advertisement = db['User_car_data']

    def add_car_data(self, data: dict) -> dict:
        data['uuid'] = str(uuid4())
        self.advertisement.insert_one(data)
        return data

    def update_data_car(self):
        pass

    def remove_car_data(self):
        pass


storage = MongoStorage()
