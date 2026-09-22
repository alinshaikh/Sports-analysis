import pandas as pd
import matplotlib.pyplot as plt


# Load datasets

player_performance = pd.read_csv("player_performance.csv")
matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")
players = pd.read_csv("players.csv")
teams = pd.read_csv("teams.csv")
venues = pd.read_csv("venues.csv")


# Basic dataset information

print("\nPLAYER PERFORMANCE")
print(player_performance.head())
print(player_performance.shape)
print(player_performance.info())

print("\nMATCHES")
print(matches.head())
print(matches.shape)

print("\nDELIVERIES")
print(deliveries.head())
print(deliveries.shape)

print("\nPLAYERS")
print(players.head())
print(players.shape)

print("\nTEAMS")
print(teams.head())
print(teams.shape)

print("\nVENUES")
print(venues.head())
print(venues.shape)


# Missing values

print("\nMISSING VALUES")
print("Player Performance:\n", player_performance.isnull().sum())
print("Matches:\n", matches.isnull().sum())
print("Deliveries:\n", deliveries.isnull().sum())
print("Players:\n", players.isnull().sum())
print("Teams:\n", teams.isnull().sum())
print("Venues:\n", venues.isnull().sum())


# Player analysis

players_by_team = players.groupby("team").size().sort_values(ascending=False)

print("\nPLAYERS BY TEAM")
print(players_by_team)

players_by_role = players["role"].value_counts()

print("\nPLAYERS BY ROLE")
print(players_by_role)

average_age = players.groupby("team")["age"].mean().round(2)

print("\nAVERAGE AGE BY TEAM")
print(average_age)


# Team analysis

team_matches = pd.concat([
    matches[["team1"]].rename(columns={"team1": "team"}),
    matches[["team2"]].rename(columns={"team2": "team"})
])

matches_played = team_matches["team"].value_counts()

wins = matches["winner"].value_counts()

team_analysis = pd.DataFrame({
    "matches_played": matches_played,
    "wins": wins
}).fillna(0)

team_analysis["losses"] = (
    team_analysis["matches_played"] -
    team_analysis["wins"]
)

team_analysis["win_percentage"] = (
    team_analysis["wins"] /
    team_analysis["matches_played"] * 100
).round(2)

team_analysis = team_analysis.sort_values(
    "win_percentage",
    ascending=False
)

print("\nTEAM PERFORMANCE")
print(team_analysis)


# Toss analysis

toss_wins = matches["toss_winner"].value_counts()

toss_match_wins = (
    matches["toss_winner"] == matches["winner"]
).sum()

toss_win_percentage = (
    toss_match_wins /
    len(matches) * 100
)

print("\nTOSS WINNERS")
print(toss_wins)

print("\nTOSS WINNER MATCH WIN PERCENTAGE")
print(round(toss_win_percentage, 2))


# Toss decision analysis

toss_decision_analysis = (
    matches.groupby("toss_decision")
    .size()
    .sort_values(ascending=False)
)

print("\nTOSS DECISIONS")
print(toss_decision_analysis)


# Season analysis

season_analysis = matches.groupby("season").agg(
    matches=("match_id", "count"),
    total_run_margin=("win_by_runs", "sum"),
    total_wicket_margin=("win_by_wickets", "sum")
)

print("\nSEASON ANALYSIS")
print(season_analysis)


# Player of the match

player_of_match = (
    matches["player_of_match"]
    .value_counts()
    .head(10)
)

print("\nTOP PLAYER OF THE MATCH AWARDS")
print(player_of_match)


# Delivery analysis

total_runs = deliveries["total_runs"].sum()
total_batter_runs = deliveries["runs_batter"].sum()
total_extra_runs = deliveries["runs_extra"].sum()
total_wickets = deliveries["is_wicket"].sum()

print("\nDELIVERY ANALYSIS")
print("Total Runs:", total_runs)
print("Batter Runs:", total_batter_runs)
print("Extra Runs:", total_extra_runs)
print("Wickets:", total_wickets)


# Batting analysis

batting = deliveries.groupby("batter").agg(
    runs=("runs_batter", "sum"),
    balls_faced=("batter", "count")
)

batting["strike_rate"] = (
    batting["runs"] /
    batting["balls_faced"] * 100
).round(2)

batting = batting.sort_values(
    "runs",
    ascending=False
)

print("\nTOP BATTERS")
print(batting.head(10))


# Add player information

top_batters = (
    batting.reset_index()
    .merge(
        players[["player_id", "player_name", "team"]],
        left_on="batter",
        right_on="player_id",
        how="left"
    )
)

