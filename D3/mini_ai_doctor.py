def diagnose(symptom):
    print("Diagnosis:")
    if "fever" or "headache" or "cold" or "pain" in symptom:
        if "fever" in symptom:
            print("--You might have a viral infection.")
        if "headache" in symptom:
            print("--Possible dehydration or stress.")
        if "cold" in symptom:
            print("--You may have a common cold.")
        if "pain" in symptom:
            print("--Pain detected, consult a doctor.")
    else:
        print("--Symptom not recognized. Please consult a healthcare professional.")
    return 0
symptom = input("Enter your symptom: ").lower()
print(diagnose(symptom))