
team_abb = {
"ATLANTA HAWKS" : "ATL",
"ST. LOUIS HAWKS" : "SLH",
"MILWAUKEE HAWKS" : "MIL",
"TRI-CITIES BLACKHAWKS" : "TCB",
"BOSTON CELTICS" : "BOS",
"BROOKLYN NETS" : "BRK",
"NEW JERSEY NETS" : "NJN",
"CHICAGO BULLS" : "CHI",
#"CHARLOTTE HORNETS": "CHH",
"CHARLOTTE HORNETS": "CHO",
"CHARLOTTE BOBCATS" : "CHA",
"CLEVELAND CAVALIERS" : "CLE",
"DALLAS MAVERICKS" : "DAL",
"DENVER NUGGETS" : "DEN",
"DETROIT PISTONS" : "DET",
"FORT WAYNE PISTONS" : "FWP",
"GOLDEN STATE WARRIORS" : "GSW",
"SAN FRANCISCO WARRIORS" : "SFW",
"PHILADELPHIA WARRIORS" : "PHI",
"HOUSTON ROCKETS" : "HOU",
"INDIANA PACERS" : "IND",
"LOS ANGELES CLIPPERS" : "LAC",
"SAN DIEGO CLIPPERS" : "SDC",
"BUFFALO BRAVES" : "BUF",
"LOS ANGELES LAKERS" : "LAL",
"MINNEAPOLIS LAKERS" : "MIN",
"MEMPHIS GRIZZLIES" : "MEM",
"VANCOUVER GRIZZLIES" : "VAN",
"MIAMI HEAT" : "MIA",
"MILWAUKEE BUCKS" : "MIL",
"MINNESOTA TIMBERWOLVES" : "MIN",
"NEW ORLEANS PELICANS" : "NOP",
"NEW ORLEANS/OKLAHOMA CITY HORNETS" : "NOK",
"NEW ORLEANS HORNETS" : "NOH",
"NEW YORK KNICKS" : "NYK",
"OKLAHOMA CITY THUNDER" : "OKC",
"SEATTLE SUPERSONICS" : "SEA",
"ORLANDO MAGIC" : "ORL",
"PHILADELPHIA 76ERS" : "PHI",
"SYRACUSE NATIONALS" : "SYR",
"PHOENIX SUNS" : "PHO",
"PORTLAND TRAIL BLAZERS" : "POR",
"SACRAMENTO KINGS" : "SAC",
"KANSAS CITY KINGS" : "KCK",
"KANSAS CITY-OMAHA KINGS" : "KCK",
"CINCINNATI ROYALS" : "CIN",
"ROCHESTER ROYALS" : "ROR",
"SAN ANTONIO SPURS" : "SAS",
"TORONTO RAPTORS" : "TOR",
"UTAH JAZZ" : "UTA",
"NEW ORLEANS JAZZ" : "NOJ",
"WASHINGTON WIZARDS" : "WAS",
"WASHINGTON BULLETS" : "WAS",
"CAPITAL BULLETS" : "CAP",
"BALTIMORE BULLETS" : "BAL",
"CHICAGO ZEPHYRS" : "CHI",
"CHICAGO PACKERS" : "CHI",
"ANDERSON PACKERS" : "AND",
"CHICAGO STAGS" : "CHI",
"INDIANAPOLIS OLYMPIANS" : "IND",
"SHEBOYGAN RED SKINS" : "SRS",
"ST. LOUIS BOMBERS" : "SLB",
"WASHINGTON CAPITOLS" : "WAS",
"WATERLOO HAWKS" : "WAT",
"SAN DIEGO ROCKETS" : "SDR"
}


from basketball_reference_scraper.box_scores import get_box_scores
import pandas as pd
import csv
from basketball_reference_scraper.seasons import get_schedule

for i in range(2014,2017):
    season_games = pd.DataFrame()
    year_df = get_schedule(i)
    for index, row in year_df.iterrows():
        try:
            date = str(row["DATE"])[:10]
            teamAway = team_abb[row["VISITOR"].upper()]
            teamHome = team_abb[row["HOME"].upper()]
            gameId = (date + teamHome + teamAway).replace("-","") #20171017BOSCLE
            print(f"Getting data for {date}, {teamHome} vs {teamAway}")
            box_score = get_box_scores(date,teamAway,teamHome)
            teamHome_df = box_score[teamHome]
            teamHome_df.insert(0,"TEAM",teamHome)
            teamHome_df = teamHome_df[:8]

            teamAway_df = box_score[teamAway]
            teamAway_df.insert(0,"TEAM",teamAway)
            teamAway_df = teamAway_df[:8]

            game_df = pd.concat([teamHome_df, teamAway_df])
            game_df.insert(0, "GAMEID",gameId,True)
            game_df = game_df.loc[(game_df["MP"] != 'Did Not Play') & (game_df["MP"] != 'Player Suspended') & (game_df["MP"] != 'Did Not Dress') & (game_df["MP"] != 'Not With Team')]
            
            season_games = pd.concat([season_games,game_df])
        except:
            print("Whoops!")
    season_games.to_csv(f"{i}.csv")





