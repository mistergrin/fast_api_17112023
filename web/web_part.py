from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from storage import storage

templates = Jinja2Templates(directory='templates')


router = APIRouter(
    prefix='',
    tags=['WEB', ],
)


@router.get('/')
def index(request: Request):
    cars = storage.get_data_cars(0, limit=5)
    context = {
        'request': request,
        'page': 'page 1',
        'title': 'first page',
        'cars': cars

    }
    return templates.TemplateResponse('index.html', context=context)

@router.get('/second')
def index(request: Request):
    context = {
        'request': request,
        'page': 'page 1',
        'title': 'second page'


    }
    return templates.TemplateResponse('index.html', context=context)

