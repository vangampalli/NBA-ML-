import pandas as pd
from basketball_reference_scraper.seasons import get_schedule

season_games = pd.DataFrame()
for i in range(2017,2020):
    year_df = get_schedule(i)
    season_games = pd.concat([season_games,year_df])
season_games.to_csv("seasons.csv")





