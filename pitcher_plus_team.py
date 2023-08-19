import pandas as pd
from pybaseball import team_batting
from tm_monthly_bat_data import master_df as batting_df

pitcher_df = pd.read_csv('pitcher_logs.csv')

# def add_team_abbrevs(row):
#     if row['Lev'] == 'Maj-AL':
#         if row['Tm'] ==
# len(pitcher_df[pitcher_df['Team_Abbrev'].isna()])

pitcher_df[['W','L','SV']] = pitcher_df[['W','L','SV']].fillna(0)
pitcher_df['fantasy_pts'] = pitcher_df['IP'] * 3 \
                           + pitcher_df['H'] * -1 \
                           + pitcher_df['ER'] * -2 \
                           + pitcher_df['BB'] * -1 \
                           + pitcher_df['SO'] * 1 \
                           + pitcher_df['W'] * 2 \
                           + pitcher_df['L'] * -2 \
                           + pitcher_df['SV'] * 5


pitcher_df.loc[(pitcher_df['Opp'] == 'Baltimore'), ['Team_Abbrev']] = 'BAL'
pitcher_df.loc[(pitcher_df['Opp'] == 'Boston'), ['Team_Abbrev']] = 'BOS'
pitcher_df.loc[(pitcher_df['Opp'] == 'Chicago') & (pitcher_df['Lev'] == 'Maj-AL'), ['Team_Abbrev']] = 'CHW'
pitcher_df.loc[(pitcher_df['Opp'] == 'Cleveland'), ['Team_Abbrev']] = 'CLE'
pitcher_df.loc[(pitcher_df['Opp'] == 'Detroit'), ['Team_Abbrev']] = 'DET'
pitcher_df.loc[(pitcher_df['Opp'] == 'Houston'), ['Team_Abbrev']] = 'HOU'
pitcher_df.loc[(pitcher_df['Opp'] == 'Kansas City'), ['Team_Abbrev']] = 'KCR'
pitcher_df.loc[(pitcher_df['Opp'] == 'Los Angeles'), ['Team_Abbrev']] = 'LAA'
pitcher_df.loc[(pitcher_df['Opp'] == 'Minnesota'), ['Team_Abbrev']] = 'MIN'
pitcher_df.loc[(pitcher_df['Opp'] == 'New York') & (pitcher_df['Lev'] == 'Maj-AL'), ['Team_Abbrev']] = 'NYY'
pitcher_df.loc[(pitcher_df['Opp'] == 'Oakland'), ['Team_Abbrev']] = 'OAK'
pitcher_df.loc[(pitcher_df['Opp'] == 'Seattle'), ['Team_Abbrev']] = 'SEA'
pitcher_df.loc[(pitcher_df['Opp'] == 'Tampa Bay'), ['Team_Abbrev']] = 'TBR'
pitcher_df.loc[(pitcher_df['Opp'] == 'Texas'), ['Team_Abbrev']] = 'TEX'
pitcher_df.loc[(pitcher_df['Opp'] == 'Toronto'), ['Team_Abbrev']] = 'TOR'
pitcher_df.loc[(pitcher_df['Opp'] == 'Arizona'), ['Team_Abbrev']] = 'ARI'
pitcher_df.loc[(pitcher_df['Opp'] == 'Atlanta'), ['Team_Abbrev']] = 'ATL'
pitcher_df.loc[(pitcher_df['Opp'] == 'Chicago') & (pitcher_df['Lev'] == 'Maj-NL'), ['Team_Abbrev']] = 'CHC'
pitcher_df.loc[(pitcher_df['Opp'] == 'Cincinnati'), ['Team_Abbrev']] = 'CIN'
pitcher_df.loc[(pitcher_df['Opp'] == 'Colorado'), ['Team_Abbrev']] = 'COL'
pitcher_df.loc[(pitcher_df['Opp'] == 'Los Angeles') & (pitcher_df['Lev'] == 'Maj-NL'), ['Team_Abbrev']] = 'LAD'
pitcher_df.loc[(pitcher_df['Opp'] == 'Miami'), ['Team_Abbrev']] = 'MIA'
pitcher_df.loc[(pitcher_df['Opp'] == 'Milwaukee'), ['Team_Abbrev']] = 'MIL'
pitcher_df.loc[(pitcher_df['Opp'] == 'New York') & (pitcher_df['Lev'] == 'Maj-NL'), ['Team_Abbrev']] = 'NYM'
pitcher_df.loc[(pitcher_df['Opp'] == 'Philadelphia'), ['Team_Abbrev']] = 'PHI'
pitcher_df.loc[(pitcher_df['Opp'] == 'Pittsburgh'), ['Team_Abbrev']] = 'PIT'
pitcher_df.loc[(pitcher_df['Opp'] == 'San Diego'), ['Team_Abbrev']] = 'SDP'
pitcher_df.loc[(pitcher_df['Opp'] == 'San Francisco'), ['Team_Abbrev']] = 'SFG'
pitcher_df.loc[(pitcher_df['Opp'] == 'St. Louis'), ['Team_Abbrev']] = 'STL'
pitcher_df.loc[(pitcher_df['Opp'] == 'Washington'), ['Team_Abbrev']] = 'WSN'
# print(len(pitcher_df[pitcher_df['Team_Abbrev'].isna()]))
# print(pitcher_df)

# Setting Month value to Month - 1 to prevent data leak. Not using data for Mar/Apr
# pitcher_df.loc[(pitcher_df['Date'].str.split(expand=True)[0] == 'Mar'), ['Month']] = 4
# pitcher_df.loc[(pitcher_df['Date'].str.split(expand=True)[0] == 'Apr'), ['Month']] = 4
pitcher_df.loc[(pitcher_df['Date'].str.split(expand=True)[0] == 'May'), ['Month']] = 4
pitcher_df.loc[(pitcher_df['Date'].str.split(expand=True)[0] == 'Jun'), ['Month']] = 5
pitcher_df.loc[(pitcher_df['Date'].str.split(expand=True)[0] == 'Jul'), ['Month']] = 6
pitcher_df.loc[(pitcher_df['Date'].str.split(expand=True)[0] == 'Aug'), ['Month']] = 7

# batting_df = team_batting(2023)

full_df = pd.merge(pitcher_df, batting_df, left_on=['Team_Abbrev', 'Month'], right_on=['Team', 'Month'])
print(full_df)

