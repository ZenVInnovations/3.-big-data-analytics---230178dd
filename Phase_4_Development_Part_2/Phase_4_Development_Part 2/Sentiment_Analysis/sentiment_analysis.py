import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize the SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

# Sample text data for sentiment analysis
sample_text = "I love this product! It's amazing and works perfectly."

# Analyze the sentiment of the sample text
sentiment_scores = sid.polarity_scores(sample_text)

# Determine sentiment based on the compound score
if sentiment_scores['compound'] >= 0.05:
    sentiment = "Positive"
elif sentiment_scores['compound'] <= -0.05:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

# Print the sentiment analysis results
print("Sample Text:", sample_text)
print("Sentiment: ", sentiment)
print("Sentiment Scores (Positive, Neutral, Negative):", sentiment_scores)
