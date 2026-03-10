📊 GT STRATEGIC PERFORMANCE DASHBOARD
--------------------------------------
import pandas as pd

def gt_bowling_efficiency_fixed(master_df):
  
    Identifies the most effective bowlers by analyzing Strike Rate (Balls/Wicket) 
    and Economy (Runs/Over) for those with a significant sample size.
   
    # Filter for all balls bowled by GT
    gt_bowling = master_df[master_df['bowling_team'] == 'Gujarat Titans']

    # Aggregating stats
    bowler_stats = gt_bowling.groupby('bowler').agg({
        'ball': 'count',
        'runs_off_bat': 'sum',
        'wicket_type': 'count'
    })

    # 1. We only want bowlers who have actually taken a wicket
    # 2. We only want bowlers who have bowled at least 5 overs (30 balls)
    real_threats = bowler_stats[(bowler_stats['wicket_type'] > 0) & (bowler_stats['ball'] >= 30)].copy()

    # Calculating the real Strike Rate (Balls per Wicket)
    real_threats['strike_rate'] = real_threats['ball'] / real_threats['wicket_type']

    # Calculating Economy (Runs per over)
    real_threats['economy'] = (real_threats['runs_off_bat'] / (real_threats['ball'] / 6))

    print("\n--- 🎯 REAL GT STRIKE-RATE KINGS (Top 5) ---")
    print(real_threats[['ball', 'wicket_type', 'strike_rate', 'economy']].sort_values('strike_rate').head(5))

def gt_death_over_finishers(master_df):
   
    Filters batting data for the 'Death Overs' (16.1 to 20.0) 
    to find players with the highest scoring intensity at the end of the innings.
   
    # 1. Filter for GT Batting in the Death Overs (Over 16.1 to 19.6)
    # Note: In Cricsheet format, 16.0 indicates the 17th over has started.
    gt_death = master_df[(master_df['batting_team'] == 'Gujarat Titans') & (master_df['ball'] >= 16.0)]

    # 2. Group by batsman
    finisher_stats = gt_death.groupby('striker').agg({
        'ball': 'count',
        'runs_off_bat': 'sum',
        'wicket_type': 'count'
    })

    # 3. Calculate Strike Rate (Runs per 100 balls)
    finisher_stats['strike_rate'] = (finisher_stats['runs_off_bat'] / finisher_stats['ball']) * 100

    # 4. Filter for players who have faced at least 20 balls in the death
    real_finishers = finisher_stats[finisher_stats['ball'] >= 20].sort_values('strike_rate', ascending=False)

    print("\n--- 🔥 GT'S MOST DANGEROUS DEATH OVER BATSMEN ---")
    print(real_finishers[['ball', 'runs_off_bat', 'strike_rate']].head(5))

def gt_phase_analysis(master_df):
   
    Compares the scoring intensity (RPO) between the Powerplay and the Death Overs 
    to understand where GT applies the most pressure.
  
    # Filter for GT Batting
    gt_batting = master_df[master_df['batting_team'] == 'Gujarat Titans']

    # Define the Phases (Powerplay: 0-6 overs | Death: 15-20 overs)
    pp_data = gt_batting[gt_batting['ball'] < 6.0]
    death_data = gt_batting[gt_batting['ball'] >= 15.0]

    def get_phase_stats(df, phase_name):
        runs = df['runs_off_bat'].sum() + df['extras'].sum()
        balls = len(df)
        if balls == 0: return {'Phase': phase_name, 'RPO': 0, 'Total Balls': 0}
        rpo = (runs / balls) * 6 # Runs per Over (RPO)
        return {'Phase': phase_name, 'RPO': round(rpo, 2), 'Total Balls': balls}

    stats = [get_phase_stats(pp_data, 'Powerplay'), get_phase_stats(death_data, 'Death')]

    phase_df = pd.DataFrame(stats)
    print("\n--- ⏳ GT SCORING INTENSITY BY PHASE ---")
    print(phase_df)

# --- RUNNING THE DASHBOARD ---
# When you have master_df loaded, you can call these:
# gt_bowling_efficiency_fixed(master_df)
# gt_death_over_finishers(master_df)
# gt_phase_analysis(master_df)
