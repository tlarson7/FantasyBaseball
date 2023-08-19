import plotly.express as px
import plotly.graph_objects as go
# from pitcher_plus_team import full_df
# from pitcher_plus_ytd import full_df as new_df
from pitcher_df_transformations import pitcher_df

# fig = px.scatter(data_frame=full_df.loc[full_df['GS'] == 1],x='wOBA', y='fantasy_pts', hover_data=['Name', 'Team', 'Date'])
# fig.show()

# median_df = full_df.loc[full_df['GS'] == 1].groupby(['wOBA'])[['wOBA','fantasy_pts']].median()
# fig = px.scatter(data_frame=median_df,x='wOBA', y='fantasy_pts')
# fig.show()

# fig = px.scatter(data_frame=new_df.loc[new_df['GS'] == 1],x='wOBA', y='fantasy_pts', hover_data=['Name', 'Team', 'Date_x'], trendline='ols')
# fig.show()

# median_df = new_df.loc[new_df['GS'] == 1].groupby(['wOBA'])[['wOBA','fantasy_pts']].median()
# fig = px.scatter(data_frame=median_df,x='wOBA', y='fantasy_pts', trendline='ols')
# fig.show()

# fig = px.scatter(data_frame=new_df.loc[new_df['GS'] == 1],x='WAR', y='fantasy_pts', hover_data=['Name', 'Team', 'Date_x'], trendline='ols')
# fig.show()

# median_df = new_df.loc[new_df['GS'] == 1].groupby(['WAR'])[['WAR','fantasy_pts']].median()
# fig = px.scatter(data_frame=median_df,x='WAR', y='fantasy_pts', trendline='ols')
# fig.show()

# fig = px.scatter(data_frame=new_df.loc[new_df['GS'] == 1],x='avg_fpts', y='fantasy_pts', hover_data=['Name', 'Team', 'Date_x'], trendline='ols')
# fig.show()

def scatter(df, x, y, hover):
    fig = px.scatter(data_frame=df, x=x, y=y, hover_data=hover, trendline='ols')
    fig.show()


# scatter(pitcher_df.query('GS == 1'), 'shft_mean', 'fantasy_pts', ['Name', 'Team_Abbrev', 'Date'])
fig = fig = px.scatter(data_frame=pitcher_df.query('GS == 1'), x='shft_median', y='fantasy_pts',
                       hover_data = ['Name', 'Team_Abbrev', 'Date', 'Differential'], color='Diff_bool')
fig.show()