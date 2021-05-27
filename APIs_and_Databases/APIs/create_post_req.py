
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.



base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "first_name": "[Shalonn]",
    "last_name": "[Ingram]",
    "email": "[mscianika@gmail.com]"
}

response = requests.post(base_url, json=body)
print(f"Response Code: {response.status_code}")

r = requests.get("http://demo.codingnomads.co:8080/tasks_api/users")
print()
