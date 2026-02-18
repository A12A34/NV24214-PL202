#python -m venv myfirstproject
#source myfirstproject/bin/activate
#source NV24214-PL202\myfirstproject\bin\activate
#pip install pandas
import pandas as pd
df = pd.read_csv('data.csv')
print(df.to_string())
