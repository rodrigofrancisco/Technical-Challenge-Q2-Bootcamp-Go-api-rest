from fastapi import FastAPI
import requests

app = FastAPI()
baseUrl = "https://jsonplaceholder.typicode.com/todos"

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/todos")
def read_item():
    response = requests.get(baseUrl)
    return {"todos": response.json()}

@app.get("/todos/{todo_item}")
def read_item(todo_item: int):
    url = baseUrl + "/" + str(todo_item)
    response = requests.get(url)
    return {"todos": response.json()}