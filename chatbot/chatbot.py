import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.corpus import stopwords
from nltk.classify import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
import json
import random

class SentimentChatBot:
    def __init__(self, sentiment_file, responses_file):
        self.responses = self.load_responses(responses_file)
        self.sentiment_classifier = self.train_sentiment_classifier(sentiment_file)

    def load_responses(self, file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    def load_sentiment_data(self, sentiment_file):
        with open(sentiment_file, 'r') as f:
            sentiment_data = json.load(f)
        return sentiment_data

    def preprocess_data(self, data):
        stop_words = set(stopwords.words('english'))
        processed_data = []
        
        for label, sentences in data.items():
            for sentence in sentences:
                words = word_tokenize(sentence.lower())
                filtered_words = [word for word in words if word.isalpha() and word not in stop_words]
                
                features = {word: True for word in filtered_words}
                
                processed_data.append((features, label))
        
        return processed_data

    def train_sentiment_classifier(self, sentiment_file):
        sentiment_data = self.load_sentiment_data(sentiment_file)
        processed_data = self.preprocess_data(sentiment_data)
        return NaiveBayesClassifier.train(processed_data)

    def analyze_sentiment(self, text):
        words = word_tokenize(text.lower())
        features = {word: True for word in words if word.isalpha()}
        return self.sentiment_classifier.classify(features)

    def get_response(self, user_input):
        sentiment = self.analyze_sentiment(user_input)
        responses = self.responses.get(sentiment, [])
        return random.choice(responses) if responses else "I'm not sure how to respond to that."

    def chat(self, user_input):
        if user_input.lower() in ['exit', 'bye', 'quit']:
            print("SentimentChatBot: Goodbye!")
        return self.get_response(user_input)