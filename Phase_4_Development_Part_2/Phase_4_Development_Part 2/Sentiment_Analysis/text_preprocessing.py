import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Sample text data for preprocessing
sample_text = "This is a sample text for text preprocessing. It includes removing punctuation and stopwords."

# Function to preprocess text data
def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = re.sub(f"[{re.escape(string.punctuation)}]", '', text)
    
    # Tokenize the text
    words = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    
    # Join the processed words back into a single string
    processed_text = ' '.join(words)
    
    return processed_text

# Preprocess the sample text
preprocessed_text = preprocess_text(sample_text)

# Print the preprocessed text
print("Sample Text:", sample_text)
print("Preprocessed Text:", preprocessed_text)
