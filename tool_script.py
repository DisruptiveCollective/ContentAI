import requests
import os
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from textblob import TextBlob
import openai

# Function to check for existing API keys or prompt the user for them
def check_and_load_api_keys():
    env_file_path = ".env"
    keys = ["NEWS_API_KEY", "OPENAI_API_KEY"]

    if os.path.isfile(env_file_path):
        load_dotenv(env_file_path)
        if all(key in os.environ for key in keys):
            return {key: os.getenv(key) for key in keys}
    
    with open(env_file_path, "w") as env_file:
        for key in keys:
            value = input(f"Enter your {key}: ")
            os.environ[key] = value
            env_file.write(f"{key}={value}
")
    
    return {key: os.getenv(key) for key in keys}

# Placeholder for other functions (fetch_trending_topics, generate_content, etc.)

def main():
    api_keys = check_and_load_api_keys()
    # ... rest of your script logic ...

if __name__ == "__main__":
    main()
