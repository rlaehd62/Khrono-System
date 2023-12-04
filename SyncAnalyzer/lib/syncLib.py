from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np, math

def calculate_similarity(sentence1: str, sentence2: str):
    
    print("Calculating Similarity")
    print(sentence1)
    print(sentence2)
    
    # Tokenize and convert sentences to vectors
    vectorizer = CountVectorizer().fit_transform([sentence1, sentence2])
    vectors = vectorizer.toarray()

    # Calculate cosine similarity
    similarity = cosine_similarity([vectors[0]], [vectors[1]])[0, 0]
    print(similarity, "\n")
    
    return round(similarity, 3)


