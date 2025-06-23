import sqlite3
import pandas as pd
import os
import numpy as np

DB_PATH = "data/snmp_poll_data.db"
OUTPUT_PATH = "data/processed/features.csv"

def load_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM snmp_stats", conn)
    conn.close()
    return df

def compute_features(df, window_size=5):
    # Sort and index
    df = df.sort_values(by=["device", "interface", "timestamp"])
    df.set_index("timestamp", inplace=True)

    feature_rows = []
    for (device, iface), group in df.groupby(["device", "interface"]):
        group = group.rolling(window=window_size, min_periods=1).mean().dropna()

        group["delta_in_errors"] = group["in_errors"].diff().fillna(0)
        group["delta_out_errors"] = group["out_errors"].diff().fillna(0)

        group["device"] = device
        group["interface"] = iface

        feature_rows.append(group)

    features = pd.concat(feature_rows)
    features.reset_index(inplace=True)
    return features

def generate_labels(df):
    """
    If errors increase rapidly in a window → label as degrading (1)
    Otherwise → label as healthy (0)
    """
    df["label"] = np.where(
        (df["delta_in_errors"] > 10) | (df["delta_out_errors"] > 10), 1, 0
    )
    return df

def save_features(df):
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"[✔] Saved features to {OUTPUT_PATH}")

def run_pipeline():
    df = load_data()
    print(f"[📊] Loaded {len(df)} rows from DB")
    df_feat = compute_features(df)
    df_labeled = generate_labels(df_feat)
    save_features(df_labeled)

if __name__ == "__main__":
    run_pipeline()
