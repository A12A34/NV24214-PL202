import math
import os
from pathlib import Path
import subprocess

print(math.sqrt(16))

requirements_path = Path(__file__).with_name("requirements.txt")
with requirements_path.open("w") as req_file:
    subprocess.run(["pip", "freeze"], stdout=req_file, check=True)
