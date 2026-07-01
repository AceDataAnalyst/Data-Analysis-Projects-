import pandas as pd

df=pd.read_csv('data.csv')
#print(df.dtypes)
#print(df.isnull().any())
#print(df.isnull().sum())
df_filled=df.fillna(0)

##filling missing values with the mean of the colunm
df['Sales_fillNA']=df['Sales'].fillna(df['Sales'].mean())
#print(df['Sales_fillNA'])
#print(df)

#print(df.dtypes)

#Renaming columns 
df2=df.rename(columns={'Date':'Sales Date'})
print(df2.head())