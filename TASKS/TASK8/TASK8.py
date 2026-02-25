import requests

url = "https://api.github.com/users/torvalds"

response = requests.get(url)

data = response.json()

print("Name:", data["name"])
print("Public Repos:", data["public_repos"])
print("Followers:", data["followers"])