
Write a program that makes a DELETE request to remove the user your create in a previous example.

Again make a GET request to confirm that information has been deleted.


import requests

r = requests.delete("http://demo.codingnomads.co:8080/tasks_api/users/363")
print(r.status_code)
