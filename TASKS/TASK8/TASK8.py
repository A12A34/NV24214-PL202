import os
from pathlib import Path
import subprocess

import requests

url = "https://api.github.com/users/torvalds"

response = requests.get(url)

data = response.json()

print("Name:", data["name"])
print("Public Repos:", data["public_repos"])
print("Followers:", data["followers"])
requirements_path = Path(__file__).with_name("requirements.txt")
with requirements_path.open("w") as req_file:
    subprocess.run(["pip", "freeze"], stdout=req_file, check=True)
