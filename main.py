"""
🏆 BEYOND-THE-SCORECARD: THE GT COMMAND CENTER (2026)

# Import all your specialized modules
import gt_strategy_engine as engine
import gt_performance_analytics as perf
import gt_tactical_lookup as tact
import gt_predictive_intelligence as pred
import gt_ground_intelligence as ground
import gt_data_integrity_venue as audit

def run_full_gt_briefing(opponent, current_score, wickets, strikers, temp, pitch, dew):
    print("\n" + "█"*60)
    print(" INITIALIZING GT STRATEGY COMMAND CENTER")
    print("█"*60)

    # 1. LOAD & AUDIT DATA
    # This ensures the analyst knows the data is fresh and complete
    master_df = engine.load_and_clean_data() # Assuming the load logic is in a function
    audit.check_missing_matches_by_season(master_df)

    # 2. PRE-MATCH GROUND ADVISORY
    # Is it a 'Bat First' day in Ahmedabad?
    ground.get_ahmedabad_toss_advice(temp, pitch, dew)

    # 3. PERFORMANCE DASHBOARD
    # Who are our 'Real Threats' and 'Death Kings' lately?
    perf.gt_bowling_efficiency_fixed(master_df)
    perf.gt_death_over_finishers(master_df)

    # 4. TACTICAL HEAD-TO-HEAD
    # Check the specific matchups for the current strikers
    for batter in strikers:
        # Check against the opponent's lead bowler (e.g., Bumrah if MI)
        lead_bowler = 'JJ Bumrah' if opponent == 'Mumbai Indians' else 'Avesh Khan'
        tact.get_matchup(master_df, lead_bowler, batter)

    # 5. LIVE WIN PROBABILITY & FORECASTING
    # The 'Bumrah Tax' and 'Gear Shift' logic applied live
    pred.predict_gt_final_score_v3(current_score, wickets, strikers, opponent)
    
    print("\n" + "█"*60)
    print("🏁 STRATEGIC BRIEFING COMPLETE")
    print("█"*60)

# --- EXECUTION ---
if __name__ == "__main__":
    # SCENARIO: GT vs MI, 95/2 at 10 overs, hot day in Ahmedabad
    run_full_gt_briefing(
        opponent='Mumbai Indians',
        current_score=95,
        wickets=2,
        strikers=['Shubman Gill', 'Sai Sudharsan'],
        temp=41,
        pitch='Red Soil',
        dew=False
    )
