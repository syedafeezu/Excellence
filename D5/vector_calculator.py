from math import sqrt

def parse_vector(text):
    vec=map(int,text.split(','))
    return list(vec)
def dot_product(a, b):
    dot=0
    for i in range(len(a)):
        dot+=a[i]*b[i]
        return dot
def vector_add(a, b):
    c=[]
    for i in range(len(a)):
        sum=a[i]+b[i]
        c.append(sum)
    return c

def vector_sub(a, b):
    c=[]
    for i in range(len(a)):
        sub=a[i]-b[i]
        c.append(sub)
    return c

def magnitude(a):
    sum=0
    for i in range(len(a)):
        sum += a[i]**2
    mag=sqrt(sum)
    return mag

def main():
    A=input("Enter Values for Vector A (CSV): ")
    B=input("Enter Values for Vector B (CSV): ")
    vec_a=parse_vector(A)
    vec_b=parse_vector(B)
    print("A + B : ", vector_add(vec_a,vec_b))
    print("A - B : ", vector_sub(vec_a,vec_b))
    print("Dot Product : ", dot_product(vec_a,vec_b))
    print("Magnitude of A : ", magnitude(vec_a))
    print("Magnitude of B : ", magnitude(vec_b))
    
main()