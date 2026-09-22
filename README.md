# 🏏 Sports Analytics Project

## 📌 Project Overview

This project analyzes sports performance data using SQL, Python and Power BI to identify insights related to players, teams, matches, batting, bowling, venues, toss decisions and overall team performance.

The project follows a complete data analytics workflow:

Data → SQL Analysis → Python Analysis → Visualization → Power BI Dashboard → Insights

The dataset contains multiple related tables that allow analysis using JOINs, aggregations, CTEs, CASE statements and window functions.

## 🎯 Objectives

- Analyze player performance
- Identify top run scorers and wicket takers
- Analyze team wins and win percentage
- Study toss decisions and match results
- Analyze match and season performance
- Identify high-performing venues
- Analyze batting strike rates
- Analyze bowling economy
- Study powerplay and death-over performance
- Create player and team rankings
- Create data-driven visualizations
- Build an interactive Power BI dashboard

## 📂 Dataset

The project contains six interconnected datasets:

### 1. player_performance.csv

Contains player-level performance information used to analyze individual player statistics.

### 2. matches.csv

Contains match-level information including:

- Match ID
- Season
- Date
- Teams
- Venue
- Toss winner
- Toss decision
- Match winner
- Winning margin
- Player of the Match

### 3. deliveries.csv

Contains ball-by-ball information including:

- Match
- Innings
- Over
- Ball
- Batter
- Bowler
- Non-striker
- Batter runs
- Extra runs
- Total runs
- Wickets

### 4. players.csv

Contains player information including:

- Player ID
- Player name
- Team
- Role
- Batting style
- Bowling style
- Nationality
- Age

### 5. teams.csv

Contains team information including:

- Team ID
- Team name
- Short name
- City
- Home venue
- Founded year

### 6. venues.csv

Contains venue information including:

- Venue ID
- Venue name
- City
- State
- Capacity
- Established year

## 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- SQL
- Power BI
- DAX
- GitHub

## 🗄️ SQL Analysis

The SQL analysis covers beginner to advanced concepts.

### Basic Analysis

- Dataset exploration
- Record counts
- Player distribution
- Team distribution
- Venue analysis
- Season analysis

### Player Analysis

- Players by team
- Players by role
- Average player age
- Top run scorers
- Top wicket takers
- Player rankings

### Team Analysis

- Matches played
- Wins
- Losses
- Win percentage
- Team rankings
- Season performance

### Match Analysis

- Matches by season
- Match winners
- Winning margins
- Player of the Match
- Toss decisions
- Toss winner vs match winner

### Batting Analysis

- Total runs
- Balls faced
- Strike rate
- Top batters

### Bowling Analysis

- Runs conceded
- Wickets
- Economy rate
- Top bowlers

### Advanced SQL

The project uses:

- JOIN
- GROUP BY
- HAVING
- CASE
- CTE
- Subqueries
- RANK()
- PARTITION BY
- Window Functions

SQL analysis is available in:

sports_analysis.sql

## 🐍 Python Analysis

Python is used for data exploration, analysis and visualization.

### Python Workflow

Load Data
↓
Explore Data
↓
Check Missing Values
↓
Analyze Players
↓
Analyze Teams
↓
Analyze Matches
↓
Analyze Batting
↓
Analyze Bowling
↓
Analyze Venues
↓
Analyze Toss
↓
Analyze Seasons
↓
Create Visualizations
↓
Export Results

Python analysis is available in:

sports_analysis.py

## 📊 Visualizations

The Python analysis includes visualizations for:

- Players by team
- Players by role
- Team wins
- Team win percentage
- Top run scorers
- Top wicket takers
- Strike rate
- Bowling economy
- Runs by over
- Wickets by over
- Matches by season
- Toss decisions
- Top venues
- Run distribution
- Powerplay vs death-over runs
- Player performance

## 📊 Power BI Dashboard

Power BI will be used as the dashboard and business intelligence layer of the project.

The dashboard will transform the analyzed data into an interactive reporting experience.

### Planned Dashboard Pages

#### 1. Overview Dashboard

KPIs:

