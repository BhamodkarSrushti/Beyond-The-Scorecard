🔮 GT PREDICTIVE INTELLIGENCE 3.0
--------------------------------------

import matplotlib.pyplot as plt
import pandas as pd

def visualize_gt_gear_shift():
    """
    Generates a professional bar chart comparing GT's scoring 
    intensity in the Powerplay vs the Death Overs.
    """
    phases = ['Powerplay (Overs 1-6)', 'Death (Overs 16-20)']
    rpo_values = [8.04, 10.22] # Based on historical GT data

    # Professional GT Colors (Navy Blue and Gold/Yellow)
    plt.figure(figsize=(10, 6))
    bars = plt.bar(phases, rpo_values, color=['#1b2133', '#d1ab3e'], edgecolor='black')

    # Formatting
    plt.ylabel('Runs Per Over (RPO)', fontsize=12, fontweight='bold')
    plt.title('Gujarat Titans: The Gear Shift Analysis', fontsize=15, fontweight='bold', pad=20)
    plt.ylim(0, 12) 

    # Data Labels
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.3, yval, ha='center', va='bottom', fontsize=12, fontweight='bold')

    plt.grid(axis='y', linestyle='--', alpha=0.7)
    print("📊 Gear Shift Visualization Generated.")
    plt.show()

def predict_gt_final_score_v3(current_score, wickets_lost, strikers_list, opponent='Other', bumrah_overs_left=0):
    """
    Predicts the final 20-over total using:
    - Base Phase RPOs (Middle: 9.94, Death: 11.67)
    - Player Impact Multipliers (e.g., Tewatia 1.25x)
    - Opponent Penalties (The Bumrah Tax)
    - Wicket-based scoring decay
    """
    # Base GT Data (2025-26 Stats)
    middle_rpo = 9.94
    death_rpo = 11.67

    # Impact Player Multipliers (Historical scoring boosts)
    impact_players = {
        'Sai Sudharsan': 1.15, 
        'Shubman Gill': 1.10, 
        'David Miller': 1.20, 
        'Rahul Tewatia': 1.25
    }

    # Determine highest multiplier at the crease
    current_multiplier = 1.0
    for player in strikers_list:
        if player in impact_players:
            current_multiplier = max(current_multiplier, impact_players[player])

    # Calculate Base Remaining Runs (Assuming 10 overs left: 5 Middle, 5 Death)
    middle_runs = 5 * middle_rpo
    death_runs = 5 * death_rpo

    # --- THE BUMRAH TAX ---
    # Adjusts death potential if facing Mumbai Indians' lead bowler
    if opponent == 'Mumbai Indians' and bumrah_overs_left > 0:
        # Penalty = difference between avg death RPO and Bumrah's elite economy (~6.68)
        tax_per_over = (death_rpo - 6.68)
        total_tax = tax_per_over * bumrah_overs_left
        death_runs -= total_tax
        print(f"⚠️ Alert: Bumrah Tax applied (-{total_tax:.1f} runs)")

    # Wicket Penalty Logic (Harsher decay after 3 wickets)
    penalty = 1.0 if wickets_lost <= 3 else (1.0 - ((wickets_lost - 3) * 0.12))

    # Final Calculation
    final_projection = current_score + ((middle_runs + death_runs) * current_multiplier * penalty)

    print(f"\n--- GT Predictive Intelligence 3.0 ---")
    print(f"Opponent: {opponent}")
    print(f"Batting: {strikers_list} | Multiplier: {current_multiplier}x")
    print(f"Projected Final Score: {int(final_projection)}")
    print("-" * 35)

# --- EXAMPLE TEST ---
# Scenario: GT is 95/2 at 10 overs vs MI. 
# Sai Sudharsan is batting, and Bumrah has 2 death overs left.
# predict_gt_final_score_v3(95, 2, ['Sai Sudharsan'], opponent='Mumbai Indians', bumrah_overs_left=2)
