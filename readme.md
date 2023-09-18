# Sentiment and Intent Predictor

## Overview
This project is a Python application that uses a pre-trained language model to perform sentiment analysis and intent prediction on user-provided text. It allows you to analyze the sentiment of the text as positive, negative, or neutral and predict the intent behind the text, such as "change_package," "upgrade," or "cancel_service."

## Project Structure
The codebase is organized into the following directories:

- `src`: Contains the Python source code for the Sentiment and Intent Predictor.
- `config`: Holds model configurations, preferably in .ini format but also supports .yaml.
- `data`: Contains simulation data created with ChatGPT for testing and validation.
- `resources`: Stores the pre-trained zero-shot model. You can use the Hugging Face zero-shot model, such as `facebook/bart`.

## Features
- Sentiment Analysis: Analyzes the sentiment (positive, negative, or neutral) of the input text.
- Intent Prediction: Predicts the intent (e.g., change_package, upgrade, cancel_service) behind the input text.
- Customizable Labels: You can customize the sentiment and intent labels by editing the `model_config.ini` configuration file.
- Integration with Java: The project includes a Java class (`TextSentimentIntentAnalyzer`) that allows you to call the Python script from Java and display the output.

## Requirements
- Python 3.x
- Java Development Kit (JDK)

## Setting Up a Virtual Environment (PyCharm)

1. Open the project in PyCharm.

2. Create a virtual environment:
   - Click on "File" > "Settings" (or "PyCharm" > "Preferences" on macOS).
   - In the left sidebar, navigate to "Python Interpreter."
   - Click the gear icon and select "Add..."
   - Choose "Virtual Environment" and select your preferred location for the virtual environment directory.
   - Select a base interpreter (Python 3.x) and click "OK."

3. Install the required packages:
   - In the "Python Interpreter" settings, click the "+" button to add packages.
   - Search for and install the following packages:
     - `torch` (PyTorch)
     - `transformers` (Hugging Face Transformers)
     - `configparser` (usually included with Python)

## Installation
You can install this project as a Python package using `setuptools`. Follow the steps below to set up the project:

1. Clone the repository to your local machine.

2. Customize the labels in the `model_config.ini` file to match your specific use case.

   ```ini
   [SENTIMENT]
   sentiment_labels = positive, negative, neutral

   [INTENT]
   intent_labels = change_package, upgrade, cancel_service
