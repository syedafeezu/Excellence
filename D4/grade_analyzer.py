def get_marks():
    marks=[]
    n = int(input("Enter the Number of Subjects : "))
    while(i!=n):
        try:
            m = int(input(f"Enter the mark for Subject {i} : "))
            if m<0 or m>100:
                raise ValueError 
        except ValueError:
            print("Enter a Valid Mark")
        else:
            marks.append(m)
            i+=1
    return "Retreival Done"
def calculate_average(marks):
    tot=0
    for i in range(marks):
        tot+=marks[i]
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
    marks=get_marks()
    avg=calculate_average(marks)
    grade=find_grade(avg)
    
    print("The Average is ",avg)
    print("The Grade is ",grade)
    
main()
