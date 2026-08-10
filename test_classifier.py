import pandas as pd

from sklearn.model_selection import train_test_split

from modules.preprocessing import TextPreprocessor 
from modules.feature_extraction import FeatureExtractor
from modules.classifier import CyberbullyingClassifier
from modules.evaluation import ModelEvaluator

# Load data
df = pd.read_csv("data/cyberbullying_tweets.csv")

# Use a small sample for development
df =df.sample(
    n=1000,
    random_state=42
)

# Preprocess
preprocessor = TextPreprocessor()

df = preprocessor.preprocess_dataset(df)

# Separate features and Labels
x_text = df["cleaned_text"]
y = df["cyberbullying_type"]

# Split into training and testing data 
x_train_text, x_test_text, y_train, y_test = train_test_split(
    x_text, 
    y,
    test_size = 0.2, 
    random_state = 42,
    stratify = y
)

# Create TF-IDF extractor
extractor = FeatureExtractor()

# Fit TF-IDF Only on training data 
x_train = extractor.fit_transform(x_train_text)

# Transform test data using the existing vocabulary
x_test = extractor.transform(x_test_text)

# Creat classifier 
classifier = CyberbullyingClassifier()

# Train 
classifier.train(x_train, y_train)

# Predict
predictions = classifier.predict(x_test)

# Evaluate Model
evaluator = ModelEvaluator()

metrics = evaluator.evaluate(
    y_test,
    predictions
)

print("\n--- CLASSIFIER TEST ---")

print("Training records:", len(x_train_text))
print("Testing records:", len(x_test_text))

print("Number of predictions:", len(predictions))

print("\n--- PERFORMANCE METRICS ---")

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

print("\n--- CLASSIFICATION REPORT ---")

print(
    evaluator.classification_report(
        y_test,
        predictions
    )
)

print("\n--- CONFUSION MATRIX ---")

print(
    evaluator.confusion_matrix(
        y_test,
        predictions
    )
)

