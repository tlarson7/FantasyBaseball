import pandas as pd
import datetime

pitcher_df = pd.read_csv('pitcher_logs.csv')

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

pitcher_df['Date'] = pd.to_datetime(pitcher_df['Date'])

pitcher_df['GS'] = pd.to_numeric(pitcher_df['GS'])
pitcher_df[['W','L','SV']] = pitcher_df[['W','L','SV']].fillna(0)
pitcher_df['fantasy_pts'] = pitcher_df['IP'] * 3 \
                           + pitcher_df['H'] * -1 \
                           + pitcher_df['ER'] * -2 \
                           + pitcher_df['BB'] * -1 \
                           + pitcher_df['SO'] * 1 \
                           + pitcher_df['W'] * 2 \
                           + pitcher_df['L'] * -2 \
                           + pitcher_df['SV'] * 5

# pitcher_df['avg_fpts'] = pitcher_df.groupby('mlbID')['fantasy_pts'].transform('sum') / pitcher_df.groupby('mlbID')['fantasy_pts'].transform('count')
# pitcher_df['med_fpts'] = pitcher_df.groupby('mlbID')['fantasy_pts'].transform('median')

ytd_df = pitcher_df.copy()
ytd_df.sort_values(by=['mlbID', 'Date'], inplace=True)
ytd_df.reset_index(drop=True, inplace=True)
# unknown = ytd_df.groupby('mlbID')['fantasy_pts'].expanding().mean().reset_index(drop=True)
ytd_df['exp_sum'] = ytd_df.groupby('mlbID')['fantasy_pts'].expanding().sum().reset_index(drop=True)
ytd_df['exp_count'] = ytd_df.groupby('mlbID')['fantasy_pts'].expanding().count().reset_index(drop=True)
ytd_df['exp_mean'] = ytd_df.groupby('mlbID')['fantasy_pts'].expanding().mean().reset_index(drop=True)
ytd_df['exp_median'] = ytd_df.groupby('mlbID')['fantasy_pts'].expanding().median().reset_index(drop=True)

# stats_to_cum = ['SO', 'BB', 'H', 'R', 'ER', 'HR', 'IP']
# for stat in stats_to_cum:
#     ytd_df[f'cum_{stat}'] = ytd_df.groupby('mlbID')[stat].expanding().sum().reset_index(drop=True)
# ytd_df['cum_K/BB'] = ytd_df['cum_SO'] / ytd_df['cum_BB']

# ytd_df['Target_Date'] = ytd_df['Date'] - datetime.timedelta(days=1)
ytd_df['Target_Date'] = ytd_df.groupby('mlbID')['Date'].shift(-1)
# ytd_df['shft_mean'] = ytd_df.groupby('mlbID')['exp_mean'].shift(1)
# ytd_df['shft_median'] = ytd_df.groupby('mlbID')['exp_median'].shift(1)

pitcher_df.sort_values(by=['mlbID', 'Date'], inplace=True)
pitcher_df.reset_index(drop=True, inplace=True)

pitcher_df = pd.merge(pitcher_df, ytd_df[['mlbID', 'exp_mean', 'exp_median', 'Date', 'Target_Date']],
                      how='left', left_on=['mlbID', 'Date'], right_on=['mlbID', 'Target_Date'])

# pitcher_df['Differential'] = pitcher_df['fantasy_pts'] - pitcher_df['shft_median']
# pitcher_df.loc[(pitcher_df['Differential'] >= 0), ['Diff_bool']] = 'Pos'
# pitcher_df.loc[(pitcher_df['Differential'] < 0), ['Diff_bool']] = 'Neg'

# pitcher_df.query('GS == 1', inplace=True)
print(pitcher_df)
# print(pitcher_df['Differential'].sum())