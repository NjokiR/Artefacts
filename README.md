# Cyberbullying Forensics System

A Python-based prototype that combines **machine-learning-based cyberbullying classification** with **digital forensic evidence preservation**.

The system accepts a social-media-style text message, classifies it into a cyberbullying category using a machine-learning model, and creates a forensic evidence record containing the message, metadata, timestamp, and a SHA-256 integrity hash.

---

## 1. Project Overview

The Cyberbullying Forensics System has two main components:

### Machine Learning Detection

The system uses:

* Text preprocessing
* TF-IDF feature extraction
* Logistic Regression classification
* Train/test evaluation
* Accuracy
* Precision
* Recall
* F1-score
* Classification report
* Confusion matrix

### Digital Forensic Evidence Preservation

For every message submitted for analysis, the system creates an evidence record containing:

* Message content
* Message ID
* User ID
* Timestamp
* Classification result
* SHA-256 hash

The evidence is stored in an SQLite database.

The SHA-256 hash provides an integrity mechanism that can be used to detect whether stored evidence has been modified.

---

## 2. System Workflow

The general processing workflow is:

```text
User enters message
        |
        v
Flask Web Application
        |
        v
Text Preprocessing
        |
        v
TF-IDF Feature Extraction
        |
        v
Logistic Regression Classifier
        |
        v
Cyberbullying Classification
        |
        +----------------------+
        |                      |
        v                      v
Forensic Evidence         Classification
Record Creation               Result
        |
        v
SHA-256 Hash Generation
        |
        v
SQLite Evidence Database
        |
        v
Results displayed to user
```

---

## 3. Cyberbullying Categories

The model currently predicts six categories:

```text
age
ethnicity
gender
not_cyberbullying
other_cyberbullying
religion
```

These categories are based on the labels contained in the training dataset.

---

## 4. Project Structure

```text
Artefacts/
│
├── app.py
├── config.py
├── train_model.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── cyberbullying_tweets.csv
│   └── evidence.db
│
├── models/
│   ├── classifier.pkl
│   └── tfidf.pkl
│
├── modules/
│   ├── classifier.py
│   ├── database.py
│   ├── data_loader.py
│   ├── evaluation.py
│   ├── feature_extraction.py
│   ├── forensic_logger.py
│   ├── integrity.py
│   └── preprocessing.py
│
├── templates/
│   ├── index.html
│   └── results.html
│
└── static/
    └── style.css
```

---

# 5. Getting the Code from GitHub

The project is hosted on GitHub under:

```text
NjokiR/Artefacts
```

A user can obtain the project by cloning the repository.

## Option 1: Clone using SSH

If GitHub SSH authentication has already been configured:

```prompt
git clone git@github.com:NjokiR/Artefacts.git
```

Then enter the project directory:

```prompt
cd Artefacts
```

## Option 2: Clone using HTTPS

If SSH has not been configured, HTTPS can be used:

```prompt
git clone https://github.com/NjokiR/Artefacts.git
```

Then enter the project directory:

```prompt
cd Artefacts
```

## Verify the Download

Run:

```prompt
git status
```

A newly cloned repository should display something similar to:

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

The project files can also be viewed with:

```bash
ls
```

The user should see files and directories such as:

```text
app.py
config.py
train_model.py
requirements.txt
README.md
data/
models/
modules/
templates/
static/
```

---

# 6. Technologies Used

The project uses:

* Python 3.10+
* Flask
* pandas
* NumPy
* scikit-learn
* joblib
* SQLite
* HTML
* CSS
* Git
* GitHub

---

# 7. Creating the Python Virtual Environment

After cloning the repository, create a virtual environment:

```prompt
python3 -m venv venv
```

Activate it on Linux or Ubuntu:

```prompt
source venv/bin/activate
```

---

# 8. Installing the Required Packages

With the virtual environment activated, install the project dependencies:

```prompt
pip install -r requirements.txt
```

This installs the Python packages required by the application and machine-learning components.

To verify the Python environment:

```prompt
python3 --version
```

---

# 9. Dataset

The system uses the **Cyberbullying Classification** dataset from Kaggle.

The expected dataset file is:

```text
data/cyberbullying_tweets.csv
```

The dataset contains two primary columns:

```text
tweet_text
cyberbullying_type
```

The current dataset contains approximately **47,692 records**.

The labels are:

```text
age
ethnicity
gender
not_cyberbullying
other_cyberbullying
religion
```

## Dataset Setup

After obtaining the dataset, make sure it is located at:

```text
data/cyberbullying_tweets.csv
```

The filename must match exactly because `train_model.py` expects:

```text
data/cyberbullying_tweets.csv
```

