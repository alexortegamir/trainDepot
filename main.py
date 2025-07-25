from fastapi import FastAPI
from app.api import router

app = FastAPI()
app.include_router(router)

@app.get('/')
def root():
    return {'message': 'Welcome to H0TrainDepot!'}
