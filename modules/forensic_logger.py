import uuid 
from datetime import datetime 

class ForensicLogger: 

    def create_evidence_record(
        self, 
        message, 
        prediction, 
        user_id=None 
    ):

        """
        create a forensic evidence record. 
        parameters: 
            message: The original message text. 
            prediction: The ML classification result. 
            user_id; Optional user identifier. 

        Returns: 
            A dictionary containing the evidence metadata. 
        """        
        # Generate a unique evidence/message ID
        message_id = str(uuid.uuid4())

        # Generate a user ID if one was not supplied 
        if user_id is None:
            user_id = f"USER-{uuid.uuid4().hex[:8]}"

        # Record the time the evidence was processed 
        timestamp = datetime.now()

        # Create the evidence record
        evidence = {
            "message_id": message_id, 
            "user_id": user_id, 
            "timestamp": timestamp, 
            "message": message, 
            "prediction": prediction
        }
    
        return evidence   


