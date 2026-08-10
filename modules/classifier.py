from sklearn.linear_model import LogisticRegression 

class CyberbullyingClassifier: 
    
    def __init__(self):
        self.model = LogisticRegression(
        max_iter=1000
        )
    
    def train(self, x_train, y_train):
        # Train the classifer using the training data.    
        self.model.fit(x_train, y_train)
    
    def predict(self, x_test):
        # Predict cyberbullying categories for new data.
        return self.model.predict(x_test)