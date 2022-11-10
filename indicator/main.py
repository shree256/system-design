from fastapi import FastAPI

import redis

app = FastAPI()
r = redis.Redis(host="redis", port=6379)


@app.get("/users")
async def get_users():
    users_list = r.keys()
    user_status = [(k, r.get(k)) for k in users_list]
    return user_status


@app.get("/users/{user_id}")
async def get_user(user_id):
    return "online" if r.get(user_id) else "offline"


@app.post("/users/{user_id}")
async def user_status_handler(user_id):
    r.set(str(user_id), "online", 10)
    return "success"
