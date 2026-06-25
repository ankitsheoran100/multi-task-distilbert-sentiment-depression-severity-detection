import os
import subprocess

def download_dataset():
    # Install kaggle if not installed
    subprocess.run(["pip", "install", "kaggle"], check=True)
    
    # Create data folder
    os.makedirs("data", exist_ok=True)
    
    # Download the dataset
    subprocess.run([
        "kaggle", "datasets", "download",
        "-d", "nikhileswarkomati/suicide-watch",
        "--path", "./data",
        "--unzip"
    ], check=True)
    
    print("✅ Dataset downloaded successfully to ./data/")

if __name__ == "__main__":
    download_dataset()
