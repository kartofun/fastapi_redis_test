import redis


# Функция с подключением к redis, чтобы потом в Depends засунуть
def get_db():
    return redis.Redis(host="redis", port=6379, db=0, password='password', decode_responses=True)
