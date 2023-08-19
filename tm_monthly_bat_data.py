from pybaseball import team_batting
import pandas as pd

for month in [4,5,6,7,8]:
    df = team_batting(2023,month=month)
    df['Month'] = month
    if month == 4:
        master_df = df
    else:
        master_df = pd.concat([master_df,df])

# print(master_df)