You can verify the file exists with:

```prompt
ls -lh data/cyberbullying_tweets.csv
```

---

# 10. Dataset Limitations

During development, the dataset was examined for duplicate and conflicting records.

The analysis found:

* Total records: **47,692**
* Unique tweet texts: **46,017**
* Texts with conflicting labels: **1,639**
* Total rows involved in conflicting-label duplicates: **3,278**

This means that some identical text appears with different classification labels.

The dataset also contains examples where a tweet discusses bullying without necessarily being an act of bullying itself.

For example, a tweet containing the word `bullying` does not automatically mean that the tweet is cyberbullying.

These characteristics can affect machine-learning performance.

Therefore, the model's prediction should be treated as an **automated classification result**, not as a guaranteed determination of whether a message constitutes cyberbullying.

---

# 11. Training the Machine-Learning Model

The complete training process is contained in:

```text
train_model.py
```

Run:

```prompt
python3 train_model.py
```

The training process performs the following steps:

1. Loads the dataset
2. Cleans the text
3. Creates cleaned text
4. Separates text and labels
5. Splits the data into training and testing sets
6. Fits the TF-IDF vectorizer using training data
7. Transforms the testing data
8. Trains the Logistic Regression classifier
9. Generates predictions
10. Calculates evaluation metrics
11. Generates a classification report
12. Generates a confusion matrix
13. Saves the trained classifier
14. Saves the trained TF-IDF vectorizer

The trained models are saved as:

```text
models/classifier.pkl
models/tfidf.pkl
```

---

# 12. Current Machine-Learning Configuration

The current feature extraction uses TF-IDF with:

```text
max_features = 10000
```

The classifier is:

```text
Logistic Regression
```

with:

```text
max_iter = 1000
```

The training process uses a reproducible train/test split.

The test set represents approximately 20% of the dataset.

---

# 13. Current Model Evaluation

The current trained model produced:

```text
Accuracy:  0.8382
Precision: 0.8430
Recall:    0.8382
F1-score:  0.8387
```

The classification performance was approximately:

| Category            | Precision | Recall | F1-score |
| ------------------- | --------: | -----: | -------: |
| age                 |      0.96 |   0.98 |     0.97 |
| ethnicity           |      0.97 |   0.98 |     0.97 |
| gender              |      0.92 |   0.82 |     0.87 |
| not_cyberbullying   |      0.62 |   0.55 |     0.58 |
| other_cyberbullying |      0.61 |   0.74 |     0.67 |
| religion            |      0.95 |   0.94 |     0.95 |

The model performs particularly well on:

* age
* ethnicity
* religion

The `not_cyberbullying` and `other_cyberbullying` categories are more difficult for the current model to distinguish.

Further investigation and improvement of these categories is part of the ongoing development of the project.

---

# 14. Running the Flask Application

Make sure the virtual environment is activated:

```prompt
source venv/bin/activate
```

Start the Flask application:

```prompt
python3 app.py
```

The application will start using the Flask development server.

Open the address shown by Flask in a web browser.

The home page provides a form where the user can enter a message for analysis.

---

# 15. Using the Web Interface

Once the Flask application is running:

1. Open the application in a web browser.
2. Enter a message in the text box.
3. Submit the message.
4. The message is sent to the `/predict` route.
5. The text is converted into TF-IDF features.
6. The trained classifier generates a prediction.
7. A forensic evidence record is created.
8. A SHA-256 hash is generated.
9. The evidence is stored in SQLite.
10. The results page displays the classification and forensic information.

---

# 16. Prediction Endpoint

The Flask application provides the following route:

```text
POST /predict
```

The route accepts a submitted message.

The application processes the message using the same trained TF-IDF vectorizer and classifier used by the application.

The results page displays:

* Message
* Prediction
* Message ID
* User ID
* Timestamp
* SHA-256 hash

---

# 17. Forensic Evidence

Each submitted message generates a forensic evidence record.

The evidence contains information such as:

```text
Message
Message ID
User ID
Timestamp
Prediction
```

The evidence is then hashed using SHA-256.

The general process is:

```text
Message
   |
   v
Evidence Record
   |
   v
SHA-256 Hash
   |
   v
SQLite Database
```

The hash provides a mechanism for checking whether the evidence has been modified after it was recorded.

---

# 18. SQLite Database

The forensic evidence is stored in:

```text
data/evidence.db
```

SQLite is used because it provides a lightweight structured database suitable for this prototype.

The database allows evidence records to be stored and retrieved while maintaining information such as:

* Message identifiers
* User identifiers
* Timestamps
* Predictions
* Hash values

---

