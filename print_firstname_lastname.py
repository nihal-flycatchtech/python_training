# Write a Python program which takes first and last name from the following API https://reqres.in/api/users?page=2 and print them in the following format
# Name : First_name Last_name
# Eg : Name : Hole Eve

import requests

response = requests.get("https://reqres.in/api/users?page=2")
json_data=response.json()
for i in json_data['data']:
    print("Name :"+i["first_name"]+" "+i["last_name"])


