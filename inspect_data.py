import pandas as pd 

# Load the dataset
df = pd.read_csv("data/cyberbullying_tweets.csv")

print("\n--- FIRST 5 ROWS ----")
print(df.head())

print("\n--- DATASET SHAPE ---")
print(df.shape)

print("\n--- COLUMNs NAMES ---")
print(df.columns.tolist())

print("\n--- COLUMNS NAMES ---")
print(df.columns.tolist())

print("\n--- DATA TYPES ---")
print(df.dtypes)

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- DUPLICATE ROWS ---")
print(df.duplicated().sum())

print("\n--- CLASS DISTRIBUTION ---")
print(df["cyberbullying_type"].value_counts())

print("\n-- TEXT LENGTH STATISTICS ---")

text_lengths = df["tweet_text"].astype(str).str.len()

print("Shortest tweet:", text_lengths.min())
print("Longest tweet:", text_lengths.max())
print("Average tweet length:", round(text_lengths.mean(), 2))

print("\n--- EMPTY OR WHITESPACE-ONLY TWEETS ---")

empty_tweets = (
    df["tweet_text"]
    .astype(str)
    .str.strip()
    .eq("")
    .sum()
)

print("Empty tweets:", empty_tweets)

print("\n--- DUPLICATE TEXT ---")

duplicate_text = df["tweet_text"].duplicated().sum()

print("Duplicate tweet text:", duplicate_text)

print ("\n--- DUPLICATE TEXT WITH DIFFERENT LABELS ---")

duplicate_label_check =(
    df.groupby("tweet_text")["cyberbullying_type"]
    .nunique()
)

conflicting_duplicates = duplicate_label_check[
    duplicate_label_check > 1
]

print(
    "Tweets with conflicting lables:", 
    len(conflicting_duplicates)
)

print("\n--- DUPLICATE TEXT ANALYSIS ---")

text_counts = df["tweet_text"].value_counts()

duplicate_texts = text_counts[text_counts > 1]

print("Repeated tweet texts:", len(duplicate_texts))

duplicate_label_counts = (
    df[df["tweet_text"].isin(duplicate_texts.index)]
    .groupby("tweet_text")["cyberbullying_type"]
    .nunique()
)

same_label_duplicates = (
    duplicate_label_counts[duplicate_label_counts == 1]
)

conflicting_label_duplicates = (
    duplicate_label_counts[duplicate_label_counts > 1]
)

print(
    "Repeated texts with same label:", 
    len(same_label_duplicates)
)

print(
    "Repeated texts with conflicting labels:", 
    len(conflicting_label_duplicates)
)
