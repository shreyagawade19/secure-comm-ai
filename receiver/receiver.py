from encryption.aes_encrypt import decrypt_data
from sender.sender import encrypted_msg, key, status

print("📥 Encrypted message received")

if "Normal" in status:
    decrypted_message = decrypt_data(encrypted_msg, key)
    print("🔓 Decrypted message:", decrypted_message)
else:
    print("🚨 ALERT: Suspicious communication blocked!")
