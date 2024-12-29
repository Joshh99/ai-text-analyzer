# AI Text Analysis Dashboard

This Streamlit application analyzes text using OpenAI's API.

## Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate` (On Windows: `venv\Scripts\activate`)
4. Install dependencies: `pip install -r requirements.txt`
5. Set your OpenAI API key: `export OPENAI_API_KEY='your-api-key-here'`
6. Run the application: `streamlit run src/app.py`

## Features

- Sentiment Analysis

## Usage

1. Enter your text in the input area
2. Click "Analyze" to see the results



---------------------------
git checkout -b feature/ui-development
git add src/app.py
git commit -m "Implement basic Streamlit interface"

git checkout -b feature/openai-integration
git add src/openai_utils.py src/text_analyzer.py
git commit -m "Implement OpenAI API integration and text analysis functions"

git add README.md
git commit -m "Update README with setup instructions"

git push origin feature/ui-development
git push origin feature/openai-integration
