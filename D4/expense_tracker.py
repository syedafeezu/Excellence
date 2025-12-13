import json

def load_data():
    try:
        with open(r'D4/expenses.json', 'r') as file: # D4\expenses.json breaks in linux! So Im using raw string!
            exp = file.read()
            return json.loads(exp)
    except (FileNotFoundError, json.JSONDecodeError): # Forgot to handle JSONDecodeError earlier
        return []
    
    
def save_data(data):
    with open(r'D4/expenses.json', 'w') as file:
        return json.dump(data,file,indent=4)

def add_expense(data):
    item = input("Enter Item Name : ")
    try:
        amt = int(input("Enter the Amount : "))
        if amt<0:
            raise ValueError
    except ValueError:
        print('Enter a Valid Amount')
    else:
        data.append({'Item': item,
                     'Amount':amt})
    
def view_expense(data):
    print(json.dumps(data, indent=1))

def total_expense(data):
    tot=0
    for i in data:
        tot+=i['Amount']
    return tot

def main():
    c=0
    while(c!=4):
        print('====Expense Tracker====')
        print('1. Add Expense')
        print('2. View Expense')
        print('3. Total Spent')
        print('4. Exit')
        
        c=int(input('Enter your choice : '))
        
        if(c==1):
            data=load_data()
            add_expense(data)
            save_data(data)
        elif(c==2):
            data=load_data()
            print("--Your Expenses--")
            view_expense(data)    
        elif(c==3):
            data=load_data()
            print('Total Spent : ',total_expense(data))
        elif(c==4):
            print("Thank You !")
            break
        else:
            print("Enter a Valid Choice !")
            
main()