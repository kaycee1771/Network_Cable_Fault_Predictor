
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

### ✅ Self-Updating Model from Field Logs  
A system that automatically retrains itself on historical logs and real-world behavior to improve accuracy over time. This creates a true **feedback loop**.

### 🔭 Time-to-Failure Prediction  
Using a **regression model** to estimate “⏳ time remaining before failure,” enabling **preventive** maintenance, not just reactive classification.

### 📊 Real-Time Grafana Dashboard  
Push cable health data to **Grafana + Prometheus** or **Plotly Dash**, for real-time visualization of interface health, historical trends, and model confidence.

### 🧬 Entropy + Signal Pattern Analysis  
Go beyond simple error counters by computing **entropy scores** of signal patterns over time to detect **early signs of fraying or physical wear** — like zero-day detection for cables.
