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
    all_valid = True

    for record in records:

        message_id = record[0]
        user_id = record[1]
        timestamp = record[2]
        message = record[3]
        prediction = record[4]
        stored_hash = record[5]
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

        current_hash = integrity.generate_hash(evidence)

        # Generate a new hash
        print("\nMessage ID:", message_id)
        print("Stored SHA-256:", stored_hash)
        print("Current SHA-256:", current_hash)


        if integrity.verify_hash(evidence, stored_hash):

            print("INTEGRITY CHECK: PASSED")

        else:

            print("INTEGRITY CHECK: FAILED")
            all_valid = False

    print("\n---FINAL RESULT ----")

    if all_valid:
        print("All evidence records passed integrity verification.")
    else:
        print("One or more evidence records failed integrity verifiction")
