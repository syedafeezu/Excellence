def check_password(password):
    score = 0

    if len(password)>=8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in '! @ # $ % ^ & * ( ) - _ = + [ ] { } ; : , . / ?' for c in password):
        score += 1

    if 0<=score<=2:
        return "Weak"
    elif 2<score<4:
        return "Medium"
    else:
        return "Strong"
    
pswrd = input("Enter your password to check: ")
print("Your Password Strength is ", check_password(pswrd))