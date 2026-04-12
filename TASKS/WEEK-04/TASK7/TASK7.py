import math
import os
from pathlib import Path

print(math.sqrt(16))

requirements_path = Path(__file__).with_name("requirements.txt")
os.system(f'pip freeze > "{requirements_path}"')
