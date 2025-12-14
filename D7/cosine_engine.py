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

def main():
    a = [1, 0, 0]
    b = [0.9, 0.1, 0]
    print(cosine_similarity(a, b))
    
main()