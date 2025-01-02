from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer  # type: ignore
from datasets import load_dataset # type: ignore
import pickle


class TextAnalyzer:
    """Class for text analysis using Hugging Face Transformers library"""
    
    def __init__(self, model_name):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
    
    @staticmethod
    def load_dataset(dataset_name: str):
        dataset = load_dataset(dataset_name)
        return dataset
    
    def tokenize_function(self, examples: load_dataset, tokenizer: AutoTokenizer):
        return self.tokenizer(examples["text"], padding="max_length", truncation=True)
    
    def train_model(self, model, tokenized_datasets):
        self.model = model
        
    def sentiment_analysis(self, texts: str):
        sentiment_pipeline = pipeline("sentiment-analysis", model=self.model, tokenizer=self.tokenizer)
        
        return sentiment_pipeline(texts)

    # def save_model(self, path: str):
    #     pickle.dump(self.model, open(path, "wb"))
        
# if __name__ == "__main__":
#     text_analyzer = TextAnalyzer(model_name="distilbert/distilbert-base-uncased-finetuned-sst-2-english")
#     dataset = TextAnalyzer.load_dataset("imdb")
#     print(type(text_analyzer))
    
#     # Example usage
#     result = text_analyzer.sentiment_analysis("I love this movie!")
#     print(result[0]['label'])
#     text_analyzer.save_model("data/model.pkl")