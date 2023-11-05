import pandas as pd

df = pd.read_csv('your_file.csv')

column_labels = df.columns

print("Column Labels:")
for label in column_labels:
	print(label)

r  =df['players']

for item in r.values:
    print(type(item))