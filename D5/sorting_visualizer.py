def bubble_sort(arr):
    print(arr)
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
            print(arr)
            
def selection_sort(arr):
    n=len(arr)
    print(arr)
    for i in range(n): 
        for j in range(i,n):
            min=i
            if arr[i]>arr[j]:
                min=j
                arr[i],arr[min]=arr[min],arr[i]
        print(arr)
        
def get_values():
    try:
        values=map(int, input("Enter numbers separated by space: ").split())
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return get_values()
    return values

def menu(val):
    print("Choose Sorting Algorithm:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    try:
        c=int(input("Enter the Choice : "))
        if c==1:
            bubble_sort(val)
        elif c==2:
            selection_sort(val)
        else:
            print("Enter the Correct choice!")
            menu(val)
    except ValueError:
        print("Invalid input. Please enter integers only.")
        menu(val)
        
def main():
    print('====SORTING VISUALIZER====')
    val=list(get_values())
    menu(val)
main()
        