import pandas as ps

df = ps.read_json('../TASK9/data.json')
print(df.head(7))
print(df.tail(7))