from flask import Flask, request, jsonify
import joblib

from modules.data_loader import DataLoader

app = Flask (__name__)

# Create Dataloader Object
loader = DataLoader()

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

    return jsonify({
        "message": message,
        "prediction": prediction
    })    

# RUN APPLICATION

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)    