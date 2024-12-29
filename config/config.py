import os
from dotenv import load_dotenv

load_dotenv()

# Model settings
MODEL_NAME = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"
MAX_LENGTH = 512

# API keys (if needed)
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# Paths
MODEL_SAVE_PATH = "data/model.pkl"
