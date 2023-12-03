from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def cosine_similarity(sentence1: str, sentence2: str):
    # Tokenize and convert sentences to vectors
    vectorizer = CountVectorizer().fit_transform([sentence1, sentence2])
    vectors = vectorizer.toarray()

    # Calculate cosine similarity
    similarity = cosine_similarity([vectors[0]], [vectors[1]])[0, 0]

    return similarity


