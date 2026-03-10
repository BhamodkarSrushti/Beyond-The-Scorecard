 GT STRATEGY COMMAND CENTER (2026)
--------------------------------------

import pandas as pd

def gt_win_probability_calculator(current_score, wickets, strikers, opponent, overs_left=10):
  
    Calculates dynamic win probability based on historical Ahmedabad 
    home advantage and real-time player impact.
  
    # 1. Base Probability (Historical Ahmedabad Home Advantage)
    win_prob = 58.0

    # 2. Dynamic Projection Logic
    middle_rpo, death_rpo = 9.94, 11.67
    impact_players = {'Sai Sudharsan': 1.15, 'Shubman Gill': 1.10, 'David Miller': 1.20}

    current_mult = 1.0
    for p in strikers:
        current_mult = max(current_mult, impact_players.get(p, 1.0))

    # Calculate potential runs for remaining 10 overs
    projected_runs = ((5 * middle_rpo) + (5 * death_rpo)) * current_mult
    
    # Wicket Penalty: Harsher decay for 2026 season stats
    penalty = 1.0 if wickets <= 3 else (1.0 - ((wickets - 3) * 0.15))
    final_projection = current_score + (projected_runs * penalty)

    # 3. Probability Weighting based on Score Thresholds
    if final_projection > 210: win_prob += 25.0
    elif final_projection > 190: win_prob += 10.0
    elif final_projection < 160: win_prob -= 30.0
    else: win_prob -= 10.0

    # Opponent Adjustment (Tactical specific)
    if opponent == 'Rajasthan Royals':
        win_prob -= 10.0 
        print(f"⚠️ Tactical Alert: {opponent} has 'Gill-Neutralizers' (Avesh/Boult) in the squad.")

    # Bound the probability between 1% and 99%
    win_prob = max(1, min(99, win_prob))

    print(f"\n--- 📈 GT LIVE WIN PROBABILITY (Ahmedabad) ---")
    print(f"Current State: {current_score}/{wickets} | Projected: {int(final_projection)}")
    print(f"WIN PROBABILITY: {win_prob:.1f}%")

    # Visual Probability Bar (CLI Version)
    bar_length = int(win_prob / 2)
    print(f"[{'█' * bar_length}{'-' * (50 - bar_length)}]")

def gt_strategic_intelligence_dashboard(opponent, current_wickets, strikers, bumrah_overs=0, temp=40, pitch='Red Soil', dew=False):
    """
    Generates a full pre-match/mid-match Intelligence Report.
    """
    print("="*60)
    print(f"🚀 GUJARAT TITANS MATCH INTELLIGENCE REPORT vs {opponent}")
    print("="*60)

    # 1. TOSS ADVICE MODULE
    print("\n[SECTION 1: TOSS STRATEGY]")
    score_bat_first = 0
    if temp > 38: score_bat_first += 30
    if pitch == 'Red Soil': score_bat_first += 40
    if not dew: score_bat_first += 30
    rec = "BAT FIRST" if score_bat_first >= 60 else "BOWL FIRST"
    print(f"Recommendation: {rec} (Confidence: {score_bat_first}%)")

    # 2. VENUE IMPACT MODULE
    print("\n[SECTION 2: VENUE IMPACT (AHMEDABAD)]")
    print(f"- Shubman Gill Mode: 'HOME-HIGH' (Expected SR: 157.84)")
    print(f"- Rashid Khan Mode: 'DEFENSIVE-LOW' (Expected Econ: 9.28)")

    # 3. OPPONENT THREATS (Kryptonite Detection)
    print("\n[SECTION 3: OPPONENT THREATS]")
    threats = {
        'Mumbai Indians': "Jasprit Bumrah (SR 108)",
        'Rajasthan Royals': "Avesh Khan (2 Wkts) & TA Boult (SR 95)",
        'Chennai Super Kings': "TU Deshpande (2 Wkts)"
    }
    found = threats.get(opponent, "✅ No primary Gill-Neutralizers detected.")
    print(f"⚠️ Warning: {found}" if opponent in threats else found)

    print("\n" + "="*60)

def find_gill_kryptonite_ahmedabad(master_df):
    """
    Analyzes historical data to find bowlers who suppress 
    Gill's scoring rate at home.
    """
    # Filter for Gill at Ahmedabad
    gill_ahmedabad = master_df[
        (master_df['striker'] == 'Shubman Gill') &
        (master_df['venue'].str.contains('Ahmedabad|Narendra Modi', case=False, na=False))
    ]

    # Group by bowler (Min 18 balls/3 overs)
    bowler_vs_gill = gill_ahmedabad.groupby('bowler').agg({
        'runs_off_bat': 'sum',
        'ball': 'count',
        'match_id': 'nunique'
    })

    threats = bowler_vs_gill[bowler_vs_gill['ball'] >= 18].copy()
    threats['strike_rate'] = (threats['runs_off_bat'] / threats['ball']) * 100

    print("\n--- ⚔️ GILL'S BIGGEST THREATS IN AHMEDABAD (Min 18 balls) ---")
    print(threats.sort_values('strike_rate').head(5))

# --- EXAMPLE TEST RUN ---
# gt_strategic_intelligence_dashboard('Rajasthan Royals', 2, ['Shubman Gill', 'Sai Sudharsan'])
# gt_win_probability_calculator(85, 2, ['Shubman Gill'], 'Rajasthan Royals')
