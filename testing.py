import pybaseball
from pybaseball import batting_stats, team_batting, team_game_logs, statcast, pitching_stats_range, pitching_stats_bref, retrosheet, playerid_reverse_lookup, team_ids

# data = batting_stats(2023)
# print(data)

data = team_batting(2023,ind=0, month="8")
print(data)

# batting_logs = team_game_logs(2023, "TBR")
# print(batting_logs)

# data = statcast(team='ATL')
# print(data)

# data = pitching_stats_range("2023-07-01", "2023-07-02")
# print(data)

# data = pitching_stats_bref(2023)
# print(data)

# data = retrosheet.season_game_logs(2023)
# print(data)

# player = playerid_reverse_lookup([642585])
# print(player)

# teams = team_ids()
# print(teams)

