from fastapi import FastAPI
import models
from database import engine
from routers import user, authentication, match_betting, matches

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(match_betting.router)
app.include_router(matches.router)