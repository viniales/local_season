from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return 'hello'

@app.get('/blog/{id}')
def show_id(id):
    return f"Your id is {id}"