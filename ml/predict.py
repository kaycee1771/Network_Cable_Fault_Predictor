'''import joblib
import pandas as pd
import os

MODEL_PATH = "models/cable_fault_predictor.pkl"

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model not found at {MODEL_PATH}")
    return joblib.load(MODEL_PATH)

def prepare_input(snmp_snapshot):
    """
    Input: A list of dicts like:
    [
        {
            'device': 'switch_1',
            'interface': 'eth1',
            'in_octets': 123456,
            'out_octets': 234567,
            'in_errors': 10,
            'out_errors': 2,
            'speed': 1000000000,
            'delta_in_errors': 1,
            'delta_out_errors': 0
        },
        ...
    ]
    Output: pandas DataFrame ready for model
    """
    df = pd.DataFrame(snmp_snapshot)

    required_features = [
        "in_octets", "out_octets",
        "in_errors", "out_errors",
        "delta_in_errors", "delta_out_errors",
        "speed"
    ]

    if not all(f in df.columns for f in required_features):
        raise ValueError(f"Missing one or more required features: {required_features}")

    return df[required_features], df[["device", "interface"]]

def predict(snapshot):
    model = load_model()
    X, meta = prepare_input(snapshot)
    predictions = model.predict(X)
    meta["prediction"] = predictions
    return meta.to_dict(orient="records")

# Example Usage (mock snapshot)
if __name__ == "__main__":
    fake_data = [
        {
            'device': 'switch_1', 'interface': 'eth1',
            'in_octets': 500000, 'out_octets': 600000,
            'in_errors': 10, 'out_errors': 5,
            'speed': 1000000000,
            'delta_in_errors': 12, 'delta_out_errors': 0
        },
        {
            'device': 'switch_1', 'interface': 'eth2',
            'in_octets': 100000, 'out_octets': 80000,
            'in_errors': 2, 'out_errors': 1,
            'speed': 1000000000,
            'delta_in_errors': 0, 'delta_out_errors': 1
        }
    ]
    results = predict(fake_data)
    for r in results:
        print(f"{r['device']} {r['interface']} → {'⚠️ FAULT' if r['prediction'] else '✅ OK'}")'''