print("\nTOP BATTERS WITH PLAYER DETAILS")
print(
    top_batters[
        ["player_name", "team", "runs", "balls_faced", "strike_rate"]
    ].head(10)
)


# Bowling analysis

bowling = deliveries.groupby("bowler").agg(
    runs_conceded=("total_runs", "sum"),
    balls_bowled=("bowler", "count"),
    wickets=("is_wicket", "sum")
)

bowling["economy"] = (
    bowling["runs_conceded"] /
    bowling["balls_bowled"] * 6
).round(2)

bowling = bowling.sort_values(
    "wickets",
    ascending=False
)

print("\nTOP BOWLERS")
print(bowling.head(10))


# Add bowler information

top_bowlers = (
    bowling.reset_index()
    .merge(
        players[["player_id", "player_name", "team"]],
        left_on="bowler",
        right_on="player_id",
        how="left"
    )
)

print("\nTOP BOWLERS WITH PLAYER DETAILS")
print(
    top_bowlers[
        [
            "player_name",
            "team",
            "wickets",
            "runs_conceded",
            "economy"
        ]
    ].head(10)
)


# Match analysis

match_runs = (
    deliveries.groupby("match_id")["total_runs"]
    .sum()
    .sort_values(ascending=False)
)

match_analysis = (
    matches[
        [
            "match_id",
            "season",
            "team1",
            "team2",
            "venue",
            "winner"
        ]
    ]
    .merge(
        match_runs.rename("total_runs"),
        on="match_id",
        how="left"
    )
)

print("\nHIGHEST SCORING MATCHES")
print(
    match_analysis
    .sort_values("total_runs", ascending=False)
    .head(10)
)


# Venue analysis

venue_analysis = matches.groupby("venue").agg(
    matches_played=("match_id", "count"),
    average_run_margin=("win_by_runs", "mean"),
    average_wicket_margin=("win_by_wickets", "mean")
).round(2)

venue_analysis = venue_analysis.sort_values(
    "matches_played",
    ascending=False
)

print("\nVENUE ANALYSIS")
print(venue_analysis)


# Venue capacity analysis

venue_capacity = venues.sort_values(
    "capacity",
    ascending=False
)

print("\nLARGEST VENUES")
print(
    venue_capacity[
        ["venue_name", "city", "capacity"]
    ].head(10)
)


# Powerplay analysis

powerplay = (
    deliveries[deliveries["over"] <= 2]
    .groupby("inning")["total_runs"]
    .sum()
)

print("\nPOWERPLAY RUNS")
print(powerplay)


# Death over analysis

death_overs = (
    deliveries[deliveries["over"] >= 5]
    .groupby("inning")["total_runs"]
    .sum()
)

print("\nDEATH OVER RUNS")
print(death_overs)


# Run distribution

run_distribution = (
    deliveries["runs_batter"]
    .value_counts()
    .sort_index()
)

print("\nRUN DISTRIBUTION")
print(run_distribution)


# Wicket analysis

wickets_by_batter = (
    deliveries[deliveries["is_wicket"] == 1]
    .groupby("batter")
    .size()
    .sort_values(ascending=False)
)

print("\nWICKETS LOST BY BATTER")
print(wickets_by_batter.head(10))


# Player performance analysis

performance = (
    player_performance
    .merge(
        players[
            [
                "player_id",
                "player_name",
                "team",
                "role"
            ]
        ],
        on="player_id",
        how="left"
    )
)

print("\nPLAYER PERFORMANCE")
print(performance.head())


# Player performance ranking

performance_ranked = performance.sort_values(
    "runs",
    ascending=False
)

print("\nTOP PLAYER PERFORMERS")
print(performance_ranked.head(10))


# =========================
# VISUALIZATIONS
# =========================


# 1. Players by team

plt.figure(figsize=(10, 6))
players_by_team.plot(kind="bar")
plt.title("Players by Team")
plt.xlabel("Team")
plt.ylabel("Number of Players")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 2. Players by role

plt.figure(figsize=(8, 6))
players_by_role.plot(kind="bar")
plt.title("Players by Role")
plt.xlabel("Role")
plt.ylabel("Number of Players")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# 3. Team wins

plt.figure(figsize=(10, 6))
wins.sort_values(ascending=False).plot(kind="bar")
plt.title("Team Wins")
plt.xlabel("Team")
plt.ylabel("Wins")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 4. Team win percentage

