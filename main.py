from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

app = FastAPI()
app.mount("/temp", StaticFiles(directory="temp", html=True), name="temp")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):

    with open(f"temp/welcomed.txt", "at+") as file:
        file.write(f"{name}\n")
    return {"message": f"Hello {name}"}
