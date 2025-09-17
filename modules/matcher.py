"""
Keyword Matching & Scoring Module
"""

# TODO: Install and import scikit-learn, pandas
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# import pandas as pd


def match_keywords(jd_keywords, resume_tokens):
    """Count keyword matches and return matched/missing keywords."""
    jd_set = set([kw.lower() for kw in jd_keywords])
    resume_set = set([tok.lower() for tok in resume_tokens])
    matched = list(jd_set & resume_set)
    missing = list(jd_set - resume_set)
    return matched, missing


def compute_similarity_score(jd_text, resume_text):
    """Compute TF-IDF cosine similarity score between JD and resume."""
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    corpus = [jd_text, resume_text]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return score
