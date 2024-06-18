from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

handler = Mangum(app)


@app.get("/")
async def hello():
    return {"message": "IDE (FastaApi app) -> GitHub (with Github Action) -> S3 -> Lambda - CI/CD test"}


@app.get("/fastapi")
async def hello():
    return {"message":" FastAPI route root"}


@app.get("/fastapi/1")
async def hello():
    return {"message":" FastAPI route 1"}
