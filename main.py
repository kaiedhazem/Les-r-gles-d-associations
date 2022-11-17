# importing pandas
import pandas as pd
from mlxtend.frequent_patterns import apriori 
from mlxtend.frequent_patterns import association_rules
import numpy as np
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
T=pd.crosstab(df["ID"], [df["Product"]], rownames=['ID'], colnames=['Products'])
#print(T.iloc[:30,:3])

#a priori
freq_itemsets = apriori(T,min_support=0.025,max_len=4,use_colnames=True)
#print(freq_itemsets.head(15))
#fonction de test d'inclusion
def is_inclus(x,items):
 return items.issubset(x)

id = np.where(freq_itemsets.itemsets.apply(is_inclus,items={'Aspirin'}))
id2 = np.where(freq_itemsets.itemsets.apply(is_inclus,items={'Aspirin','Eggs'}))
#affichage des itemsets corresp.
#print(freq_itemsets.loc[id2])
regles = association_rules(freq_itemsets,metric="confidence",min_threshold=0.75)
#5 "premières" règles
#print(regles.iloc[:5,:])
#affichage des règles avec un LIFT supérieur ou égal à 7
print(regles[regles['lift'].ge(7.0)])
#filtrer les règles menant au conséquent {‘2pct_milk’}
print(regles[regles['consequents'].eq({'2pct_Milk'})])