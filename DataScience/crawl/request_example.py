import requests


# r = requests.get('https://jsonplaceholder.typicode.com/todos/1')
# r = requests.get('https://api.github.com/users/teghfo')
r = requests.get('https://api.github.com/users/Teghfo/repos')

# print(r.content)
# print(r.text)
print(r.json())
