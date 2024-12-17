import pandas as pd

df = pd.read_csv('demografia.csv', decimal=".", na_values=".")
idx = df['2022'].idxmax()
print(df['KRAJE'][idx])

