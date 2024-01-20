from fastapi import APIRouter
from pydantic import BaseModel, Field
import constants
from storage import storage


router = APIRouter(
    prefix="/api/data_cars",
    tags=['API', 'Data_cars']


)


class UserCarData(BaseModel):
    name: str = Field(min_length=2)
    telephone_number: int
    model: str
    producer: str
    year_created: int = Field(gt=2010)
    price: float = Field(default=0.0, gt=0.0)
    tags: list[constants.TypeCar] = Field(default=[], max_items=2)


class SavedData(UserCarData):
    uuid: str


@router.post('/add')
def add_car_data(data: UserCarData) -> UserCarData:
    data.name.upper().strip()
    storage.add_car_data(data.model_dump())
    return data


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
