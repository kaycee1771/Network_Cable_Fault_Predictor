import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

# Ensure the model directory exists
os.makedirs("models", exist_ok=True)

# Load training data
df = pd.read_csv("data/cable_fault_dataset.csv")

# Ensure correct types
df = df[["in_octets", "out_octets", "in_errors", "out_errors", "speed", "label"]]
df["label"] = df["label"].astype(str)

# Prepare features and labels
X = df.drop("label", axis=1)
y = df["label"]

# Split and train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save trained model
joblib.dump(model, "models/cable_fault_predictor.pkl")

print("[MODEL] Training complete. Model saved to models/cable_fault_predictor.pkl")
