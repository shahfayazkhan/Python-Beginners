
accounts = {}

start = True
access = False


def register():
    username = input("Please Enter Name : ")
    password = input("Please Enter Password : ")
    father_name = input("Please Enter Father Name : ")
    age = int(input("Please Enter Age : "))
    mobile = input("Please Enter Mobile No : ")
    address = input("Please Enter Address : ")
    clas = input("Enter Student Class : ")
    if len(accounts) > 0:
        found = True
        for i in accounts:
            if i == username:
                print("This Username is Already Exists Please Enter Again : ")
                found = False
                break
            
        if found:
            accounts[username] = [password,father_name,age,mobile,address,clas]
            print("User Registered Successfully")
    else:
        accounts[username] = [password,father_name,age,mobile,address,clas]
        print("User Registered Successfully")

while start:
    print("Welcome To Alsadiq Public High School")
    if access:
        print("Your are in the Main Menu")
        print("1: User's Account : ")
        print("2: Logout")
        user = int(input("Please Enter in Above Options: "))
        if user == 1:
            print(accounts)
        elif user == 2:
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

