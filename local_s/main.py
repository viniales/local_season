from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()




@app.get('/')
def create():
    return 'ok'
