from math import sqrt

def parse_vector(text):
    vec=map(int,text.split(','))
    return list(vec)

def normalise(vector):
    norm_vec=[]
    mag = magnitude(vector)
    for i in range(len(vector)):
        norm_vec.append(vector[i]/mag)
    return norm_vec

def magnitude(vector):
    sum=0
    for i in range(len(vector)):
        sum += vector[i]**2
    mag=sqrt(sum)
    return mag

def main():
    A=input("Enter Values for Vector A (CSV): ")
    vec=parse_vector(A)
    print("The Normalized Vector is = ", normalise(vec))
    
main()