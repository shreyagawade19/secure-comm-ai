import pandas as pd
import joblib
from sklearn.ensemble import IsolationForest
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

def train_model():
    data_file = DATA_DIR / "network_logs.csv"

    if not data_file.exists():
        raise FileNotFoundError(
            "network_logs.csv not found. "
            "Run feature_extraction.py first."
        )

    # Load cleaned data
    df = pd.read_csv(data_file)

    # Train Isolation Forest
    model = IsolationForest(
        contamination=0.1,
        random_state=42
    )
    model.fit(df)

    # Save trained model
    model_path = Path(__file__).parent / "anomaly_model.pkl"
    joblib.dump(model, model_path)

    print("✅ Anomaly detection model trained successfully")
    print(f"✅ Model saved at: {model_path}")

def detect(packet_features):
    model_path = Path(__file__).parent / "anomaly_model.pkl"
    model = joblib.load(model_path)
    result = model.predict([packet_features])
    return "⚠️ Suspicious" if result[0] == -1 else "✅ Normal"

if __name__ == "__main__":
    train_model()
