import requests
import json

#GET
get_url = "https://jsonplaceholder.typicode.com/todos/15"

get_response = requests.get(get_url)
print(get_response.json())



#PUT
to_do_item = {"userId": 2, "title": "my to do putting", "completed": False}
put_response = requests.put(get_url, json=to_do_item)
print(put_response.json())

#PATCH
to_do_item = {"title": "my to do patch"}
patch_response = requests.patch(get_url, json=to_do_item)
print(patch_response.json())

#DELETE
delete_response = requests.delete(get_url)
print(delete_response.json())
print(delete_response.status_code)

