import pandas as pd
import numpy as np
from numpy import zeros,array
df = pd.read_csv('market_basket.txt', 
                 header=None,delim_whitespace=True,
                 names='ID Product'.split(' '))
df1 = df.head(50)
# Creating Empty DataFrame and Storing it in variable df
headers = df1["ID"].drop_duplicates()
products = df1["Product"].drop_duplicates()
df2 = pd.DataFrame(index=headers)
""""
for i in products:
    tab = zeros(50, int)
    a2 = df1.groupby("Product", as_index=False).get_group(i)
    for j in range (50):
        print(j in a2["ID"])
            #tab[j]=1
        #print(tab)
        print("************* ",j," ****************") """
a2 = df1.groupby(["ID","Product"]).get_group("98pct_Fat_Free_Hamburger")
print(a2)
#for j in range (50):
       # print("sweet potatoes in",j,": ",j in a2["ID"])
  

# print dataframe.
#print(tab)