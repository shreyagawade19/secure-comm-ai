import sys
from pathlib import Path

# Add project root to Python path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

import streamlit as st
import random

from encryption.aes_encrypt import generate_key, encrypt_data, decrypt_data
from ai_model.anomaly_model import detect

st.set_page_config(page_title="Secure Comm AI Dashboard", layout="centered")

st.title("🛡️ AI-Based Secure Communication Dashboard")
st.markdown("Defense-oriented secure communication monitoring system")

st.divider()

# Input message
message = st.text_input(
    "📡 Enter message to transmit",
    "Secure military telemetry data"
)

if st.button("🔐 Send Secure Message"):

    # Encryption
    key = generate_key()
    encrypted_msg = encrypt_data(message, key)

    # Metadata (must match training features)
    packet_features = [
        random.uniform(0.1, 1),        # dur
        len(encrypted_msg),            # sbytes
        len(encrypted_msg) * 0.8,      # dbytes
        64                              # sttl
    ]

    status = detect(packet_features)

    st.subheader("📊 AI Analysis Result")

    st.write("**Packet Features Used:**")
    st.json({
        "Duration (dur)": packet_features[0],
        "Source Bytes (sbytes)": packet_features[1],
        "Destination Bytes (dbytes)": packet_features[2],
        "TTL (sttl)": packet_features[3]
    })

    if "Normal" in status:
        st.success("✅ Communication is NORMAL")

        decrypted_msg = decrypt_data(encrypted_msg, key)
        st.subheader("🔓 Decrypted Message")
        st.code(decrypted_msg)

    else:
        st.error("🚨 SUSPICIOUS communication detected!")
        st.warning("Message blocked for security reasons")

st.divider()
st.caption("AI monitors encrypted traffic behavior without inspecting payload data")
