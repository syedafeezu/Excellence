from math import sqrt

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

def most_similar(word, embeddings):
    max_sim=-1
    most_sim="No word found"
    for i in embeddings:
        if i==word:
            continue
        sim=cosine_similarity(embeddings[word],embeddings[i])
        if sim>max_sim:
            max_sim=sim
            most_sim=i
    return most_sim
    
def main():
    embeddings = {
    "hello": [1, 0, 0],
    "hi": [0.9, 0.1, 0],
    "bye": [0, 1, 0],
    "night": [0, 0, 1]
    }
    word=input("Enter the Word to Search: ")
    similar=most_similar(word,embeddings)
    print(f"Most Similar to {word} -> {similar}")
    
main()