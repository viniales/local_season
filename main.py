from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return 'ok'

@app.get('/blog/{id}')
def show_id(id):
    return f"Your id: {id}"