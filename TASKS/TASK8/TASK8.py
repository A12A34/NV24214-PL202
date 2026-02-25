import requests
import os

url = "https://api.github.com/users/torvalds"

response = requests.get(url)

data = response.json()

print("Name:", data["name"])
print("Public Repos:", data["public_repos"])
print("Followers:", data["followers"])
os.system("pip freeze > TASKS\\TASK8\\requirements.txt")