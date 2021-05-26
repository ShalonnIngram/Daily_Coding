import requests
from pprint import pprint


# use the pprint library to return a GET request from the API
params = {
    "email": "martin@email.com"
}

response = requests.get("http://demo.codingnomads.co:8080/tasks_api/users", params=params)
pprint(response.json())
















