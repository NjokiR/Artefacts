import pandas as pd 

from modules.preprocessing import TextPreprocessor
from modules.feature_extraction import FeatureExtractor

# Load the dataset
df = pd.read_csv("data/cyberbullying_tweets.csv")

# Use a small sample for testing 
sample = df.head(100)

# Preprocess the text 
preprocessor = TextPreprocessor()

processed = preprocessor.preprocess_dataset(sample)

# Create the feature extractor 
extractor = FeatureExtractor()

# Convert cleaned text into TF-IDF features
X = extractor.fit_transform(
    processed["cleaned_text"]
)

print("\n--- TF-IDF TEST---")

print("Original records:", len(sample))

print("TF-IDF matriix shape:", X.shape)

print("Number of features:", X.shape[1])