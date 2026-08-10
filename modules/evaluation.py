from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

class ModelEvaluator:
    def evaluate(self, y_true, y_pred):
        # Calculate classification performance metrics.

        accuracy = accuracy_score(y_true, y_pred)

        precision = precision_score(
            y_true,
            y_pred,
            average="weighted",
            zero_division=0
        )

        recall = recall_score(
            y_true,
            y_pred,
            average="weighted",
            zero_division=0
        )

        f1 = f1_score(
            y_true,
            y_pred,
            average="weighted",
            zero_division=0
        )

        return {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1_score": f1
        }

    def classification_report(self, y_true, y_pred):
        """
        Generate detailed performance results 
        for each cyberbullying category.
        """

        return classification_report(
            y_true,
            y_pred,
            zero_division=0
        )

    def confusion_matrix(self, y_true, y_pred):
        """
        Generate a confusion matrix showing
        correct and incorrect predictions.
        """

        return confusion_matrix(
            y_true,
            y_pred
        )    