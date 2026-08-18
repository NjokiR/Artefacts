import pandas as pd 
import joblib

from sklearn.model_selection import train_test_split, GroupShuffleSplit

from modules.preprocessing import TextPreprocessor
from modules.feature_extraction import FeatureExtractor
from modules.classifier import CyberbullyingClassifier
from modules.evaluation import ModelEvaluator 

# 1. Load the complete dataset 

print("\n--- LOADING DATASET ---")

df = pd.read_csv("data/cyberbullying_tweets.csv")

print("Total records:", len(df))

# 2. Preprocessing the text

print("\n--- PREPROCESSING ---")

preprocessor = TextPreprocessor()

df = preprocessor.preprocess_dataset(df)

print("Preprocessing completed.")

# 3. Separate text and labels

x_text = df["cleaned_text"]

y = df["cyberbullying_type"]

# 4. Split into training and testing data 

print("\n--- TRAIN/TEST SPLIT ---")

splitter = GroupShuffleSplit(
    n_splits = 1,
    test_size = 0.2,
    random_state = 42
)
train_idx, test_idx = next(
    splitter.split(
        x_text,
        y,
        groups = df["tweet_text"]
    )
 )

x_train_text = x_text.iloc[train_idx]
x_test_text = x_text.iloc[test_idx]

y_train = y.iloc[train_idx]
y_test = y.iloc[test_idx]

print("Training records:", len(x_train_text))
print("Testing records:", len(x_test_text))

# 5. TF-IDF feature extraction

print("\n--- TF-IDF ---")

extractor = FeatureExtractor()

# IMPORTANT:
# Fir TF-IDF Only on training data

x_train = extractor.fit_transform(
    x_train_text
)

# Transform test data using the 
# vocabulary learned from training data

x_test = extractor.transform(
    x_test_text
)

print("Training TF-IDF shape;", x_train.shape)
print("Testing TF-IDF shape:", x_test.shape)

#. Train classifier 

print("\n--- TRAINING CLASSIFIER---")

classifier = CyberbullyingClassifier()

classifier.train(
    x_train,
    y_train
)

print("Classifier training completed.")

# 7. Make predictions

print("\n--- PREDICTIONS ---")

predictions = classifier.predict(
    x_test
)

print("Predictins generated:", len(predictions))

# 8. Evaluate Model

print("\n--- MODEL EVALUATION ---")

evaluator = ModelEvaluator()

metrics = evaluator.evaluate(
    y_test,
    predictions
)

print(
    "Accuracy:", 
    round(metrics["accuracy"], 4)
)

print(
    "Precision:", 
    round(metrics["precision"], 4)
)

print(
    "Recall:", 
    round(metrics["recall"], 4)
)

print(
    "F1_score:", 
    round(metrics["f1_score"], 4)
)

print("\n---CLSSIFICATION REPORT ----")

print(
    evaluator.classification_report(
        y_test,
        predictions
    )
)

print("\n---CONFUSION MATRIX ---")

print(
    evaluator.confusion_matrix(
        y_test, 
        predictions
    )
)

# 9. Save trained models

print("\n--- SAVING MODELS ---")

joblib.dump(
    classifier.model,
    "models/classifier.pkl"
)

joblib.dump(
    extractor.vectorizer, 
    "models/tfidf.pkl"
)

print("Classifier saved to models/clssifier.pkl")
print("TF-IDF vectorizer saved to models/tfidf.pkl")

print("\n--- TRAINING COMPLETE ---")