import os
import requests
import schedule
import time
from git import Repo
from datetime import datetime

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  
# GitHub token from environment variable
GITHUB_USERNAME = "github_username"
REPO_NAME = "repo_name"

# Local repo directory
REPO_DIR = "/path/to/your/repo"

# Function to generate code
def generate_code():
    # For simplicity, we're writing a basic Python script
    code = f"""
# Auto-generated code by GitHub Bot on {datetime.now().strftime('%Y-%m-%d')}
def say_hello():
    print("Hello, world!")

if __name__ == "__main__":
    say_hello()
"""
    return code

# Function to commit and push code
def commit_and_push():
    # Generate the code
    code = generate_code()
    
    # Save the code to a file
    file_path = os.path.join(REPO_DIR, "auto_generated_code.py")
    with open(file_path, "w") as f:
        f.write(code)
    
    # Initialize the repo
    repo = Repo(REPO_DIR)
    repo.git.add(file_path)
    
    # Commit the code
    commit_message = f"Auto-generated code on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    repo.index.commit(commit_message)
    
    # Push the code to the remote repository
    origin = repo.remote(name='origin')
    origin.push()

    print("Code committed and pushed successfully.")

# Function to run the bot daily
def run_daily():
    print("Running the GitHub bot...")
    commit_and_push()

# Schedule the bot to run daily at a specific time, e.g., 09:00 AM
schedule.every().day.at("09:00").do(run_daily)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
