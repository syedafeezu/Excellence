# def diagnose(symptom):
#     print("Diagnosis:")
#     if ( "fever" in symptom or 
#         "headache" in symptom or 
#         "cold" in symptom or 
#         "pain" in symptom ):
#         if "fever" in symptom:
#             print("--You might have a viral infection.")
#         if "headache" in symptom:
#             print("--Possible dehydration or stress.")
#         if "cold" in symptom:
#             print("--You may have a common cold.")
#         if "pain" in symptom:
#             print("--Pain detected, consult a doctor.")
#     else:
#         print("--Symptom not recognized. Please consult a healthcare professional.")
#     return 0

def diagnose(symptom):
    print("Diagnosis:")

    rules = {
        "fever": "--You might have a viral infection.",
        "headache": "--Possible dehydration or stress.",
        "cold": "--You may have a common cold.",
        "pain": "--Pain detected, consult a doctor."
    }
    recognized = False

    for word,message in rules.items():
        if word in symptom:
            print(message)
            recognized = True
    if not recognized:
        print("--Symptom not recognized. Please consult a healthcare professional.")
    
symptom = input("Enter your symptom: ").lower()
print(diagnose(symptom))