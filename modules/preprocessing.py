import re
import pandas as pd

class TextPreprocessor:

    def clean_text(self, text):
        """
        Clean a single piece of text for machine-learning analysis.
        """

        # Convert to string 
        text = str(text)

        # Convert text to Lowercase 
        text = text.lower()

        # Remove URLs
        text = re.sub(r"http\S+|www\S+|https\S+", "", text)

        # Remove Twitter mentions 
        text = re.sub(r"@\w+", "", text)

        # Remove hashtag symbol but keep the word 
        text = re.sub(r"#", " ", text)

        # Remove punctuation and special characters 
        text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)

        # Remove extra whitespace 
        text = re.sub(r"\s+", " ", text).strip()

        return text
    def preprocess_dataset(self, df):
        """
        Create a cleaned text column while preserving 
        the original tweet_text column.
        """

        df = df.copy()

        df["cleaned_text"] = df["tweet_text"].apply(
            self.clean_text
        )    

        return df
