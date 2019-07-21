
students = []

teachers = []

bol = True

def show_Teachers():
    print(teachers)

def add_Teacher():
    id = input("Please Enter Teacher ID : ")
    name = input("Please Enter Teacher Name : ")
    fname = input("Please Enter Teacher Father Name : ")
    subject = input("Please Enter Teacher Subject : ")
    teachers.append(id)
    teachers.append(name)
    teachers.append(fname)
    teachers.append(subject)

def show_Student():
    x = 0
    for i in range(len(students)):
        print("Name : "+str(students[x])+"\t\tFather Name : "+str(students[x+1])+
                "\t\tClass : "+str(students[x+2])+"\t\tMarks : "+str(students[x+3]))
        
        x = x+4
        if x == len(students):
            break


def add_Student():
    name = input("Enter Student Name : ")
    fname = input("Enter Student Father Name : ")
    cla = input("Enter Student Class : ")
    marks = input("Enter Student Marks : ")
    students.append(name)
    students.append(fname)
    students.append(cla)
    students.append(marks)
    print("\t\tStudent Added Successfully")

while bol:
    print("1 : Add Student : ")
    print("2 : Add Teacher : ")
    print("3 : Show Students : ")
    print("4 : Show Teachers : ")
    print("5 : Quit")
    user = int(input("Please Enter Any value in Above Option : "))
    if user == 1:
        add_Student()
    elif user == 2:
        add_Teacher()
    elif user == 3:
        show_Student()
    elif user == 4:
        show_Teachers()
    elif user == 5:
        print("Thanks For Using our")
        bol = False
    else:
        continue


"""
add few function's like : ID,age,mobile,address,subject
format like this : 
    ======================================================================================
    |  ID  |  Name  |  Father Name  |  Class  |  English  | Urdu  |  Computer  |  Total  |
    --------------------------------------------------------------------------------------
    |  1   |sfk     | khial badshah |  10     | 78        | 10    |   40       |  129    |
    --------------------------------------------------------------------------------------
                            Al-Sadiq Public High School Teri
"""
