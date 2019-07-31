
accounts = {}
profile = {}

start = True
access = False

def add_student():
    id = int(input("Enter Student ID : "))
    name = input("Enter Student Name : ")
    fname = input("Enter Student Father Name : ")
    age = int(input("Enter Student Age : "))
    clas = int(input("Enter Student Class : "))
    profile[id] = [name,fname,age,clas]

def show_Student():
    print(profile)

def search_Student():
    id = int(input("Enter Search Student ID : "))
    found = True
    for i in profile:
        if i == id:
            found = False
            student_Id = str("Student ID : "+str(id))
            name = profile[id][0]
            fname = profile[id][1]
            age = str(profile[id][2])
            clas = str(profile[id][3])
            print(student_Id+"\nName : "+name+"\nFather Name : "+fname+"\nAge : "+age+
                        "\nClass : "+clas)
            break
    if found:
        print("This ID is Not Exists in Student Profile Please Enter Another ID")
        user_input = input("Do You Want to Continue Searching (Y/N) : ")
        if user_input == 'Y' or user_input =='y':
            search_Student()
        

def register():
    username = input("Please Enter Name : ")
    password = input("Please Enter Password : ")
    father_name = input("Please Enter Father Name : ")
    if len(accounts) > 0:
        found = True
        for i in accounts:
            if i == username:
                print("This Username is Already Exists Please Enter Again : ")
                found = False
                break
            
        if found:
            accounts[username] = [password,father_name]
            print("User Registered Successfully")
    else:
        accounts[username] = [password,father_name]
        print("User Registered Successfully")

while start:
    print("Welcome To Alsadiq Public High School")
    if access:
        print("Your are in the Main Menu")
        print("1: User's Account : ")
        print("2: add Student")
        print("3: show Students")
        print("4: search Student")
        print("5: Logout")
        user = int(input("Please Enter in Above Options: "))
        if user == 1:
            print(accounts)
        elif user == 2:
            add_student()
        elif user == 3:
            show_Student()
        elif user == 4:
            search_Student()
        elif user == 5:
            access = False
        else:
            print("Please Enter in Above Options")
    else:
        print("1: Login : ")
        print("2: Register : ")
        print("3: Quit : ")
        user_input = int(input("Please Enter in the Above Option's : "))
        if user_input == 1:
            username = input("Please Enter Username : ")
            password = input("Please Enter Password : ")
            if accounts[username][0] == password:
                access = True
                print("User Access Granted")
                
            else:
                print("Access Denied")
        elif user_input == 2:
            register()
        elif user_input == 3:
            print("Thanks For Visiting...?")
            start = False
        else:
            print("Please Enter The Value in Above Option's\nPlease Go Back")
            continue

