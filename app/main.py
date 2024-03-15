from fastapi import FastAPI
from . import models
from .database import engine, get_db
from . import models
from .routers import post, user, auth

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
async def root():
    return {"Status": "Healthy"}