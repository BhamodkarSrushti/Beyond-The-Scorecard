
 GT DATA INTEGRITY & VENUE SPECIALIST (2026)

import pandas as pd
import numpy as np

# --- 1. VENUE IMPACT ENGINES ---

def gt_bowling_venue_impact(master_df, bowler_name):
    """
    Quantifies 'Defensive Impact' by comparing Home vs Away Economy.
    """
    bowler_data = master_df[master_df['bowler'] == bowler_name]
    
    # Split using fuzzy matching for Ahmedabad venue variations
    home_mask = bowler_data['venue'].str.contains('Ahmedabad|Narendra Modi', case=False, na=False)
    home_data = bowler_data[home_mask]
    away_data = bowler_data[~home_mask]

    def get_economy(df):
        if len(df) == 0: return 0.0
        # Economy = (Runs / Overs) where 1 over = 6 balls
        return (df['runs_off_bat'].sum() + df['extras'].sum()) / (len(df) / 6)

    print(f"\n--- 🛡️ DEFENSIVE IMPACT: {bowler_name} ---")
    print(f"Home Economy: {get_economy(home_data):.2f} ({len(home_data)//6} overs)")
    print(f"Away Economy: {get_economy(away_data):.2f} ({len(away_data)//6} overs)")

def gt_home_vs_away_analysis(master_df, player_name):
    """
    Quantifies 'Offensive Impact' by comparing Home vs Away Strike Rate.
    """
    player_data = master_df[master_df['striker'] == player_name]
    
    home_mask = player_data['venue'].str.contains('Ahmedabad|Narendra Modi', case=False, na=False)
    home_data = player_data[home_mask]
    away_data = player_data[~home_mask]

    def get_sr(df):
        if len(df) == 0: return 0.0
        return (df['runs_off_bat'].sum() / len(df)) * 100

    print(f"\n--- 🏟️ VENUE IMPACT (OFFENSIVE): {player_name} ---")
    print(f"Home Strike Rate: {get_sr(home_data):.2f} ({len(home_data)} balls)")
    print(f"Away Strike Rate: {get_sr(away_data):.2f} ({len(away_data)} balls)")

# --- 2. DATA INTEGRITY ENGINES ---

def check_missing_matches_by_season(master_df):
    """
    Audits the Master DB against official IPL match counts.
    """
    # Use match_id if available, otherwise fallback to start_date
    id_col = 'match_id' if 'match_id' in master_df.columns else 'start_date'
    
    season_stats = master_df.groupby('season')[id_col].nunique().reset_index()
    season_stats.columns = ['Season', 'Matches_Found']

    # Official counts for IPL 2022-2025
    official_counts = {'2022': 74, '2023': 74, '2024': 74, '2025': 74}

    print("\n--- 🔍 DATA INTEGRITY AUDIT ---")
    for _, row in season_stats.iterrows():
        s = str(row['Season'])
        found = row['Matches_Found']
        official = official_counts.get(s, "N/A")

        if isinstance(official, int):
            status = "✅ Complete" if found == official else f"❌ Missing {official - found} matches"
        else:
            status = "Incomplete Reference"
            
        print(f"Season {s}: Found {found} matches | {status}")

def check_gt_match_continuity(master_df, target_season):
    """
    Chronological audit of GT appearances in a specific season.
    """
    # Standardize season as string for safe filtering
    master_df['season_str'] = master_df['season'].astype(str)
    
    gt_matches = master_df[
        (master_df['season_str'] == str(target_season)) &
        ((master_df['batting_team'] == 'Gujarat Titans') | (master_df['bowling_team'] == 'Gujarat Titans'))
    ]

    unique_dates = gt_matches['start_date'].unique()

    print(f"\n--- ⚡ GT MATCH TIMELINE ({target_season}) ---")
    if len(unique_dates) > 0:
        sorted_dates = np.sort(unique_dates)
        for i, date in enumerate(sorted_dates):
            print(f"Match {i+1:02}: {pd.to_datetime(date).date()}")
    else:
        print(f"No match data found for GT in {target_season}.")

# --- EXECUTION ---
# check_missing_matches_by_season(master_df)
# gt_home_vs_away_analysis(master_df, 'Shubman Gill')
