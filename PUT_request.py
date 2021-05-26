import requests

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"


# update existing record with PUT request
body = {
    "id": 361,
    "first_name": "Cianika",
    "last_name": "Campbell",
    "email": "mscianika2@email.com"
}

# execute the PUT request
response = requests.put(base_url, json=body)

# print the status code
print(f"Response Code: {response.status_code}")

# make a GET request to retrieve the new data from the server
response = requests.get(base_url)

# print the updated record
print(f"Response Content: {response.content}")