plt.figure(figsize=(10, 6))
team_analysis["win_percentage"].plot(kind="bar")
plt.title("Team Win Percentage")
plt.xlabel("Team")
plt.ylabel("Win Percentage")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 5. Top 10 batsmen

plt.figure(figsize=(10, 6))
batting.head(10)["runs"].sort_values().plot(kind="barh")
plt.title("Top 10 Run Scorers")
plt.xlabel("Runs")
plt.ylabel("Player")
plt.tight_layout()
plt.show()


# 6. Top 10 bowlers

plt.figure(figsize=(10, 6))
bowling.head(10)["wickets"].sort_values().plot(kind="barh")
plt.title("Top 10 Wicket Takers")
plt.xlabel("Wickets")
plt.ylabel("Player")
plt.tight_layout()
plt.show()


# 7. Strike rate

strike_rate_top = (
    batting[batting["balls_faced"] >= 10]
    .sort_values("strike_rate", ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))
strike_rate_top["strike_rate"].sort_values().plot(kind="barh")
plt.title("Top Strike Rates")
plt.xlabel("Strike Rate")
plt.ylabel("Player")
plt.tight_layout()
plt.show()


# 8. Bowling economy

economy_top = (
    bowling[bowling["balls_bowled"] >= 10]
    .sort_values("economy")
    .head(10)
)

plt.figure(figsize=(10, 6))
economy_top["economy"].sort_values(ascending=False).plot(kind="barh")
plt.title("Best Bowling Economy")
plt.xlabel("Economy")
plt.ylabel("Player")
plt.tight_layout()
plt.show()


# 9. Runs by over

runs_by_over = (
    deliveries.groupby("over")["total_runs"]
    .sum()
)

plt.figure(figsize=(10, 6))
runs_by_over.plot(kind="line", marker="o")
plt.title("Runs by Over")
plt.xlabel("Over")
plt.ylabel("Total Runs")
plt.grid(True)
plt.tight_layout()
plt.show()


# 10. Wickets by over

wickets_by_over = (
    deliveries.groupby("over")["is_wicket"]
    .sum()
)

plt.figure(figsize=(10, 6))
wickets_by_over.plot(kind="bar")
plt.title("Wickets by Over")
plt.xlabel("Over")
plt.ylabel("Wickets")
plt.tight_layout()
plt.show()


# 11. Season matches

season_matches = matches["season"].value_counts().sort_index()

plt.figure(figsize=(10, 6))
season_matches.plot(kind="bar")
plt.title("Matches by Season")
plt.xlabel("Season")
plt.ylabel("Matches")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# 12. Toss decisions

plt.figure(figsize=(8, 6))
toss_decision_analysis.plot(kind="pie", autopct="%1.1f%%")
plt.title("Toss Decision Distribution")
plt.ylabel("")
plt.tight_layout()
plt.show()


# 13. Venue matches

venue_matches = matches["venue"].value_counts().head(10)

plt.figure(figsize=(10, 6))
venue_matches.sort_values().plot(kind="barh")
plt.title("Top Venues by Matches")
plt.xlabel("Matches")
plt.ylabel("Venue")
plt.tight_layout()
plt.show()


# 14. Run distribution

plt.figure(figsize=(10, 6))
run_distribution.plot(kind="bar")
plt.title("Batting Run Distribution")
plt.xlabel("Runs on Delivery")
plt.ylabel("Number of Deliveries")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# 15. Powerplay vs death overs

phase_data = pd.DataFrame({
    "Powerplay": [powerplay.sum()],
    "Death Overs": [death_overs.sum()]
})

plt.figure(figsize=(8, 6))
phase_data.iloc[0].plot(kind="bar")
plt.title("Powerplay vs Death Over Runs")
plt.xlabel("Phase")
plt.ylabel("Runs")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# 16. Player performance

top_performance = performance_ranked.head(10)

plt.figure(figsize=(10, 6))
plt.barh(
    top_performance["player_name"],
    top_performance["runs"]
)
plt.title("Top Player Performance by Runs")
plt.xlabel("Runs")
plt.ylabel("Player")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()


# Export analysis results

team_analysis.to_csv("team_analysis.csv")
batting.reset_index().to_csv("batting_analysis.csv", index=False)
bowling.reset_index().to_csv("bowling_analysis.csv", index=False)
venue_analysis.reset_index().to_csv("venue_analysis.csv")
match_analysis.to_csv("match_analysis.csv", index=False)

print("\nAnalysis completed successfully.")
print("Results exported successfully.")
