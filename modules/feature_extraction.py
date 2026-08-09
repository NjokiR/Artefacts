from sklearn.feature_extraction.text import TfidfVectorizer

class FeatureExtractor:

    def __init__(self):
        self.vectorizer = TfidfVectorizer(
            max_features = 5000
        )

    def fit_transform(self, texts): 
        """
        Learn the vocabulary and transform text
        into TF-IDF numerical features.
        """

        return self.vectorizer.fit_transform(texts)

    def transform(self, texts):
        """
        Transform new text using the vocabulary
        already learned during training.
        """
        return self.vectorizer.transform(texts)       