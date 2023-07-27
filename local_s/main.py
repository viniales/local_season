from fastapi import FastAPI

app = FastAPI()

@app.post('/system')
def create():
    return 'creating'