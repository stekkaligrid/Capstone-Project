from fastapi import FastAPI
from app.db import Base,engine
from app.routes import router
from app.models import User

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)

@app.get("/")
def root():
    return{ "message":"App is working" }
