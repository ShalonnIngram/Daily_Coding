
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.



import requests
from pprint import pprint

r = requests.get("http://demo.codingnomads.co:8080/tasks_api/users")
info = r.json()

# loop through nested json data to return all emails
for i in info["data"]:
    pprint(i["email"])
