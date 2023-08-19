from pybaseball import pitching_stats_range
from datetime import datetime
import pandas as pd


# start date
start_date = datetime.strptime("2023-03-30", "%Y-%m-%d")
end_date = datetime.today().date()

# difference between each date. D means one day
D = 'D'

date_list = pd.date_range(start_date, end_date, freq=D)
# print(f"Creating list of dates starting from {start_date} to {end_date}")
# print(date_list)

# if you want dates in string format then convert it into string
dates_as_strings = date_list.strftime("%Y-%m-%d")

master_df = pd.DataFrame()
for i,ds in enumerate(dates_as_strings):
    print(ds)
    try:
        df = pitching_stats_range(ds, ds)
    except IndexError:
        print(f"{ds} not valid in search")
    if i == 0:
        master_df = df
    else:
        master_df = pd.concat([master_df, df])
    # if i > 0:
    #     break
# print(master_df)
# print(master_df.dtypes)

master_df[['W','L','SV']] = master_df[['W','L','SV']].fillna(0)
master_df['fantasy_pts'] = master_df['IP'] * 3 \
                           + master_df['H'] * -1 \
                           + master_df['ER'] * -2 \
                           + master_df['BB'] * -1 \
                           + master_df['SO'] * 1 \
                           + master_df['W'] * 2 \
                           + master_df['L'] * -2 \
                           + master_df['SV'] * 5
# master_df.to_csv('pitcher_logs.csv')
# df = pitching_stats_range("2023-07-17", "2023-07-17")
# print(master_df)