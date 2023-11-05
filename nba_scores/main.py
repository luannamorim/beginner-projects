from requests import get
from datetime import datetime

BASE_URL = "https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json"


def get_scoreboard():
    response = get(BASE_URL).json()
    games = response['scoreboard']['games']
    date_games = response['scoreboard']['gameDate']
    date_formated = datetime.strptime(
        date_games, "%Y-%m-%d").strftime("%d/%m/%Y")

    print(f"📅 NBA scores {date_formated}:\n")

    for game in games:
        home_team = game['homeTeam']
        away_team = game['awayTeam']
        status_game = game['gameStatusText']

        if home_team['score'] != 0 and away_team['teamName'] != 0:
            print("🏀", status_game)
            print(
                f"{home_team['teamName']} {home_team['score']}:{away_team['score']} {away_team['teamName']}\n")

        else:
            print("🏀", status_game)
            print(f"{home_team['teamName']} vs {away_team['teamName']}\n")


print(get_scoreboard())
