import pandas as pd

df = pd.read_csv("AB_NYC_2019.csv")
df['reviews_per_month'] = df['reviews_per_month'].astype(str)
df['reviews_per_month'] = df['reviews_per_month'].apply(lambda x: x.replace('nan','0'))
df['reviews_per_month'] = df['reviews_per_month'].astype(float)
df['last_review'] = pd.to_datetime(df['last_review'])

missing_values = df.isnull().sum()
# Display the DataFrame of missing values
print(missing_values)

print(df.info())
df.to_csv('AB1_NYC_2019.csv', index=False)