from utility import *
import string

def preprocess(text):
    words = text.lower().strip()
    for p in string.punctuation:        # improvement From Ai
        words = words.replace(p, "")    # remove punctuation
    return words
    
def intent_detect(text):
    if "hello" in text or "hi" in text:
        intent = "greeting"
    elif "bye" in text:
        intent = "goodbye"
    elif "price" in text or "cost" in text:
        intent = "pricing"
    elif "help" in text or "support" in text:
        intent = "support"
    else:
        intent = "unknown"
    return intent


def generate_response(intent):
    # if intent =="greeting": 
    #     response = "Hello! How can I assist you?"
    # if intent =="goodbye": 
    #     response = "Goodbye! Have a great day!"
    # if intent =="pricing": 
    #     response = "Our product starts at Rs. 499."
    # if intent =="support": 
    #     response = "Sure, tell me what issue you're facing."
    # if intent =="unknown": 
    #     response = "I'm not sure I understand. Try asking differently."
    # return response
    responses = {
        "greeting": "Hello! How can I assist you?",
        "goodbye": "Goodbye! Have a great day!",
        "pricing": "Our product starts at Rs. 499.",
        "support": "Sure, tell me what issue you're facing.",
        "unknown": "I'm not sure I understand. Try asking differently."
    }
    return responses[intent]

def main():
    print("====AI PIPELINE====")
    while True:    
        text = input("You: ")
        if(text=="exit"):
            print("Thank You! Have a Nice Day. Chat Ended.")
            break
        processed_text=preprocess(text)
        intent = intent_detect(processed_text)   
        response = generate_response(intent)
        print("AI: ", response)
        line()
clear_screen()
main()