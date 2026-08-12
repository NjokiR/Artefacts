import joblib

print("\n--- LOADING SAVED MODELS---")

classifier = joblib.load("models/classifier.pkl")
tfidf = joblib.load("models/tfidf.pkl")

print("Classifier loaded successfully.")
print("TF-IDF vectorizer loaded successfully.")

print("\nClassifier type:", type(classifier))
print("TF-IDF type:", type(tfidf))

print("\n--- MODEL LOADING TEST PASSED ---")


