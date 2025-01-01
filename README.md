# chatbot_python

This project implements a chatbot that classifies user input into various emotional sentiments and responds with an appropriate message based on the sentiment. The chatbot uses Natural Language Processing (NLP) techniques to detect sentiments and provide dynamic responses based on pre-trained data.

## Folder Structure

The project structure is as follows:

```
chatbot/
│
├── data/
│   ├── responses.json   # Predefined responses for various sentiments
│   └── sentiment_data.json # Sentiment training data for the chatbot
│
├── chatbot/
│   └── chatbot.py       # Core chatbot logic
│
└── app.py               # FastAPI app for handling HTTP requests
```

- **`data/`**: Contains JSON files (`responses.json` and `sentiment_data.json`) that store predefined chatbot responses and sentiment data for training the sentiment classifier.
- **`chatbot/`**: Contains the `chatbot.py` file, which includes the logic for training the sentiment classifier, preprocessing data, and generating responses.
- **`app.py`**: The main FastAPI application that exposes an HTTP endpoint for interacting with the chatbot.

## Installation

### Prerequisites

Ensure that you have the following installed:

- Python 3.7 or later
- `pip` (Python package installer)

### Steps

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/sentiment-chatbot.git
   cd sentiment-chatbot
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/MacOS
   venv\Scripts\activate     # For Windows
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   If you don't have a `requirements.txt` file, install the dependencies manually:

   ```bash
   pip install fastapi uvicorn nltk
   ```

   - `fastapi`: For building the web API
   - `uvicorn`: ASGI server to run the FastAPI app
   - `nltk`: For natural language processing tasks, including sentiment analysis

4. Download the necessary NLTK resources:

   Inside a Python shell, run:

   ```python
   import nltk
   nltk.download('stopwords')
   nltk.download('punkt')
   ```

## Usage


### With the Next.js integration

The app.py file contains commented code that you can use if you want to integrate it with your Next.js site or React site.

```bash
uvicorn app:app --reload
#run this and then test it on your front end.
```



### Running the FastAPI Server

To start the FastAPI server, run the following command:

```bash
uvicorn app:app --reload
```

This will start a development server on `http://127.0.0.1:8000`. The `--reload` flag enables auto-reloading during development.

### Endpoints

**POST `/chat/`**: Send a message to the chatbot and receive a response based on the sentiment of the message.

**Request Body (JSON):**

```json
{
  "message": "Your input message here"
}
```

**Response (JSON):**

```json
{
  "response": "Chatbot's response based on sentiment"
}
```

Example using `curl`:

```bash
curl -X 'POST' \
     'http://127.0.0.1:8000/chat/' \
     -H 'Content-Type: application/json' \
     -d '{"message": "I'm feeling great!"}'
```

**Response:**

```json
{
  "response": "I'm so glad you're feeling good!"
}
```

### Testing

You can also test the API using tools like Postman or your browser.

## Project Files

- **`chatbot/chatbot.py`**: This file contains the `SentimentChatBot` class which does the following:
  - Preprocesses the sentiment data
  - Trains the sentiment classifier using Naive Bayes
  - Analyzes sentiment in user input
  - Provides an appropriate response based on sentiment classification

- **`data/responses.json`**: This file contains predefined responses for various sentiments. Each sentiment (e.g., "positive", "anger", "greetings") has a list of responses that the chatbot can randomly choose from.

- **`data/sentiment_data.json`**: This file contains labeled sentiment data used to train the sentiment classifier. Each sentiment label (e.g., "positive", "negative", "anger") has a list of sample sentences.

## Contributing

Feel free to fork this repository, submit issues, or create pull requests. Contributions are welcome!
