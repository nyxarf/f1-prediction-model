import pandas as pd
from pathlib import Path
from sklearn.preprocessing import LabelEncoder

def preprocess_dataset(year):
    data_dir = Path(__file__).resolve().parents[2] / 'data'
    input_file = data_dir / f'f1_combined_laps_{year}.csv'
    output_file = data_dir / f'f1_preprocessed_laps_{year}.csv'
    
    # Load dataset
    df = pd.read_csv(input_file)
    print(f"Loaded dataset: {input_file}")
    print(f"Initial shape: {df.shape}")
    
    # Example: Select Relevant Columns (You can expand this later)
    columns_to_keep = [
        'DriverNumber', 'LapNumber', 'Stint',
        'Compound', 'LapTime', 'TrackStatus',
        'IsPersonalBest', 'RaceName'
    ]
    available_cols = [col for col in columns_to_keep if col in df.columns]
    df = df[available_cols]
    
    # Convert LapTime from string to seconds (if applicable)
    if 'LapTime' in df.columns:
        df['LapTime'] = pd.to_timedelta(df['LapTime'], errors='coerce').dt.total_seconds()
    
    # Encode categorical variables
    for col in ['Compound', 'RaceName', 'TrackStatus']:
        if col in df.columns:
            encoder = LabelEncoder()
            df[col] = encoder.fit_transform(df[col].astype(str))
    
    # Drop NaNs (Optional - adjust for your needs)
    df = df.dropna()
    
    # Save preprocessed dataset
    df.to_csv(output_file, index=False)
    print(f"\n✅ Preprocessed dataset saved at: {output_file}")
    print(f"Final shape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")

if __name__ == "__main__":
    preprocess_dataset(2023)
