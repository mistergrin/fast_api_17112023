from fastapi import FastAPI
from api import api_cars

app = FastAPI()
app.include_router(api_cars.router)


@app.get('/')
def root() -> dict:
    return {'try': "ok", "count": 10, "bool": True}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True, host='0.0.0.1', port=8660)