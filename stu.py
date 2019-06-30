students=[]
while True:
    print("Press 1 to Add Student")
    print("Press 2 to Edit Student")
    print("press 3 to student search")
    print("press 4 to delete student")
    print("press 6 to display all students")
    print("press 5 to exit")
    choice=int(input("Enter choice 1 to 6: "))
    if choice==1:
        student={}
        student['Name']=input('Enter student name: ')
        student['Age']=int(input('Enter student age: '))
        student['Class']=input('Enter student class: ')
        students.append(student)
    if choice==5:
        break
    if choice==6:
        print(students)
    if choice==2:
        id=input("Enter student name to update the data: ")
        for fu  in students:
            if id ==fu['Name']:
                fu['Name']=input("Enter name: ")
                fu['Age']=int(input("Enter age: "))
                fu['Class']=input("Enter class: ")
                print("Record edited successfully.")
    if choice==3:
        stid =input("Enter Student Name to search the data.")
        for fu in students:
            if stid==fu['Name']:
                print("Name:"   +fu['Name'])
                print("Age:"    +str(fu['Age'])) 
                print("Class:"  +fu['Class'])
    if choice==4:
        sid=input("Enter Student Name to delete the data of that student.")
        for fu in students:
               if sid ==fu['Name']:
                   students.remove(fu)
                   print("Record Deleted Successfully.")
         #       del fu['Name']
          #      del fu['Age']
           #     del fu['Class']
    else:
        print("Please Enter a valid choice.")