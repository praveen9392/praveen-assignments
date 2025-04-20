
# fastapi
# Question-18:
# convert helloj of flask to fastapi

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class Hello(BaseModel):
    name: str = "praveen"
    format: str = "json"

@app.get("/helloj")
async def helloj_get(hello:Hello):
    return {"name": hello.name, "format": hello.format}

@app.post("/helloj")
async def helloj_post(body: Hello):
    return {"name": body.name, "format": body.format}

@app.get("/helloj/{name}/{format}")
async def helloj_get_path(name: str, format: str):
    return {"name": name, "format": format}
