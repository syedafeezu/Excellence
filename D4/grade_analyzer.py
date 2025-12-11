def get_marks():
    marks=[]
    n = int(input("Enter the Number of Subjects : "))
    i=0
    while(i!=n):
        try:
            m = int(input(f"Enter the mark for Subject {i+1} : "))
            if m<0 or m>100:
                raise ValueError 
        except ValueError:
            print("Enter a Valid Mark")
        else:
            marks.append(m)
            i+=1
    return marks
def calculate_average(marks):
    tot=0
    for i in marks:
        tot+=i
    avg = tot/len(marks)
    return avg

def find_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 75:
        return 'B'
    elif avg >= 60:
        return 'C'
    elif avg >= 40:
        return 'D'
    else:
        return 'F'
def main():
    print("=====Grade Analyzer=====")
    marks=get_marks()
    avg=calculate_average(marks)
    grade=find_grade(avg)
    
    print("The Average is",avg)
    print("The Grade is",grade)
    
main()
