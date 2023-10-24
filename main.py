from fastapi import FastAPI
from routers import user, auth, match_betting, loading_matches, calculate_score
import models
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(match_betting.router)
app.include_router(loading_matches.router)
app.include_router(calculate_score.router)