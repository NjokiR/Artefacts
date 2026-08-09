from flask import Flask 
from modules.data_loader import DataLoader

app = Flask (__name__)

# Create Dataloader Object
loader = DataLoader()

# Location of the dataset 
DATASET_PATH = "data/cyberbullying_tweets.csv"


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
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)    