import kagglehub 
import shutil
import os

# Download Kaggle dataset
path = kagglehub.dataset_download("andrewmvd/cyberbullying-classification")

print("Dataset download to:")
print(path)

# List downloaded files 
print("\nFiles available:")

for file in os.listdir(path):
    print(file)
    