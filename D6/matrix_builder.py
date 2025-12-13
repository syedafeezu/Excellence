def parse_vector(text):
    vec=map(int,text.split(','))
    return list(vec)
def build_matrix(vectors):
    matrix=vectors
    return matrix
def print_matrix(matrix):
    for row in matrix:
        print(row)
def input_vectors():
    try:
        n=int(input("Enter the Number of Vectors: "))
        if n<1:
            print("Number of vectors must be at least 1.")
            return input_vectors()
        vectors=[]
        for i in range(n):
            A=input(f"Enter Values for Vector {i+1} (CSV): ")
            vectors.append(parse_vector(A))
        return vectors
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return input_vectors()
    
def main():
    vectors=input_vectors()
    matrix=build_matrix(vectors)
    print("Matrix Representation:")
    print_matrix(matrix)
    
main()