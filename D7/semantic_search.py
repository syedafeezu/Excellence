from math import sqrt
documents = {
  "doc1": "ai and machine learning",
  "doc2": "robots and automation",
  "doc3": "space exploration mission",
  "doc4": "deep learning in ai"
} # Sample documents (Will be replaced by actual document contents)

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
} # Embedding vectors for words in documents

def dot(a, b):
    dot=0
    for i in range(len(a)):
        dot+=a[i]*b[i]
    return dot
    
def magnitude(a):
    sum=0
    for i in range(len(a)):
        sum += a[i]**2
    mag=sqrt(sum)
    return mag

def cosine_similarity(a, b):
    cos=dot(a,b)/(magnitude(a)*magnitude(b))
    return cos

def preprocess_text(text):
    return text.lower().split()

def find_avg(words,embeddings):  # Passing list of words and embeddings to find avg vector of known words
    known=[]
    for word in words:
        if word in embeddings:
            known.append(word)
    if len(known)==0:
        return 'Unknown'
    x,y,z=0,0,0
    for word in known:
        x+=embeddings[word][0] #Getting the x,y,z components of each known word vector from embeddings
        y+=embeddings[word][1]
        z+=embeddings[word][2]
    n=len(known)
    return [x/n,y/n,z/n] #Returning the avg vector of known words

''' to get the results i will just do preprocessing(splitting of words) and
get the vectors of words(if matches) then get the avg of words from each document
and then compare that with the avg of words from the query
and i'll keep track of ranks of docs
    and return the most similar one '''
    
def get_docs_avg():
    avg_docs={}
    for name,text in documents.items():
        avg_vec = find_avg(text.split(), word_vectors) #Splitting the document text into words and passing to find_avg function 
        avg_docs[name] = avg_vec
    return avg_docs  

def similarity(text_vec,docs_vec):
    sim={}
    for name,vec in docs_vec.items():
        sim[name]=cosine_similarity(text_vec,vec)
    return sim

def sim_rank(similarity_list):
    top_k={}
    for  doc,score in sorted(similarity_list.items(), key=lambda x: x[1], reverse=True)[:2]:
        top_k[doc]=score
    return top_k

def main():
    query=input("Enter the Query : ") #Getting the Query from User
    processed_txt=preprocess_text(query) # Preprocessing the Query(String to list of words)
    query_avg_vector=find_avg(processed_txt, word_vectors) # Getting the vectors of known words and then avg vector of the query
    docs_avg= get_docs_avg() # Getting avg vectors of all documents
    similarity_list=similarity(query_avg_vector,docs_avg) 
    sim_rank_list=sim_rank(similarity_list)
    print("Ranked Documents based on Similarity : ")
    for doc,score in sim_rank_list.items():
        print(f"{doc} : ({score})")
        
main()