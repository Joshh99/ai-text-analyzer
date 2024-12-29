# Setup Instructions

1. Clone the repository:
git clone https://github.com/Joshh99/ai-text-analyzer.git
cd ai-text-analyzer

2. Create a virtual environment:
python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate


3. Install dependencies:
pip install -r requirements.txt

4. Set up environment variables:
Create a `.env` file in the root directory and add:
HUGGINGFACE_API_KEY=your_api_key_here

5. Run the Streamlit app:
streamlit run src/app.py

6. Run tests:
python -m unittest discover tests