# 19. Testing the Flask Application

## Test that Flask loads

With the virtual environment activated:

```prompt
python3 -c "from app import app; print('Flask application loaded successfully')"
```

Expected result:

```text
Flask application loaded successfully
```

## Test the home page

Run:

```prompt
python3 -c "from app import app; client=app.test_client(); response=client.get('/'); print('Status:', response.status_code); print('Content type:', response.content_type)"
```

Expected result:

```text
Status: 200
```

## Test a prediction

Run:

```prompt
python3 -c "from app import app; client=app.test_client(); response=client.post('/predict', data={'message':'You are stupid'}); print('Status:', response.status_code)"
```

Expected result:

```text
Status: 200
```

The returned page should contain:

* The submitted message
* A prediction
* Message ID
* User ID
* Timestamp
* SHA-256 hash

---

# 20. Testing Different Messages

Testers are encouraged to submit different types of messages, including:

### Non-bullying examples

```text
You are a wonderful person.
I hope you have a great day.
I disagree with your opinion.
Thank you for your help.
```

### Potentially abusive examples

```text
You are stupid.
I hate you.
You are an idiot.
Nobody likes you.
```

### Context-dependent examples

```text
People from that group are inferior.
Everyone is talking about bullying at school.
I disagree with what you said.
```

The purpose of these tests is to identify cases where the model's prediction does not match reasonable human interpretation.

Test results should be recorded for later model evaluation.

---

# 21. Important Model Limitation

The current model is a **statistical machine-learning classifier**.

It does not understand language in the same way a human does.

For example, TF-IDF represents text using numerical word and phrase features. Logistic Regression then uses those features to estimate which category is most likely.

Consequently, the model can sometimes produce unexpected predictions.

During development, examples such as the following were observed:

```text
"You are a wonderful person"
```

being classified as:

```text
other_cyberbullying
```

This does not necessarily mean that the model considers the message highly likely to be cyberbullying.

Prediction probabilities showed that some unexpected classifications were relatively low-confidence decisions.

The current model therefore requires further evaluation before being considered suitable for real-world deployment.

---

# 22. Current Development Status

## Completed

* Dataset loading
* Text preprocessing
* TF-IDF feature extraction
* Logistic Regression classifier
* Train/test evaluation
* Accuracy calculation
* Precision calculation
* Recall calculation
* F1-score calculation
* Classification report
* Confusion matrix
* Model persistence using joblib
* Flask web interface
* Message submission form
* Prediction route
* SQLite database
* Forensic evidence generation
* SHA-256 hashing
* Results page
* Git/GitHub integration

## Currently Under Review

* Classification quality
* `not_cyberbullying` performance
* `other_cyberbullying` performance
* Dataset duplicate records
* Conflicting labels
* Model confidence
* Feature selection
* Text preprocessing
* Possible improvements to the classification algorithm

---

# 23. Ethical and Security Considerations

This project is an educational and research prototype.

A production system would require additional safeguards, including:

* Protection of personally identifiable information
* Secure storage of forensic evidence
* Authentication and authorization
* Database access controls
* Secure Flask deployment
* Evidence retention policies
* Appropriate privacy protections
* Human review of automated classifications
* Proper digital-forensic procedures

The system should **not** be used as the sole basis for disciplinary, legal, employment, educational, or other high-impact decisions.

---

# 24. Testing by Other Users

People testing the system should record unexpected results using the following format:

```text
Message:
Expected category:
Actual category:
```

For example:

```text
Message:
You are a wonderful person.

Expected category:
not_cyberbullying

Actual category:
other_cyberbullying
```

Collecting these examples will help with future model evaluation and improvement.

---

# 25. Reproducing the Project

A new user can reproduce the project using the following general process:

```text
1. Clone the GitHub repository
        ↓
2. Enter the Artefacts directory
        ↓
3. Create a Python virtual environment
        ↓
4. Activate the virtual environment
        ↓
5. Install requirements.txt
        ↓
6. Obtain the dataset
        ↓
7. Place the dataset in data/
        ↓
8. Train the model
        ↓
9. Start the Flask application
        ↓
10. Open the application in a browser
        ↓
11. Submit messages for analysis
        ↓
12. Review predictions and forensic evidence
```

---

# 26. Project Purpose

The purpose of this project is to demonstrate the integration of:

* Machine learning
* Natural language processing
* Web application development
* SQLite databases
* Digital forensics
* Evidence integrity
* Model evaluation

The system demonstrates a complete workflow from text submission to classification and forensic evidence preservation.

The project is intended as a prototype for exploring how automated cyberbullying detection could be combined with forensic evidence handling.

---
