import requests

response = requests.get("https://api.github.com/users/legacychris/repos")
print(response.json)