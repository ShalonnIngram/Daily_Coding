# creating a POST request to add information to the API data
base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "first_name": "[Shalonn]",
    "last_name": "[Ingram]",
    "email": "[mscianika@gmail.com]"
}

response = requests.post(base_url, json=body)
print(f"Response Code: {response.status_code}")
