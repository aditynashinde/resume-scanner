"""
Text Preprocessing Module
"""

def preprocess_text(text):

    """Clean, tokenize, and normalize text using nltk."""
    import nltk
    import string
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize

    # Download resources if not already present
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords')

    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    tokens = [w.lower() for w in tokens if w.isalpha()]
    filtered = [w for w in tokens if w not in stop_words]
    return filtered
