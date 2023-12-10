def calculate_similarity(sentence1: str, sentence2: str):
    
    set1 = set(sentence1.split())
    set2 = set(sentence2.split())
    
    intersection = set1 & set2
    union = set1 | set2
    
    print(intersection)
    return len(intersection) / len(union) if len(union) != 0 else 0
