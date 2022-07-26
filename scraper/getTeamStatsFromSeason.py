from basketball_reference_scraper.teams import get_team_stats
import pandas as pd
teams = ["TOR","BOS","PHI","CLE","IND","MIA","MIL","WAS","DET","CHO","NYK","BRK","CHI","ORL","ATL","HOU","GSW","POR","OKC","UTA","NOP","SAS","MIN","DEN","LAC","LAL","SAC","DAL","MEM","PHO"]
stats_df = pd.DataFrame(columns=['G','MP','FG','FGA','FG%','3P','3PA','3P%','2P','2PA','2P%','FT','FTA','FT%','ORB','DRB','TRB','AST','STL','BLK','TOV','PF','PTS',"TEAM",'SEASON'])
for year in range(2017,2020):
    for t in teams:
        print(year, t)
        df = pd.DataFrame(get_team_stats(t,year)).T

        stats_df = pd.concat([stats_df,df])

stats_df.to_csv(f"test.csv")

