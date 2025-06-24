
# ⚡ AI-Based Network Cable Fault Predictor

**🔌 Predict Cable Failures Before They Happen — with AI, SNMP, and Real Hardware Metrics**

This project leverages **machine learning** to proactively detect **network cable degradation** in lab or enterprise environments by analyzing SNMP-collected metrics like error rates and traffic flow. Designed to work with real hardware (e.g., Cisco/Juniper/Huawei switches), this solution demonstrates predictive operations and intelligent observability — a step beyond traditional monitoring.

---

## 🔍 Features

### ✅ Current Working Features

- **📡 SNMP Poller** – Periodically queries switch port stats (e.g., octets, errors, speed)
- **🧠 ML Model (Random Forest)** – Predicts degradation based on port error rates
- **📊 Runtime Monitor** – Logs prediction results continuously with timestamp and status
- **🧪 Synthetic Training Data Generator** – Auto-generates labeled data for model training
- **🧱 Modular Architecture** – Easy to extend or integrate with alerting/visualization systems

---

## 🚀 Getting Started

### 1. Clone & Setup Virtual Environment

```bash
git clone https://github.com/YOUR_USERNAME/cable-fault-predictor.git
cd cable-fault-predictor

python -m venv cable-env
# Windows
cable-env\Scripts\activate
# macOS/Linux
source cable-env/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Monitor

```bash
python monitor/run_monitor.py
```

---

## 🧠 How It Works

1. **Poll SNMP Switch Ports** every 30 seconds for:
   - `in_octets`, `out_octets` (traffic)
   - `in_errors`, `out_errors` (signal degradation)
   - `ifSpeed` (bandwidth baseline)

2. **Feed Metrics into ML Classifier** to classify each port's cable as:
   - ✅ **Healthy**
   - ⚠️ **Degrading**
   - ❌ **Critical**

3. **Log Results to CSV** for dashboards or further training.

---

## 🛠 Technologies Used

- **Python 3.12**
- **pysnmp** – For SNMP polling
- **scikit-learn** – For ML training/inference
- **pandas** – Data processing
- **csv / logging** – Log handling

---

## 🧪 Sample Output

```json
{
  "timestamp": "2025-06-23T21:53:01",
  "device": "switch_1",
  "interface": "eth2",
  "in_octets": 32050,
  "out_octets": 67736,
  "in_errors": 3,
  "out_errors": 4,
  "speed": 1000000000,
  "status": "⚠️ Degrading"
}
```

---

## 🔮 Upcoming Features

### ✅ Self-Learning Auto-Tuner (Online ML)
A model to continuously retrain on real data as it observes new traffic patterns or degradation.

### 🔭 Trend-Based Degradation Forecasting
Use time-series prediction (e.g., LSTM or Prophet) to predict future error rates from traffic trends.

### 📊 Port Behavior Fingerprinting (Zero-Day Cables)
Profile the normal behavior of each port and raise flags on unusual patterns, even with no prior label.
