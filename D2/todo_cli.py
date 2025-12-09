tasks = []
c=0
while(c != 4):
    print("\n=====TODO LIST MENU=====")
    print("\t1. Add Task")
    print("\t2. View Tasks")
    print("\t3. Delete Task")
    print("\t4. Exit")
    c=int(input("Enter your choice : "))
    if(c==1):
        task=input("Enter Task : ")
        tasks.append(task)
        print("Task Added")
    elif(c==2):
        print("Your Tasks :")
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")
    elif(c==3):
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")
        d=int(input("Enter task number to delete : "))
        # tasks.remove(tasks[d-1])
        # print("Task Deleted")
        if (d>=1 and d<=len(tasks)) :
            tasks[d-1].pop()
        else:
            print("Enter a Valid Number !")
    elif(c==4):
        print("Thank You!")
        break
    else:
        print("Enter a Valid Choice !")