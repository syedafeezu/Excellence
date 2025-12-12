import random


movies = {
    "action": ["John Wick", "Mad Max", "Gladiator"],
    "comedy": ["The Mask", "21 Jump Street", "Deadpool"],
    "sci-fi": ["Interstellar", "The Matrix", "Inception"],
    "romance": ["La La Land", "The Notebook", "Her"],
    "horror": ["Conjuring", "Insidious", "It"]
}

def preprocess(text):
    text = text.lower().strip().split()
    return text
    
def get_genre(text, movie_dict):
    for i in text:
        if i in movie_dict:
            genre = i
            return genre
    else:
        return "unknown"
    
def recommend(genre, movie_dict):
    if genre == "unknown":
        return "I dont understand"
    else:
        return random.choice(movie_dict[genre])
def main(dict):
    while True:
        raw_text = input("You: ")
        if raw_text=="exit":
            print("Thank You, Have a Nice Day !")
            break
        processed_text=preprocess(raw_text)
        genre=get_genre(processed_text,dict)
        recommended_movie = recommend(genre, dict)
        
        print(f"Ai: I recommend: {recommended_movie}")
        
main(movies)