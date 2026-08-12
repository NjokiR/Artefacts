from modules.forensic_logger import ForensicLogger

logger = ForensicLogger()

evidence = logger.create_evidence_record(
    message = "This is a test message", 
    prediction = "not_cyberbullying"
)

print("\n--- FORENSIC LOGGER TEST ---")

print("Message ID:", evidence["message_id"])
print("User ID:", evidence["user_id"])
print("Timestamp:", evidence["timestamp"])
print("Message:", evidence["message"])
print("Prediction:", evidence["prediction"])