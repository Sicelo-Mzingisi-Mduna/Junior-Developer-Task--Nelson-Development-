import requests

endpoint = "http://localhost:8000/REST_API/"

get_response = requests.post(endpoint, json = {"data": "example"})
print(get_response.json())