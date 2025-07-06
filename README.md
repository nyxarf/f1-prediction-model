#  F1 Race Lap Time Prediction Model

This project is a full pipeline to predict F1 race lap times using machine learning.  
It automatically collects race data, preprocesses it, and trains ML models for lap time prediction.

---

##  Project Pipeline:
1. **Data Collection:**  
   Auto-fetches race lap data from FastF1 API for all races in a season.
   
2. **Dataset Combination:**  
   Combines all race CSV files into a master dataset.

3. **Preprocessing:**  
   Cleans data, encodes categorical variables, prepares ML-ready CSV.

4. **ML Model Training:**  
   Trains a Random Forest Regressor to predict lap times using race features.


##  Tech Stack:
- Python 
- FastF1 API (for F1 data)
- Pandas & Scikit-learn (for ML)
- Random Forest Regressor (ML Model)

---

##  How To Run:
1. Clone this repo:
```bash
git clone https://github.com/nyxarf/f1-prediction-model.git
cd f1-prediction-model
```

then:
```bash
pip install -r requirements.txt
 Run pipeline: # Fetch races
python src/data_collection/fetch_all_races.py

# Combine races
python src/data_collection/combine_race_laps.py

# Preprocess data
python src/data_collection/preprocess_ml_data.py

# Train ML model
python src/data_collection/train_ml_model.py
```

Future Plans:
Improve ML models (XGBoost, Deep Learning)

Predict Final Race Results

Interactive Dashboard

Integrate Real-Time Inference

Author: Arfa Ahmed Ansari
Currently working on improving accuracy and further training.

PS: ChatGPT helped me to structure this project. Structure will be optimized in future.
