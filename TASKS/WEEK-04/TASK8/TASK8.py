import requests
import os
from pathlib import Path

url = "https://api.github.com/users/torvalds"

response = requests.get(url)

data = response.json()

print("Name:", data["name"])
print("Public Repos:", data["public_repos"])
print("Followers:", data["followers"])
requirements_path = Path(__file__).with_name("requirements.txt")
os.system(f'pip freeze > "{requirements_path}"')
