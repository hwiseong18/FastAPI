import requests

url = "http://127.0.0.1:8000/todo"
headers = {
    "accept": "application/json"
}

response = requests.get(url, headers=headers)
print(response.json())