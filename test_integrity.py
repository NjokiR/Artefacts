from modules.forensic_logger import ForensicLogger
from modules.integrity import IntegrityManager

# Create forensic evidence 
logger = ForensicLogger()

evidence = logger.create_evidence_record(
    message = "This is a test message",
    prediction = "not_cyberbullying"
)

# Create integrity manager 
integrity = IntegrityManager()

# Generate SHA-256 hash
hash_value = integrity.generate_hash(evidence)

print("\n---INTEGRITY ---")

print("Evidence:")
print(evidence)

print("\nSHA-256 Hash:")
print(hash_value)

print("\n---VERIFY ORIGINAL EVIDENCE ---")

result = integrity.verify_hash(
    evidence,
    hash_value
)

print("Hash verification:", result)

# Test whether a modification is detected 
evidence["message"] = "This message has been modified"

print("\n---VERIFY MODIFIED EVIDENCE ---")

result = integrity.verify_hash(
    evidence, 
    hash_value
)

print("Hash verification:", result)
