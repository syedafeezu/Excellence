from unittest import TestCase
from simple_embedder import cosine_similarity,find_avg,preprocess_text


documents = {
  "doc1": "ai and machine learning",
  "doc2": "robots and automation",
  "doc3": "space exploration mission",
  "doc4": "deep learning in ai"
}

word_vectors = {
  "ai": [1, 0, 0],
  "machine": [0.9, 0.1, 0],
  "learning": [0.8, 0.2, 0],
  "robot": [0, 1, 0],
  "space": [0, 0, 1],
  "deep" : [0.82, 0.24, 0.67],
  "automation": [0.71, 0.88, 0.30],
  "exploration": [0.55, 0.42, 0.91],
  "mission": [0.68, 0.60, 0.49]
}


''' to get the results i will just do preprocessing(splitting of words) and
get the vectors of words(if matches) then get the avg of words from each document
and then compare that with the avg of words from the query
and i'll keep track of ranks of docs
    and return the most similar one '''
    
def get_docs_avg():
    avg_docs={}
    for name,text in documents.items():
        avg_vec = find_avg(text, word_vectors)
        avg_docs[name] = avg_vec
    return avg_docs

def similarity(text_vec,docs_vec):
    sim={}
    for name,vec in docs_vec.items():
        sim[name]=cosine_similarity(text_vec,vec)
    return sim
def sim_rank(similarity_list):
     top_k = sorted()
    
def main():
    query=input("Enter the Query : ")
    processed_txt=preprocess_text(query)
    query_avg_vector=find_avg(processed_txt, word_vectors) # Getting the Query's Avg vector to compare to docs
    docs_avg= get_docs_avg()
    similarity_list=similarity(query_avg_vector,docs_avg)
    sim_rank=sim_rank(similarity_list)