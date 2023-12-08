from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np, math

def calculate_similarity(sentence1: str, sentence2: str):
    
    print("Calculating Similarity")
    print(sentence1)
    print(sentence2)
    
    vectors = TfidfVectorizer().fit_transform([sentence1, sentence2])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    
    print(similarity, "\n")
    return similarity

