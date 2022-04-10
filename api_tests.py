import requests

baseUrl = "http://127.0.0.1:8000"

def test_hello_world_endpoint_status_code_equals_200():
     response = requests.get(baseUrl)
     assert response.status_code == 200

def test_hello_world_message_display_correctly():
     response = requests.get(baseUrl)
     response_text = response.json()
     assert response_text["message"] == "Hello World"

def test_todos_endpoint_status_code_equals_200():
     response = requests.get(baseUrl + "/todos")
     assert response.status_code == 200     

def test_todos_endpoint_has_more_than_zero_todos():
     response = requests.get(baseUrl + "/todos")
     response_text = response.json()
     assert len(response_text) > 0

def test_todos_endpoint_has_correct_structure():
     response = requests.get(baseUrl + "/todos")
     response_text = response.json()
     first_item = response_text["todos"][0]
     todo_properties = ["userId", "id", "title", "completed"]
     res = list(filter(lambda x: x not in first_item, todo_properties))
     assert len(res) == 0