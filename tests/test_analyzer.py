import unittest
from src.utils.text_analyzer import TextAnalyzer
import pickle

class TestTextAnalyzer(unittest.TestCase):
    """Test cases for the TextAnalyzer class"""
    def setUp(self):
        self.text_analyzer = TextAnalyzer(model_name="distilbert/distilbert-base-uncased-finetuned-sst-2-english")
    
    def test_sentiment_analysis(self):
        result1 = self.text_analyzer.sentiment_analysis("I love this movie!")
        result2 = self.text_analyzer.sentiment_analysis("I hate this movie!")
        self.assertEqual(result1[0]['label'], 'POSITIVE')
        self.assertEqual(result2[0]['label'], 'NEGATIVE')
        
        
    def test_save_model(self):
        self.text_analyzer.save_model("data/model.pkl")
        with open("data/model.pkl", "rb") as f:
            model = pickle.load(f)
        self.assertIsNotNone(model)
        
    def test_load_dataset(self):
        dataset = TextAnalyzer.load_dataset("imdb")
        self.assertIsNotNone(dataset)
        
    def test_tokenize_function(self):
        examples = TextAnalyzer.load_dataset("imdb")
        tokenized_datasets = self.text_analyzer.tokenize_function(examples, self.text_analyzer.tokenizer)
        self.assertIsNotNone(tokenized_datasets)
        
if __name__ == "__main__":
    unittest.main()
# Run the tests using the following command:
# python -m tests.test_analyzer
