import pandas as pd

df = pd.read_csv('demografia.csv', decimal=".", na_values=".")
maxPK = df.max()[1:]
maxP = maxPK.max()
maxPid = maxPK.idxmax()
maxPiw=df[maxPid].idxmax()
print(maxPK)
print(f"Najwiekszy przyrost w wusokosci : {maxP} \n"
      f"mial miejsce w roku: {maxPid} \n"
      f"w kraju: {df['KRAJE'][maxPiw]}")

