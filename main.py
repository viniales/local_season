from fastapi import FastAPI
import models
from database import engine
from routers import player, user

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(player.router)
app.include_router(user.router)
