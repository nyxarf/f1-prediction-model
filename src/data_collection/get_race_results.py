import requests
import pandas as pd
from pathlib import Path
import fastf1
fastf1.Cache.enable_cache('cache')  # This creates a 'cache/' folder to store fetched data

def fetch_race_results(season):
    """Fetch race results for a specific season from Ergast API."""
    all_results = []

    # Ergast API: Most seasons have ~20-24 races
    for round_num in range(1, 30):  
        url = f"http://ergast.com/api/f1/{season}/{round_num}/results.json"
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to fetch Round {round_num} - Status Code:", response.status_code)
            continue

        data = response.json()
        races = data['MRData']['RaceTable']['Races']
        if not races:
            continue  # Skip if no race data

        race = races[0]
        race_name = race['raceName']
        circuit = race['Circuit']['circuitName']
        date = race['date']

        for result in race['Results']:
            position = int(result['position'])
            driver = result['Driver']
            constructor = result['Constructor']
            driver_name = f"{driver['givenName']} {driver['familyName']}"
            constructor_name = constructor['name']
            grid = int(result['grid'])
            status = result['status']

            all_results.append({
                'Season': season,
                'Round': round_num,
                'Race': race_name,
                'Circuit': circuit,
                'Date': date,
                'Position': position,
                'Driver': driver_name,
                'Constructor': constructor_name,
                'Grid': grid,
                'Status': status
            })

    return pd.DataFrame(all_results)

if __name__ == "__main__":
    # Fetch Data
    season = 2023  # Change year if needed
    df = fetch_race_results(season)
    
    # Print preview
    print(df.head())

    # Save CSV
    output_path = Path(__file__).resolve().parents[2] / 'data' / f'f1_race_results_{season}.csv'
    df.to_csv(output_path, index=False)
    print(f"\nSaved race results to {output_path}")
    df.to_csv("D:/F1 PREDICTION MODEL/data/f1_race_results_2023.csv", index=False)
    print("Saved successfully!")
