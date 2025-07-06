import fastf1
import pandas as pd
import logging
from pathlib import Path
import os

logging.basicConfig(level=logging.INFO)
print("FastF1 Script Started!")

# ✅ Auto-create cache folder (Absolute Path)
cache_dir = Path(__file__).resolve().parents[2] / 'cache'
os.makedirs(cache_dir, exist_ok=True)
fastf1.Cache.enable_cache(str(cache_dir))

def fetch_race_laps(year, gp_name, session_type):
    print(f"Fetching race laps for {year} {gp_name} {session_type}")
    session = fastf1.get_session(year, gp_name, session_type)
    print("Loading session data...")
    session.load()

    print("Fetching laps...")
    laps = session.laps

    laps_csv_path = Path(__file__).resolve().parents[2] / 'data' / f'laps_{year}_{gp_name}_{session_type}.csv'
    laps.to_csv(laps_csv_path, index=False)

    print(f"Saved laps data to {laps_csv_path}")
    print(laps.head())

if __name__ == "__main__":
    print("Running main...")
    fetch_race_laps(2023, 'Bahrain', 'R')
