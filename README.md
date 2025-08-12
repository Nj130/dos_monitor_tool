# 🛡️🤖DoS Attack Detection Tool

🚀 Real-time defense against Distributed Denial of Service attacks using Machine Learning + Network Flow Analysis.

🔍 How It Works
1️⃣ 📡 Data Collection – Gather NetFlow/sFlow/IPFIX data from routers & switches
2️⃣ ⚙️ Feature Extraction – Compute traffic patterns (📈 bytes/sec, 🌍 unique IPs, 🔁 handshake rates)
3️⃣ 🧠 AI Model – Classify or detect anomalies using 🤖 ML algorithms
4️⃣ 🚨 Alert & Mitigation – Trigger 🔔 alerts or automatically block 🚫 suspicious sources

# 🧩 Features
📊 Real-time network monitoring
🧠 Supervised + Unsupervised ML models
🛠️ Supports CIC-DDoS2019 dataset for training
📡 NetFlow / Zeek log support
⚡ Low-latency detection for early response
🛠️ Tech Stack
🐍 Python for data processing & modeling
📦 scikit-learn / XGBoost / PyTorch for ML
📡 nfdump / pmacct / Zeek for flow collection
📊 Grafana / Kibana for dashboards

## Installation
```bash
git clone https://github.com/Nj130/dos_monitor_tool
cd dos_monitor_tool
pip install -r requirements.txt
