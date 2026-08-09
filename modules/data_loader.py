import pandas as pd 
import os

class DataLoader: 

    def load_dataset(self, file_path):

        if not os.path.exists(file_path):
            raise FileNotFoundError(
                f"Dataset not found: {file_path}"
            )
        df = pd.read_csv(file_path)

        return df    