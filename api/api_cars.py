from fastapi import APIRouter, status
from pydantic import BaseModel, Field
import constants
from storage import storage


router = APIRouter(
    prefix="/api/data_cars",
    tags=['API', 'Data_cars']


)


class UserCarData(BaseModel):
    name: str = Field(min_length=2)
    gmail: str = Field(examples=['patiw20557@wentcity.com'])
    telephone_number: int
    model: str
    producer: str
    year_created: int = Field(gt=2010)
    description: str = Field(min_length=30, max_length=250)
    price: float = Field(default=0.0, gt=0.0)
    tags: list[constants.TypeCar] = Field(default=[], max_items=2)


class SavedData(UserCarData):
    uuid: str = Field(examples=['2b49c188-e592-421d-a4b5-a9884854384a'])


@router.post('/add', status_code=status.HTTP_201_CREATED)
def add_car_data(data: UserCarData) -> SavedData:
    saved_data = storage.add_car_data(data.model_dump())
    return saved_data


@router.get('/')
def get_car_data(skip: int , limit: int = 10, search_params: str = None) -> list[SavedData]:
    cars = storage.get_car_data(skip, limit, search_params)
    result = []
    for car in cars:
        received_data = SavedData(
            **{'name': car['name'], 'gmail': car['gmail'], 'telephone_number': car['telephone_number'], 'model': car['model'],
               'producer': car['producer'], 'year_created': car['year_created'], 'description': car['description'], 'price': car['price'],
               'tags': car['tags'], 'uuid': car['uuid']})
        result.append(received_data)
    return result


@router.get('/price')
def get_data_cars_by_price(skip: int, limit: int, search_price: float) -> list[SavedData]:
    cars = storage.get_cars_by_price(skip, limit, search_price)
    result = []
    for car in cars:
        received_data = SavedData(
            **{'name': car['name'], 'gmail': car['gmail'], 'telephone_number': car['telephone_number'], 'model': car['model'],
               'producer': car['producer'], 'year_created': car['year_created'], 'description': car['description'], 'price': car['price'],
               'tags': car['tags'], 'uuid': car['uuid']})
        result.append(received_data)
    return result



@router.patch('/update/{car_id}')
def update_data_car(car_id: str, price: float):
    storage.update_data_car(car_id, price)
    return {'result': 'Successful!'}


@router.delete('/remove/{car_id}')
def remove_car(car_id: str):
    storage.remove_car_data(car_id)
    return {'result': 'Deleted'}
