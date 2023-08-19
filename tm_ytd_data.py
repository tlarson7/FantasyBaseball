import struct
import pandas as pd
from datetime import datetime
import datetime as dt

test_url = 'https://www.fangraphs.com/leaders.aspx?pos=all&stats=bat&lg=all&qual=0&type=0&season=2023&month=7&season1=2023&ind=0&team=0,ts&rost=0&age=0&filter=&players=0'

# start date
start_date = datetime.strptime("2023-03-30", "%Y-%m-%d")
end_date = datetime.today().date()

# difference between each date. D means one day
D = 'D'

date_list = pd.date_range(start_date, end_date, freq=D)
# print(f"Creating list of dates starting from {start_date} to {end_date}")
# print(date_list)

# if you want dates in string format then convert it into string
dates_as_strings = date_list.strftime("%Y-%m-%d").to_list()

master_df = pd.DataFrame()
for i,ds in enumerate(dates_as_strings):
    print(ds)
    dashboard_url = f'https://www.fangraphs.com/leaders.aspx?pos=all&stats=bat&lg=all&qual=0&type=8&season=2023&month=7&season1=2023&ind=0&team=0,ts&rost=0&age=0&filter=&players=0&startdate=2023-03-3-&enddate={ds}'
    print(dashboard_url)
    df = pd.read_html(dashboard_url)
    df = df[5]

    df2 = pd.DataFrame()
    for i, col in enumerate(df.columns):
        # print(col[1])
        # print(col)
        if i == 0:
            continue
        df2[col[1]] = df.iloc[:, i].to_frame()

    df2.drop([30], inplace=True)
    cur_date = datetime.strptime(ds, "%Y-%m-%d")
    df2['Date'] = cur_date
    df2['YTD_Target'] = cur_date - dt.timedelta(days=1)

    master_df = pd.concat([master_df, df2])

master_df.to_csv('tm_ytd_batting_data.csv')
# print(df2)
