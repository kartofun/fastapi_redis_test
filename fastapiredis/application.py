from fastapi import FastAPI, Depends
from .redis import get_db
from pydantic import BaseModel, Field


class User(BaseModel):
    phone: str = Field(default=...,
                       description="Номер телефона в международном формате, начинающийся с '+'")
    address: str = Field(default=..., min_length=1, max_length=200,
                         description="Адрес, не более 200 символов")


app = FastAPI()

CommonsDep = Depends(get_db)


@app.get("/")
def test_start_page():
    return {"result": "hello!"}


@app.get("/check_data")
def check_data(phone: str, db=CommonsDep):
    address = db.get(phone)
    return {"address": address}


@app.post("/write_data")
def write_data(user: User, db=CommonsDep):
    db.set(user.phone, user.address)
    return {"result": "ok"}
