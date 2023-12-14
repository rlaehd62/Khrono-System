from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('snunlp/KR-SBERT-V40K-klueNLI-augSTS')
def calculate_similarity(sentences1: str, sentences2: str):
    
    list1 = sentences1.split()
    list2 = sentences2.split()
    
    embeddings1 = model.encode(list1)
    embeddings2 = model.encode(list2)
    cosine_scores = util.cos_sim(embeddings1, embeddings2) # type: ignore
    
    count: int = 0
    for i in range(len(list1)):
        for j in range(len(list2)):
            if (cosine_scores[i][j] >= 0.80):
                count += 1
                break
            
    return count / len(list2)

