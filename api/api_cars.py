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
    price: float = Field(default=0.0, gt=0.0)
    tags: list[constants.TypeCar] = Field(default=[], max_items=2)


class SavedData(UserCarData):
    uuid: str = Field(examples=['2b49c188-e592-421d-a4b5-a9884854384a'])


@router.post('/add', status_code=status.HTTP_201_CREATED)
def add_car_data(data: UserCarData) -> SavedData:
    saved_data = storage.add_car_data(data.model_dump())
    return saved_data


@router.get('/')
def get_car_by_country() -> list[dict]:
    return [{'car': "mercedes"}]


@router.get('/')
def data_cars() -> list[dict]:
    return [{'car': "mercedes"}]


@router.put('/update/{car_id}')
def update_data_car():
    pass


@router.delete('/remove/{car_id}')
def remove_car():
    pass
