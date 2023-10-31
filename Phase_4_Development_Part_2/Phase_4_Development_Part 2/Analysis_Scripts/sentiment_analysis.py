# Import necessary libraries
from textblob import TextBlob

# Load your text data
text_data ="The growth of big data in recent years has been astounding. It's transforming industries,enabling data-driven decision-making, and opening up new opportunities for businesses. However, managing and analyzing big data can be challenging due to its volume, velocity, and variety. Tools and techniques for big data analytics are crucial for harnessing its potential"


# Sentiment Analysis
blob = TextBlob(text_data)
sentiment = blob.sentiment

# Print the sentiment scores
print("Sentiment Polarity:", sentiment.polarity)
print("Sentiment Subjectivity:", sentiment.subjectivity)

