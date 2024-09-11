from fastapi import FastAPI, Depends
from .redis import get_db


app = FastAPI()

# Определяем общие зависимости, так чуть меньше кода выходит
CommonsDep = Depends(get_db)


# Выносить эндпоинты в отдельный файл не стал, так как сервис очень простой (best KISS)
@app.get("/")
def test_start_page():
    return {"result": "hello!"}


@app.get("/check_data")
def check_data(phone: int, db=CommonsDep):
    address = db.get(phone)
    return {"address": address}


@app.post("/write_data")
def write_data(address: str, phone: int, db=CommonsDep):
    db.set(phone, address)
    return {"address": address, "phone": phone}
