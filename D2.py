#bmi_calculator.py
name= input("Enter your Name:")
weight= int(input("Enter your weight:"))
height= int(input("Enter your height:"))

bmi= weight/height**2

print(f"Hello, {name}!. Your BMI is {bmi:.2f}.")
