from setuptools import setup

setup(
    name="sentiment_intent_predictor",
    version="0.1",
    description="Sentiment and Intent Predictor using Hugging Face Transformers",
    packages=["src"],
    install_requires=[
        "transformers==4.11.3",
        "configparser==5.0.2",
    ],
)
