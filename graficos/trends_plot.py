# -*- coding: utf-8 -*-
"""trends_plot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12xp7y9Lqs-pAJbgU9YGispnOf1yS3Dg-
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel (r'trends.xls')
print(df)

df["\ttweet_volume"] = pd.to_numeric(df["\ttweet_volume"])
df2 = df.sort_values(by=['\ttweet_volume'], ascending=[False])
df2

graf_linha = sns.lineplot(data = df2, x="\tname", y="\ttweet_volume", color = "red" )
graf_linha.set_title("Twitter Trending Topics")
plt.xticks(rotation=90)
plt.show(graf_linha, figsize=(10, 10))