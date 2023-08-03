from fastapi import FastAPI
import models
from database import engine
from routers import player, user, authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(player.router)
app.include_router(user.router)
app.include_router(authentication.router)