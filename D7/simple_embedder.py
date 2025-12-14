from math import sqrt
from re import I

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

def most_similar(words, embeddings):
    max_sim=-1
    most_sim="No word found"
    avg_vec=find_avg(words,embeddings)
    if avg_vec is None:
        return most_sim
    for i in embeddings:
        sim=cosine_similarity(avg_vec,embeddings[i])
        if sim>max_sim:
            max_sim=sim
            most_sim=i
    return most_sim

def preprocess_text(text):
    return text.lower().split()

def find_avg(words,embeddings):
    known=[]
    for word in words:
        if word in embeddings:
            known.append(word)
    if len(known)==0:
        return None
    x,y,z=0,0,0
    for word in known:
        x+=embeddings[word][0]
        y+=embeddings[word][1]
        z+=embeddings[word][2]
    n=len(known)
    return [x/n,y/n,z/n]
        
def main():
    word_vectors = {
  "ai": [1, 0, 0],
  "machine": [0.9, 0.1, 0],
  "learning": [0.8, 0.2, 0],
  "robot": [0, 1, 0],
  "space": [0, 0, 1],
}
    
    line=input("Enter the text: ")
    words=preprocess_text(line)
    similar=most_similar(words,word_vectors)
    print(f"Most Similar word according to the Input -> {similar}")
    
main()