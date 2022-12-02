from fastapi import FastAPI

import redis

app = FastAPI()
r = redis.Redis(host="redis", port=6379)

user_status = {
    "1":"offline",
    "2":"offline",
    "3":"offline"
    }

@app.get("/users")
async def get_users():
    users_list = r.keys()
    for uid in user_status.keys():
        user_status[uid] = "offline" if r.get(uid) == None else r.get(uid)
    return user_status


@app.get("/users/{user_id}")
async def get_user(user_id):
    if user_id not in user_status.keys():
        return "User not found. Valid ids {1, 2, 3}"
    return "online" if r.get(user_id) else "offline"


@app.post("/users/{user_id}")
async def user_status_handler(user_id):
    if user_id not in user_status.keys():
        return "User not found. Valid ids {1, 2, 3}"
    r.set(str(user_id), "online", 10)
    return "success"
