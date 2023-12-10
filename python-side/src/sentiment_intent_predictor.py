import os
import sys
import configparser
from transformers import pipeline


class SentimentIntentPredictor:
    def __init__(self):
        self.model_name = "facebook/bart-large-mnli"
        self.pipeline = pipeline("zero-shot-classification", model=self.model_name)

    def load_labels(self, section_name):
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(__file__), "../config/model_config.ini"))
        # config.read("../config/model_config.ini")
        labels = config[section_name]["sentiment_labels"] if section_name == "SENTIMENT" else config[section_name][
            "intent_labels"]
        return labels.split(", ")

    def predict_sentiment(self, text):
        sentiment_labels = self.load_labels("SENTIMENT")
        result = self.pipeline(text, sentiment_labels)
        sentiment = result["labels"][0]
        return sentiment

    def predict_intent(self, text):
        intent_labels = self.load_labels("INTENT")
        result = self.pipeline(text, intent_labels)
        intent = result["labels"][0]
        return intent


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python SentimentIntentPredictor.py <text_input>")
        sys.exit(1)

    text = sys.argv[1]

    predictor = SentimentIntentPredictor()

    sentiment = predictor.predict_sentiment(text)
    intent = predictor.predict_intent(text)

    print(f"Sentiment: {sentiment}")
    print(f"Intent: {intent}")
