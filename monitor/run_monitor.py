import requests
import joblib
import time
import os
import csv
import pandas as pd
from datetime import datetime

model = joblib.load("ml/cable_fault_model.pkl")

DEVICES = [
    {"name": "switch_1", "interfaces": ["eth1", "eth2"]}
]

LOG_PATH = "logs/monitor_log.csv"
os.makedirs("logs", exist_ok=True)

# Create header if file doesn't exist
if not os.path.exists(LOG_PATH):
    with open(LOG_PATH, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "timestamp", "device", "interface",
            "in_octets", "out_octets", "in_errors", "out_errors", "speed", "status"
        ])

def predict_fault(data):
    input_df = pd.DataFrame([{
        "in_octets": data["in_octets"],
        "out_octets": data["out_octets"],
        "in_errors": data["in_errors"],
        "out_errors": data["out_errors"],
        "speed": data["speed"]
    }])
    return model.predict(input_df)[0]

def monitor():
    while True:
        timestamp = datetime.now().isoformat(timespec='seconds')

        for device in DEVICES:
            for iface in device["interfaces"]:
                try:
                    response = requests.get("http://localhost:8000", timeout=5)
                    snmp = response.json()
                    prediction = predict_fault(snmp)
                    status = "⚠️ Degrading" if prediction == 1 else "✅ Healthy"

                    log_row = [
                        timestamp,
                        device["name"],
                        iface,
                        snmp["in_octets"],
                        snmp["out_octets"],
                        snmp["in_errors"],
                        snmp["out_errors"],
                        snmp["speed"],
                        status
                    ]

                    print(dict(zip([
                        "timestamp", "device", "interface",
                        "in_octets", "out_octets",
                        "in_errors", "out_errors",
                        "speed", "status"
                    ], log_row)))

                    with open(LOG_PATH, mode="a", newline="", encoding="utf-8") as f:
                        writer = csv.writer(f)
                        writer.writerow(log_row)

                except Exception as e:
                    print(f"[ERROR] Failed {device['name']}:{iface} - {e}")

        time.sleep(30)

if __name__ == "__main__":
    monitor()
