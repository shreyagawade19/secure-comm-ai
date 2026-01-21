from encryption.aes_encrypt import generate_key, encrypt_data
from ai_model.anomaly_model import detect
import random

# Generate key
key = generate_key()

message = "Secure military telemetry data"
encrypted_msg = encrypt_data(message, key)

# Extract metadata ONLY (no content)
packet_features = [
    random.uniform(0.1, 1),        # dur
    len(encrypted_msg),            # sbytes
    len(encrypted_msg) * 0.8,      # dbytes (simulated)
    64                             # sttl
]

status = detect(packet_features)

print("📤 Encrypted message sent")
print("🤖 AI Status:", status)