- Total Matches
- Total Players
- Total Runs
- Total Wickets
- Average Runs
- Team Win Percentage

Visuals:

- Team wins
- Matches by season
- Runs by season
- Venue distribution

#### 2. Player Performance Dashboard

KPIs and visuals:

- Top Run Scorers
- Top Wicket Takers
- Strike Rate
- Economy Rate
- Player Rankings
- Player performance by team
- Player role analysis

#### 3. Team Performance Dashboard

Analysis:

- Matches Played
- Wins
- Losses
- Win Percentage
- Team Rankings
- Season-wise performance

#### 4. Match Analysis Dashboard

Analysis:

- Matches by season
- Toss decisions
- Toss winner vs match winner
- Winning margins
- Player of the Match
- Venue performance

#### 5. Over & Scoring Analysis

Analysis:

- Runs by over
- Wickets by over
- Powerplay performance
- Death-over performance
- Run distribution

### Planned Power BI Features

- Interactive slicers
- KPI cards
- Bar charts
- Line charts
- Donut charts
- Tables
- Player filters
- Team filters
- Season filters
- Venue filters
- DAX measures
- Interactive dashboard navigation

The Power BI dashboard will be completed as the next stage of the project.

## 📈 Key KPIs

| KPI | Description |
|---|---|
| Total Matches | Number of matches analyzed |
| Total Players | Number of players |
| Total Runs | Runs scored across deliveries |
| Total Wickets | Wickets recorded |
| Top Run Scorer | Player with highest runs |
| Top Wicket Taker | Player with highest wickets |
| Strike Rate | Batting scoring rate |
| Economy Rate | Bowling runs conceded per over |
| Win Percentage | Team wins relative to matches played |
| Toss Win % | Matches where toss winner also won |

## 💡 Key Insights

The analysis can be used to identify:

- High-performing players
- Consistent run scorers
- Effective wicket-taking bowlers
- Teams with strong win percentages
- Venues with higher match activity
- Toss-related match patterns
- Scoring patterns across overs
- Powerplay and death-over performance
- Player performance differences
- Team performance trends across seasons

## 📁 Project Structure

Sports-Analytics/
│
├── data/
│   ├── player_performance.csv
│   ├── matches.csv
│   ├── deliveries.csv
│   ├── players.csv
│   ├── teams.csv
│   └── venues.csv
│
├── sports_analysis.sql
├── sports_analysis.py
│
├── team_analysis.csv
├── batting_analysis.csv
├── bowling_analysis.csv
├── venue_analysis.csv
│
├── powerbi/
│   └── Sports_Analytics_Dashboard.pbix
│
└── README.md

## 🚀 How to Run

### 1. Clone the repository

git clone <repository-url>

### 2. Open the project

cd Sports-Analytics

### 3. Install Python libraries

pip install pandas matplotlib

### 4. Run Python analysis

python sports_analysis.py

### 5. Run SQL analysis

Open sports_analysis.sql in your SQL environment and execute the queries.

### 6. Power BI

Import the CSV datasets into Power BI and build the planned dashboard using relationships, visuals, slicers and DAX measures.

## 🔍 Skills Demonstrated

- Data Cleaning
- Exploratory Data Analysis
- SQL
- Advanced SQL
- Data Aggregation
- Data Joining
- Window Functions
- CTEs
- Python
- Pandas
- Matplotlib
- Data Visualization
- KPI Analysis
- Sports Analytics
- Power BI
- DAX
- Dashboard Development
- Business Intelligence
- GitHub

## 👨‍💻 Author

Alin Shaikh

BSc Computer Science  
Aspiring Data Analyst

Skills:

Python | SQL | Excel | Power BI | Data Analytics | Generative AI | Git

## ⚠️ Dataset Note

This project uses a synthetic sports dataset created for data analytics practice and portfolio demonstration. The data is not intended to represent official real-world tournament statistics.

## ⭐ Project Goal

The goal of this project is to demonstrate how raw sports data can be transformed into meaningful insights using SQL, Python, visualization and Power BI.

The project combines data analysis, statistical exploration, visualization and interactive business intelligence into a complete end-to-end analytics workflow.