import pandas as pd
from pathlib import Path

def combine_laps_data(year):
    data_dir = Path(__file__).resolve().parents[2] / 'data'
    output_file = data_dir / f'f1_combined_laps_{year}.csv'
    
    # Find all lap CSV files for the year
    all_files = list(data_dir.glob(f"laps_{year}_*_R.csv"))
    print(f"Found {len(all_files)} race files for {year}")
    
    # Combine them
    df_list = []
    for file in all_files:
        try:
            df = pd.read_csv(file)
            # Add Race Name as a new column
            race_name = file.stem.replace(f"laps_{year}_", "").replace("_R", "").replace("_", " ")
            df['RaceName'] = race_name
            df_list.append(df)
            print(f"Loaded {file.name} with {len(df)} laps")
        except Exception as e:
            print(f"Failed to load {file}: {e}")

    # Merge into one DataFrame
    combined_df = pd.concat(df_list, ignore_index=True)
    
    # Save to single CSV
    combined_df.to_csv(output_file, index=False)
    print(f"\n✅ Combined dataset saved at: {output_file}")
    print(f"Shape: {combined_df.shape}")
    print(f"Columns: {combined_df.columns.tolist()}")

if __name__ == "__main__":
    combine_laps_data(2023)
