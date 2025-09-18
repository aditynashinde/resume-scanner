"""
Text Preprocessing Module
"""

def preprocess_text(text):

    """Clean, tokenize, and normalize text using nltk."""
    import nltk
    import string
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize

    # Ensure punkt and stopwords are downloaded
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt', quiet=True)
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords', quiet=True)

    try:
        stop_words = set(stopwords.words('english'))
        tokens = word_tokenize(text)
        tokens = [w.lower() for w in tokens if w.isalpha()]
        filtered = [w for w in tokens if w not in stop_words]
        return filtered
    except LookupError as e:
        print("Error: Required NLTK resource not found. Please run the following in a Python shell:")
        print("import nltk; nltk.download('punkt'); nltk.download('stopwords')")
        raise e
