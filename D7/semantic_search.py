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
  "robots": [0, 1, 0],
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
    
def magnitude(vec):
    sum=0
    for i in range(len(vec)): # sqrt(a^2 + b^2 + c^2)
        sum += vec[i]**2
    mag=sqrt(sum)
    return mag

def cosine_similarity(vec_a, vec_b):
    cos=dot(vec_a,vec_b)/(magnitude(vec_a)*magnitude(vec_b)) # Formula for Cosine angle btwn Vectors
    return cos # measure the Closeness between the vecs not the Heights of vec

def preprocess_text(text):
    return text.lower().split() #Spliting the string into words

def find_avg(words,embeddings):  # Passing list of words and embeddings to find avg vector of known words
    known=[]
    for word in words:
        if word in embeddings:
            known.append(word)
    if len(known)==0:
        return 'Unknown'
    x,y,z=0,0,0
    for word in known:
        x+=embeddings[word][0] #Getting the x,y,z components of all known word vector from embeddings
        y+=embeddings[word][1]
        z+=embeddings[word][2]
    n=len(known)
    return [x/n,y/n,z/n] #Returning the avg vector of known words

''' to get the results i will just do preprocessing(splitting of words) and
get the vectors of words(if matches) then get the avg of words from each document
and then compare that with the avg of words from the query
and i'll keep track of ranks of docs
    and return the most similar one '''
    
def get_docs_avg(): # Getting avg vectors of all documents
    avg_docs={}
    for name,text in documents.items():
        avg_vec = find_avg(text.split(), word_vectors) #Splitting the document text into words and passing to find_avg function 
        avg_docs[name] = avg_vec
    return avg_docs  #returning a dictionary of document names and their avg vectors

def similarity(text_vec,docs_vec): # Getting similarity scores of query vector with all document vectors
    sim={}
    for name,doc_vec in docs_vec.items():
        sim[name]=cosine_similarity(text_vec,doc_vec)
    return sim #Returning a dictionary of document names and their similarity scores with the query

def sim_rank(similarity_list):# Getting the top 2 similar documents based on similarity scores
    top_k={}
    for  doc,score in sorted(similarity_list.items(), key=lambda x: x[1], reverse=True)[:2]: #Sorting the similarity scores in descending order and getting top 2 documents
        top_k[doc]=score # lambda function to sort based on similarity scores if we put x[0] it will sort based on document names but we want based on scores!
    return top_k #returns Dict of top 2

def main():
    query=input("Enter the Query : ") #Getting the Query from User
    processed_txt=preprocess_text(query) # Preprocessing the Query(String to list of words)
    query_avg_vector=find_avg(processed_txt, word_vectors) # Getting the vectors of known words and then avg vector of the query
    docs_avg= get_docs_avg() # Getting avg vectors of all documents
    similarity_list=similarity(query_avg_vector,docs_avg) #Passing the query avg vec and dict of doc avg vecs to get similarity scores
    sim_rank_list=sim_rank(similarity_list) #Getting the top 2 similar documents based on similarity scores
    print("Ranked Documents based on Similarity : ")
    for doc,score in sim_rank_list.items(): #Printing the ranked documents with similarity scores
        print(f"{doc} : ({score})")
        
main()