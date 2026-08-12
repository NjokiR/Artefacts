from flask import Flask, request, jsonify
import joblib

from modules.data_loader import DataLoader
from modules.forensic_logger import ForensicLogger
from modules.integrity import IntegrityManager
from modules.database import EvidenceDatabase

app = Flask (__name__)

# Create Dataloader Object
loader = DataLoader()

# Create forensic evidence components

logger = ForensicLogger()
integrity = IntegrityManager()
database = EvidenceDatabase()

# Location of the dataset
DATASET_PATH = "data/cyberbullying_tweets.csv"

# LOAD SAVED MACHINE LEARNING MODELS

CLASSIFIER_PATH = "models/classifier.pkl"
TFIDF_PATH = "models/tfidf.pkl"

classifier = joblib.load(CLASSIFIER_PATH)
tfidf = joblib.load(TFIDF_PATH)

# HOME ROUTE

@app.route("/")
def home():
    # Load the dataset
    df = loader.load_dataset(DATASET_PATH)

    # Basic dataset information
    rows = len(df)
    columns = df.columns.tolist()

    return{
        "message": "Cyberbullying Forensics System",
        "rows": rows,
        "columns": columns
    }

# PREDICTION ROUTE

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    message = data.get("message", "")

    if not message:
        return jsonify({
            "error": "Message is required"
        }), 400

    # Convert message into TF-IDF features
    features = tfidf.transform([message])

    # Make prediction
    prediction = classifier.predict(features)[0]

    # Create forensic evidence record
    evidence = logger.create_evidence_record(
        message = message,
        prediction = prediction
    )

    # Generate SHA-256 hash for the evidence
    hash_value = integrity.generate_hash(evidence)

    #store evidence and hash in SQLite database
    database.insert_evidence(
        evidence,
        hash_value
    )

    # Return prediction and forensic evidence informaion
    return jsonify({
        "message": evidence["message"],
        "prediction": evidence["prediction"],
        "message_id": evidence["message_id"],
        "user_id": evidence["user_id"],
        "timestamp": str(evidence["timestamp"]),
        "hash_value": hash_value
    })

# RUN APPLICATION

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)