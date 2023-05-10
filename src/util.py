import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer

# Regular expression for matching URLs
URL_REGEX = re.compile(
    r"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})"
)

# Regular expression for matching email addresses
EMAIL_REGEX = re.compile(
    r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
)

# Regular expression for matching phone numbers
PHONE_REGEX = re.compile(
    r"\+?[0-9\s-]{8,}"
)

# List of stop words to remove from text
STOPWORDS = set(stopwords.words("english"))

# Stemming algorithm to use
STEMMER = PorterStemmer()

def preprocess_text(text):
    """
    Preprocesses text data by removing URLs, email addresses, phone numbers,
    punctuation, stop words, and applying stemming.

    Args:
        text (str): The text data to preprocess.

    Returns:
        str: The preprocessed text.
    """
    # Convert to lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(URL_REGEX, "", text)

    # Remove email addresses
    text = re.sub(EMAIL_REGEX, "", text)

    # Remove phone numbers
    text = re.sub(PHONE_REGEX, "", text)

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Tokenize text into words
    words = nltk.word_tokenize(text)

    # Remove stop words
    words = [word for word in words if word not in STOPWORDS]

    # Apply stemming
    words = [STEMMER.stem(word) for word in words]

    # Rejoin words into a single string
    text = " ".join(words)

    return text

def create_tfidf_vectorizer(data, max_features=5000):
    """
    Creates a TF-IDF vectorizer for the given data.

    Args:
        data (list): A list of strings representing the data to vectorize.
        max_features (int): The maximum number of features to use in the vectorizer.

    Returns:
        TfidfVectorizer: The TF-IDF vectorizer.
    """
    vectorizer = TfidfVectorizer(
        max_features=max_features,
        ngram_range=(1, 2),
        stop_words="english"
    )
    vectorizer.fit(data)
    return vectorizer
