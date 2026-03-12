#python -m venv myfirstproject
#source myfirstproject/bin/activate
#source NV24214-PL202\myfirstproject\bin\activate
#pip install pandas
from pathlib import Path

import pandas as pd

data_path = Path(__file__).with_name('data.csv')
df = pd.read_csv(data_path)
print(df.to_string())
