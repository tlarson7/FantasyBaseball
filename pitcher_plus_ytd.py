import pandas as pd
from pitcher_df_transformations import pitcher_df

batting_df = pd.read_csv('tm_ytd_batting_data.csv')
batting_df['YTD_Target'] = pd.to_datetime(batting_df['YTD_Target'])
batting_df['YTD_Target'] = pd.to_datetime(batting_df.groupby('Team')['Date'].shift(-1))

full_df = pd.merge(left=pitcher_df, right=batting_df, left_on=['Team_Abbrev','Date'], right_on=['Team','YTD_Target'])
print(full_df)