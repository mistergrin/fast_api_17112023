from abc import ABC, abstractmethod
import config
import pymongo
from uuid import uuid4


class StorageData:
    @abstractmethod
    def add_car_data(self, data: dict):
        pass

    @abstractmethod
    def get_car_data(self, skip: int = 0, limit: int = 5, search_params: str = None):
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
        self.advertisement = db['data_car']

    def add_car_data(self, data: dict) -> dict:
        data['name'] = str(data['name']).title().strip()
        data['model'] = str(data['model']).title().strip()
        data['uuid'] = str(uuid4())
        self.advertisement.insert_one(data)
        return data

    def get_car_data(self, skip: int = 0, limit: int = 5, search_params: str = None) -> dict:
        query = {}
        if search_params:
            query = {'name': {'$regex': search_params.strip()}}
        return self.advertisement.find(query).skip(skip).limit(limit)

    def get_cars_by_price(self, search_price: float, skip: int = 0, limit: int = 5):
        query = {}
        if search_price:
            query = {'price': {'$eq': search_price}}
        return self.advertisement.find(query).skip(skip).limit(limit)

    def update_data_car(self, data_uuid: str, new_price: float):
        filter_data = {'uuid': data_uuid}
        new_data = {'$set': {'price': new_price}}
        processed = self.advertisement.update_one(filter_data, new_data)
        return processed

    def remove_car_data(self, data_uuid: str):
        filtered_data = {'uuid': data_uuid}
        deleted_data = self.advertisement.delete_one(filtered_data)
        return deleted_data


storage = MongoStorage()
