import plotly.express as px
import plotly.graph_objects as go
# from pitcher_plus_team import full_df
from pitcher_plus_ytd import full_df as new_df
from pitcher_df_transformations import pitcher_df
from scipy.stats import pearsonr, spearmanr
from sklearn.metrics import mean_squared_error

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

def scatter(df, x, y, hover, title):
    fig = px.scatter(data_frame=df, x=x, y=y, hover_data=hover, trendline='ols', title=title)
    fig.show()


# scatter(pitcher_df.query('GS == 1'), 'shft_mean', 'fantasy_pts', ['Name', 'Team_Abbrev', 'Date'])
# fig = fig = px.scatter(data_frame=pitcher_df.query('GS == 1'), x='shft_median', y='fantasy_pts',
#                        hover_data = ['Name', 'Team_Abbrev', 'Date', 'Differential'], color='Diff_bool')
# fig.show()


def r_stats(df, x, y):
    r = pearsonr(df[x], df[y])
    r = round(r[0], 3)
    r2 = round(r**2, 5)
    rmse = mean_squared_error(df[x], df[y]) ** 0.5
    return r, r2, rmse


def get_title_str(r, r2, rmse):
    title_str = f"""
    R: {r}
    \n
    R^2: {r2}
    \n
    RMSE: {rmse}
    """
    return title_str


def gen_models(df, x, y, hover):
    r, r2, rmse = r_stats(df, x, y)
    title_str = get_title_str(r, r2, rmse)
    scatter(df, x, y, hover, title_str)


df = new_df.query('GS == 1')
y = 'fantasy_pts'
hover = ['Name', 'Team', 'Date_x']
# xlist = ['wOBA', 'WAR', 'K%', 'BB%', 'ISO', 'BABIP', 'AVG', 'OBP', 'SLG', 'wRC+', 'BsR', 'Off', 'Def']
xlist = ['exp_mean', 'exp_median']
for x in xlist:
    print(x)
    gen_models(df, x, y, hover)
