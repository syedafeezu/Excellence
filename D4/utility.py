def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def read_int(prompt):
    try:
        n=int(input(prompt))
    except ValueError:
        print('Enter a Valid Integer !')
        return read_int(prompt)
    else:
        return n

def read_flt(prompt):
    try:
        n=input(prompt)
        if '.' not in str(n):
            raise ValueError
        for any in str(n):
            if any not in '-0123456789.':
                raise ValueError
    except ValueError:
        print('Enter a Valid Float !')
        return read_flt(prompt)
    else:
        return n
    
def line():
    print('------------------------------')
    
    
# def read_flt(prompt):
#    while True:
#         s = input(prompt)
#         try:
#            return float(s)
#         except ValueError:
#            print('Enter a Valid Float !')


# def read_int(prompt):
#     while True:
#         try:
#             return int(input(prompt))
#         except ValueError:
#             print('Enter a Valid Integer !')
 