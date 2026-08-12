from modules.forensic_logger import ForensicLogger
from modules.integrity import IntegrityManager
from modules.database import EvidenceDatabase 

# Create evidence 

logger = ForensicLogger()

evidence = logger.create_evidence_record(
    message = "This is a database test message",
    prediction = "not_cyberbullying"
)

# Generate SHA-256 hash

integrity = IntegrityManager()

hash_value = integrity.generate_hash(
    evidence
)

# Save evidence to database 

database = EvidenceDatabase()

database.insert_evidence(
    evidence, 
    hash_value
)

# Retrieve evidence 

records = database.get_all_evidence()

print("\n--- DATABASE TEST ---")

print("Number of evidence records:", len(records))

print("\nStored evidence:")

for record in records: 
    print(record)