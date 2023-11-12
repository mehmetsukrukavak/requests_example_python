import requests


user_input = input("Enter Id : ")
url = f"https://jsonplaceholder.typicode.com/todos/{user_input}"

get_response = requests.get(url)
print(get_response.json())