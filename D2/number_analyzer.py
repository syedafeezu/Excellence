n=int(input("Enter a number: "))

# if n>0:
#     print(f"The Number {n} is Positive",end='')
# elif n==0:
#     print(f"The Number {n} is Zero",end='')
# else:
#     print(f"The Number {n} is Negative",end='')

# if( n%2==0):
#     print(" & It is Even")
# else:
#     print(" & It is Odd")
sign = "Positive" if n>0 else "Zero" if n==0 else "Negative"
parity = "Even" if n%2==0 else "Odd"

print(f"The Number {n} Is {sign} && it is {parity}")