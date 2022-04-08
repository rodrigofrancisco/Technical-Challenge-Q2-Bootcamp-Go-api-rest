# Technical-Challenge-Q2-Bootcamp-Go-api-rest

```shell
Author: Rodrigo Francisco
Date: April, 2022

```

## Techology stack

* **Python 3.8**
* **FastAPI 0.75.1**: Its a web frameworking for building APIs in a fast way. It provides a built-in swagger to test the endpoints
* **Pipenv**: Similar to npm package manager, it manages library dependencies

## Dependency

Since I'm using a third party application, my service is couple with https://jsonplaceholder.typicode.com/todos

## Installation

```shell
pipenv install
pipenv shell

uvicorn main:app --reload
```

## Endpoints

You can go to `http://127.0.0.1:8000/docs` to see all the information of the endpoints.

We have just two endpoints

* http://127.0.0.1:8000/ : The root, this displays the hello world message
* http://127.0.0.1:8000/todos : Displays 200 todo items
* http://127.0.0.1:8000/todos/:id : Display a todo given and item id represented by `:id`
