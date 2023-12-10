from sentence_transformers import SentenceTransformer, util


model = SentenceTransformer('snunlp/KR-SBERT-V40K-klueNLI-augSTS')
def calculate_similarity(sentence1: str, sentence2: str):
    
    embeddings1 = model.encode([sentence1], convert_to_tensor=True)
    embeddings2 = model.encode([sentence2], convert_to_tensor=True)
    
    cosine_scores = util.cos_sim(embeddings1, embeddings2)
    print(f"{sentence1} vs {sentence2} : {cosine_scores[0][0]:0.4f}")
    
    return cosine_scores[0][0]