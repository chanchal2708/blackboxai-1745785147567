from transformers import pipeline

# Load sentiment-analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_speech_content(text):
    """
    Analyze speech content using NLP techniques.

    Parameters:
    - text: str, transcribed speech text

    Returns:
    - features: dict, extracted NLP features such as sentiment
    """
    features = {}

    # Sentiment analysis
    result = sentiment_analyzer(text)[0]
    features['sentiment_label'] = result['label']
    features['sentiment_score'] = result['score']

    return features
