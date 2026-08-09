import pandas as pd 
from modules.preprocessing import TextPreprocessor

# Load a small sample of the dataset 
df = pd.read_csv("data/cyberbullying_tweets.csv")

sample = df.head(5)

# Create preprocessor 
preprocessor = TextPreprocessor()

# Process sample 
processed = preprocessor.preprocess_dataset(sample)

print("\n--- ORIGINAL AND CLEANED TEXT ---")

print(
    processed[
        ["tweet_text", "cleaned_text","cyberbullying_type"]
    ].to_string(index=False)
)