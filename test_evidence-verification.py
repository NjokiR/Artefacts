from datetime import datetime

from modules.database import EvidenceDatabase 
from modules.integrity import IntegrityManager

# Create database and integrity manager 
database = EvidenceDatabase()
integrity = IntegrityManager()

# Retrieve stored evidence 
records = database.get_all_evidence()

print("\n--- EVIDENCE VERIFICATION TEST ---")

print("Number of stored records:", len(records))

# Check whether there are records 
if len(records) == 0:

    print("No evidence records found.")

else: 
    # Get the first stored record 
    record = records[0]

    message_id = record[0]
    user_id = record[1]
    timestamp = record[2]
    message = record[3]
    prediction = record[4]
    stored_hash = record[5]

    print("\nRetrieved evidence:")
    print("Message ID:", message_id)
    print("User ID:", user_id)
    print("Timestamp:", timestamp)
    print("Message:", message)
    print("prediction:", prediction)  
    print("Stored SHA-256:", stored_hash) 

    # Convert timestamp from SQLite string back to datetime
    timestamp = datetime.fromisoformat(timestamp)
    
    # Recreate the evidence dictionary
    evidence = {
        "message_id": message_id,
        "user_id": user_id,
        "timestamp": timestamp,
        "message": message,
        "prediction": prediction
    } 

    # Generate a new hash
    current_hash = integrity.generate_hash(evidence)

    print("\nCurrent SHA-256:", current_hash)

    # Compare hashes
    if current_hash == stored_hash:

        print("\nINTEGRITY CHECK: PASSED")
        print("Evidence has not been modified.")

    else:

        print("\nINTEGRITY CHECK: FAILED")
        print("Evidence may have been modified.")    