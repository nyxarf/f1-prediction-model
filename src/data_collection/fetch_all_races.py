import fastf1
from pathlib import Path
import pandas as pd
import os

# Setup cache (auto-create)
cache_dir = Path(__file__).resolve().parents[2] / 'cache'
os.makedirs(cache_dir, exist_ok=True)
fastf1.Cache.enable_cache(str(cache_dir))

def fetch_race_laps(year, gp_name, session_type):
    print(f"Fetching {session_type} data for {gp_name} {year}")
    session = fastf1.get_session(year, gp_name, session_type)
    session.load()
    laps = session.laps

    # File path
    safe_gp_name = gp_name.replace(' ', '_')
    laps_csv_path = Path(__file__).resolve().parents[2] / 'data' / f"laps_{year}_{safe_gp_name}_{session_type}.csv"


    # Save CSV
    laps.to_csv(laps_csv_path, index=False)
    print(f"Saved laps to {laps_csv_path}")

def fetch_all_races(year):
    schedule = fastf1.get_event_schedule(year)
    for _, event in schedule.iterrows():
        gp_name = event['EventName']
        try:
            fetch_race_laps(year, gp_name, 'R')  # Race session
        except Exception as e:
            print(f"Failed for {gp_name}: {e}")

if __name__ == "__main__":
    fetch_all_races(2023)

