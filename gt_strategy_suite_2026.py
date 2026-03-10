import pandas as pd
import glob
import os

# --- 1. DATA LOADING ENGINE ---
path = './mentionthepathofurcsv' 
all_files = glob.glob(os.path.join(path, "*.csv"))

li = []

print("📂 Starting Beyond-The-Scorecard Data Engine...")

for filename in all_files:
    # Cricsheet 'info' files don't have ball data, so we filter them out
    if "_info" in filename:
        continue
        
    try:
        df = pd.read_csv(filename, low_memory=False)
        # Add the match ID from the filename for tracking unique games
        df['match_id'] = os.path.basename(filename).split('.')[0]
        li.append(df)
    except Exception as e:
        print(f"⚠️ Skipping {filename} due to error: {e}")

# --- 2. THE INTEGRITY CHECK ---
if li:
    # Combine everything into the Master Database
    master_df = pd.concat(li, axis=0, ignore_index=True)

    # Clean missing values so the math doesn't break
    cols_to_fix = ['runs_off_bat', 'extras', 'wides', 'noballs', 'byes', 'legbyes']
    master_df[cols_to_fix] = master_df[cols_to_fix].fillna(0)
    
    # Check if stacking worked correctly
    if not master_df.empty:
        print(f"\n✅ SUCCESS: Master Database Created.")
        print(f"📈 Total rows in Master Database: {len(master_df)}")
        print(f"🏟️ Matches Analysed: {master_df['match_id'].nunique()}")
        print("\n--- DATA PREVIEW (First 5 rows) ---")
        print(master_df.head())
    else:
        print("❌ ERROR: Database is empty. Adjusting the loop logic.")
        
    # --- 3. THE STRATEGIC INTELLIGENCE ---
    
    # Normalizing Ahmedabad stadium names for accurate stats
    master_df['venue'] = master_df['venue'].str.replace('Narendra Modi Stadium.*', 'Ahmedabad', regex=True)

    # A. Shubman Gill: The Home-Gain Metric
    gill_data = master_df[master_df['striker'] == 'Shubman Gill']
    gill_home = gill_data[gill_data['venue'].str.contains('Ahmedabad', na=False)]
    gill_away = gill_data[~gill_data['venue'].str.contains('Ahmedabad', na=False)]
    
    sr_home = (gill_home['runs_off_bat'].sum() / len(gill_home)) * 100 if not gill_home.empty else 0
    sr_away = (gill_away['runs_off_bat'].sum() / len(gill_away)) * 100 if not gill_away.empty else 0

    print("\n" + "="*40)
    print(" GUJARAT TITANS MATCH INTELLIGENCE")
    print("="*40)
    print(f"🏠 Shubman Gill Home SR (Ahmedabad): {sr_home:.2f}")
    print(f"✈️ Shubman Gill Away SR:              {sr_away:.2f}")
    print(f"⭐ STRATEGIC GAIN AT HOME:            +{sr_home - sr_away:.2f} pts")

    # B. Rashid Khan: The Economy Paradox
    rashid_home = master_df[(master_df['bowler'] == 'Rashid Khan') & (master_df['venue'] == 'Ahmedabad')]
    total_runs = rashid_home['runs_off_bat'].sum() + rashid_home['extras'].sum()
    econ_home = (total_runs / (len(rashid_home) / 6)) if not rashid_home.empty else 0
    
    print(f"🎡 Rashid Khan Economy (Ahmedabad):   {econ_home:.2f}")
    print("\nGT ANALYSIS: Ahmedabad favors high-SR batting over containment spin.")
    print("="*40)

else:
    print("❌ ERROR: No CSV files found. Ensure Cricsheet data is in the same folder.")
