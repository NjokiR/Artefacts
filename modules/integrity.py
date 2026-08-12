import hashlib 

class IntegrityManager: 
    
    def generate_hash(self, evidence): 
        
        # Generate a SHA-256 hash for an evidence record.

        # Convert the evidence into a consistent string.
        evidence_string = (
            f"{evidence['message_id']}|"
            f"{evidence['user_id']}|"
            f"{evidence['timestamp']}|"
            f"{evidence['message']}|"
            f"{evidence['prediction']}"
        )

        # Generate SHA-256 hash

        hash_value = hashlib.sha256(
            evidence_string.encode("utf-8")
        ).hexdigest()

        return hash_value 

    def verify_hash(self, evidence, stored_hash):
        # Verify that evidence has not been modified. 

        current_hash = self.generate_hash(evidence)

        return current_hash == stored_hash   

