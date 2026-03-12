from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def default_path():
    return "Hello World! Welcome to FastAPI"

@app.get("/hello/{name}/{address}/{contact}")
def hello(name: str, address: str, contact: str):
    return f"Hello {name} Ji. Welcome to FastAPI from {address}. Your contact is {contact}"