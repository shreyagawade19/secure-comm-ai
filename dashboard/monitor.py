# ===============================
# Streamlit Dashboard
# AI-Based Secure Communication
# ===============================

import sys
from pathlib import Path
import random
import streamlit as st

# --- Fix Python path for Streamlit Cloud ---
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

# --- Project imports ---
from encryption.aes_encrypt import generate_key, encrypt_data, decrypt_data
from ai_model.anomaly_model import detect


# ===============================
# Streamlit Page Config
# ===============================
st.set_page_config(
    page_title="AI-Based Secure Communication",
    layout="centered"
)

st.title("🛡️ AI-Based Secure Communication Dashboard")
st.caption("Defense-oriented secure communication monitoring system")

st.divider()

# ===============================
# Session State (History)
# ===============================
if "history" not in st.session_state:
    st.session_state.history = []

# ===============================
# User Inputs
# ===============================
st.subheader("📨 Message Payload (Encrypted)")
message = st.text_input(
    "Enter message to transmit",
    "Secure military telemetry data"
)

st.subheader("📡 Communication Behavior Simulation")

traffic_mode = st.radio(
    "Select traffic behavior (simulation)",
    [
        "Normal Communication",
        "Repetitive / Replay-like Pattern",
        "High-Volume Traffic Spike"
    ]
)

st.info(
    "ℹ️ Message content is never analyzed by AI. "
    "Only communication behavior (metadata) is evaluated."
)

# ===============================
# Send Button
# ===============================
if st.button("🔐 Send Secure Message"):

    # --- Encrypt message ---
    key = generate_key()
    encrypted_msg = encrypt_data(message, key)

    # --- Generate packet features based on behavior ---
    if traffic_mode == "Normal Communication":
        packet_features = [
            0.6,     # duration
            120,     # source bytes
            100,     # destination bytes
            64       # TTL
        ]

    elif traffic_mode == "Repetitive / Replay-like Pattern":
        packet_features = [
            0.05,
            300,
            300,
            64
        ]

    else:  # High-Volume Traffic Spike
        packet_features = [
            2.5,
            5000,
            4800,
            255
        ]

    # --- AI Decision ---
    status = detect(packet_features)

    # ===============================
    # AI Analysis Output
    # ===============================
    st.subheader("📊 AI Analysis Result")

    st.write("**Packet Features Used (Metadata):**")
    st.json({
        "Duration (dur)": packet_features[0],
        "Source Bytes (sbytes)": packet_features[1],
        "Destination Bytes (dbytes)": packet_features[2],
        "TTL (sttl)": packet_features[3]
    })

    st.subheader("🧠 AI Reasoning")

    if "Normal" in status:
        st.success("✅ AI Decision: Communication Allowed")
        st.write(
            "✔ Traffic behavior closely matches learned normal patterns."
        )

        decrypted_msg = decrypt_data(encrypted_msg, key)
        st.subheader("🔓 Decrypted Message")
        st.code(decrypted_msg)

    else:
        st.error("🚨 AI Decision: Suspicious Communication Detected")
        st.write(
            "⚠ Traffic behavior deviates significantly from learned normal patterns."
        )
        st.warning(
            "Message blocked for security review. "
            "In real systems, this would trigger secondary verification."
        )

    # ===============================
    # Update History
    # ===============================
    st.session_state.history.append({
        "Message": message,
        "Traffic Pattern": traffic_mode,
        "AI Decision": "Allowed" if "Normal" in status else "Blocked"
    })

# ===============================
# Communication History
# ===============================
if st.session_state.history:
    st.divider()
    st.subheader("📈 Communication History (Current Session)")
    st.table(st.session_state.history)

st.divider()

st.caption(
    "🔒 This system prioritizes security over convenience. "
    "Anomaly detection is intentionally conservative."
)
