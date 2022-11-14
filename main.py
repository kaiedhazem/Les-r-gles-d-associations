# importing pandas
import pandas as pd
  
# read text file into pandas DataFrame
df = pd.read_csv('market_basket.txt', 
                 header=None,delim_whitespace=True,
                 names='ID Product'.split(' '))
df1 = df.head(10)
# Afficher les 10 premières lignes du DataFrame
#print(df1)
# Afficher les dimensions du dataframe.
#print(df.shape)

#extraire les valeurs sans redondances
headers = df1["ID"].drop_duplicates()
products = df1["Product"].drop_duplicates()
# compare result with crosstab
print((pd.crosstab(df1["ID"], [df1["Product"]], rownames=['ID'], colnames=['Products'])))


