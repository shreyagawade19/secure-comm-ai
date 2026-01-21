🛡️ AI-Based Secure Communication Monitoring System
📌 Overview

This project implements an AI-powered secure communication system that preserves end-to-end encryption while using machine learning–based anomaly detection to monitor communication behavior in real time.

Instead of analyzing message content, the system observes network traffic metadata (such as packet duration, size, and TTL) to detect unusual or potentially malicious communication behavior, making it suitable for defense and critical infrastructure applications.

🎯 Key Objectives

Preserve data confidentiality using encryption

Detect abnormal communication behavior using AI

Prevent replay attacks, spoofed traffic, and anomalous patterns

Provide a real-time interactive dashboard

Ensure privacy-preserving security monitoring

🔐 Core Idea (In Simple Terms)

Messages are fully encrypted.
AI does not read the message.
AI only checks how the communication behaves.

If the behavior looks normal → communication allowed
If the behavior looks abnormal → communication blocked

🧠 Technologies Used

Python

Streamlit – Interactive dashboard

Scikit-learn – Machine learning

Isolation Forest – Anomaly detection

AES Encryption – Secure data transmission

Joblib – Model persistence

🧪 Machine Learning Details

Algorithm: Isolation Forest (unsupervised anomaly detection)

Training Dataset: UNSW-NB15 (network intrusion dataset)

Features Used:

Packet duration (dur)

Source bytes (sbytes)

Destination bytes (dbytes)

Time-to-live (sttl)

The model is trained to learn normal communication patterns and flag deviations as anomalies.

📊 Dashboard Features

Real-time message encryption & transmission

AI-based decision: Normal / Suspicious

Visualization of packet metadata used by AI

Automatic blocking of suspicious communication

Secure decryption only for trusted communication

🗂️ Project Structure
Secure_Comm_AI_Defense/
│
├── ai_model/
│   ├── anomaly_model.py
│   ├── anomaly_model.pkl
│
├── encryption/
│   ├── aes_encrypt.py
│
├── dashboard/
│   └── monitor.py
│
├── sender/
│   └── sender.py
│
├── receiver/
│   └── receiver.py
│
├── requirements.txt
├── README.md
└── .gitignore

▶️ How to Run Locally
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run the Streamlit dashboard
streamlit run dashboard/monitor.py

🌍 Deployment

This project is deployed using Streamlit Community Cloud, making it accessible as a real-time web application without any local setup.

🔒 Dataset Notice

Large training datasets (e.g., network_logs.csv) are intentionally excluded from this repository and kept locally to maintain repository cleanliness and comply with GitHub file size limits.

Dataset source used for training:

UNSW-NB15 Network Intrusion Dataset

🧩 Use Cases

Secure military communications

Satellite telemetry monitoring

Defense command-and-control systems

Encrypted IoT networks

Critical infrastructure communication security

🏆 Key Highlights

✔ End-to-end encryption preserved
✔ AI works without inspecting message content
✔ Behavior-based anomaly detection
✔ Real-time interactive dashboard
✔ Deployment-ready architecture

📌 Future Enhancements

Attack simulation toggles

Traffic history visualization

Explainable AI scores

Role-based access control

Integration with real network streams

👤 Author

Shreya Gawade
Computer Engineering | AI/ML Enthusiast
Focus: Defense, Security & Intelligent Systems

📜 License

This project is for academic and research purposes only.