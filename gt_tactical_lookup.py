
🏏 GT TACTICAL LOOKUP & MATCHUP ENGINE
--------------------------------------

import pandas as pd

# NOTE: This script assumes you have already run the master engine 
# and have 'master_df' ready in your environment.

def run_gt_tactical_analysis(master_df):
    print("🚀 Initializing GT Tactical View...")
    
    # 1. Create a specialized DataFrame for GT
    # We check both batting and bowling to get a full 360-degree view
    gt_batting = master_df[master_df['batting_team'] == 'Gujarat Titans']
    gt_bowling = master_df[master_df['bowling_team'] == 'Gujarat Titans']

    print(f"✅ GT Batting Database: {len(gt_batting)} balls indexed.")
    print(f"✅ GT Bowling Database: {len(gt_bowling)} balls indexed.")

    # 2. Finding the 'Captain's Impact'
    # How many runs has Shubman Gill scored specifically for GT?
    gill_stats = gt_batting[gt_batting['striker'] == 'Shubman Gill']
    total_runs = gill_stats['runs_off_bat'].sum()
    
    print("-" * 30)
    print(f"👑 CAPTAIN'S IMPACT: Shubman Gill")
    print(f"Total Runs for GT: {int(total_runs)}")
    print("-" * 30)

def get_matchup(master_df, bowler_name, batsman_name):
    """
    Tactical Head-to-Head (H2H) Engine.
    Filters the master database for specific historical matchups.
    """
    matchup = master_df[(master_df['bowler'] == bowler_name) & (master_df['striker'] == batsman_name)]

    if len(matchup) == 0:
        print(f"\n🔍 No historical data for {bowler_name} vs {batsman_name}")
        return

    balls = len(matchup)
    runs = matchup['runs_off_bat'].sum()
    # Counting dismissals by checking the wicket column
    wickets = matchup['wicket_type'].dropna().count()

    strike_rate = (runs / balls) * 100

    print(f"\n⚡ HEAD-TO-HEAD: {batsman_name} vs {bowler_name}")
    print(f"• Balls Faced: {balls}")
    print(f"• Runs Scored: {runs}")
    print(f"• Dismissals:  {wickets}")
    print(f"• Strike Rate: {strike_rate:.2f}")
    
    if wickets > 2:
        print("💡 ANALYST NOTE: High-risk matchup for the batter.")

# --- EXAMPLE USAGE ---
# If running this as a standalone, ensure master_df is passed:
# run_gt_tactical_analysis(master_df)
# get_matchup(master_df, 'JJ Bumrah', 'Shubman Gill')
