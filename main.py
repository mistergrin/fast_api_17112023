from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root() -> dict:
    return {'try': "ok", "count": 10, "bool": True}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True, host='0.0.0.0', port=8000)