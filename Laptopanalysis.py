from unittest.mock import inplace

import pandas as pd
import numpy as np
df_laptops=pd.read_csv('Laptops_Analysis.csv')
df_laptops.rename(columns={'Company':'Brand'},inplace=True)
print (df_laptops['Brand'].value_counts())
print (df_laptops [df_laptops['Brand']=='Apple'].value_counts('Brand'))
print (df_laptops [df_laptops['Brand']!='HP' ])
print(df_laptops[df_laptops['Price (USD)']>2000])
np.where(df_laptops['Price (USD)']>2000,'Expensive','Cheap')
df_laptops['Price_tiers']= np.where(df_laptops['Price (USD)']>2000,'Expensive','Cheap')
print(df_laptops)
print(df_laptops.value_counts('Price_tiers'))
np.where(df_laptops['Screen Size (inches)']>15,'Big','Normal')
df_laptops['Screen_Level']=np.where(df_laptops['Screen Size (inches)']>15,'Big','Normal')
print(df_laptops.head())
print(df_laptops['Screen_Level'].value_counts())
(df_laptops['Brand'] == 'Apple') & (df_laptops['Price (USD)'] > 2000)
print(df_laptops[(df_laptops['Brand'] == 'Apple') & (df_laptops['Price (USD)'] > 2000)])
df_laptops[df_laptops ['Brand']=='Apple']
df_laptops[df_laptops ['Brand']=='HP']
((df_laptops ['Brand']=='Apple') | (df_laptops ['Brand']=='HP')) & (df_laptops['Price (USD)']>2000)
print(df_laptops[(df_laptops ['Brand']=='Apple') | (df_laptops ['Brand']=='HP') & (df_laptops['Price (USD)']>2000)])
#conditions=[
 #   df_laptops['Price (USD)']>3000,
  #  (df_laptops['Price (USD)']>2000) & (df_laptops['Price (USD)']<3000),
   # (df_laptops['Price (USD)']>800) & (df_laptops['Price (USD)']<2000),
    #(df_laptops['Price (USD)']<=800)

#]

#values=['Too Expensive','Expensive','Affordable','Cheap']


#df_laptops['priceranging']=np.select(conditions,values)
#print(df_laptops)

#df_laptops['company'] .isin(['Apple','HP'])
#print(df_laptops[df_laptops['company'] .isin(['Apple','HP'])])
#df_laptops.duplicated(['Model/Version','Processor'])
#print (df_laptops[df_laptops.duplicated(['Model/Version','Processor','Storage'])])
#df_laptops.sort_values(['Brand','Price (USD)'])
#df_laptops=df_laptops.sort_values(['Brand','Price (USD)'])
#print(df_laptops)
df_laptops.drop_duplicates(['Brand'])
print(df_laptops)