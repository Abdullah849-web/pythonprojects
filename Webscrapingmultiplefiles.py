import pandas as pd
root= "https://www.football-data.co.uk/mmz4281/"
Leagues=['E0','E1','E2','E3','EC']
Frames= []

for League in Leagues:
     df = pd.read_csv (root+'2425'+'/'+ League + '.csv')
     Frames.append(df)



print(Frames[0])



