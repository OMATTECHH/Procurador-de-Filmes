# sentiment_analysis.py
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Baixando os recursos necessários
nltk.download('vader_lexicon')

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)
    return sentiment_score

# Testando com uma avaliação de exemplo
review = "This movie was fantastic! The acting and the plot were amazing."
print(analyze_sentiment(review))  # Exibe a análise de sentimentos