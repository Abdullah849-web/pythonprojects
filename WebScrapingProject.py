import pandas as pd
df_Footballanalysis = pd.read_csv('https://www.football-data.co.uk/mmz4281/2425/E0.csv')
df_Footballanalysis.rename(columns={'AvgCAHH':'Average_Crossess','AvgCAHA':'Average_corners','BFECAHH':'Ball_Fromentryhome','BFECAHA':'Ball_Fromentryaway'},inplace=True)
print(df_Footballanalysis)