
accounts = {}

start = True
access = False



def register():
    username = input("Please Enter Name : ")
    accounts[username] = input("Please Enter Password : ")
    print("User Registered Successfully")

while start:
    print("Welcome To Alsadiq Public High School")
    if access:
        print("Your are in the Main Menu")
        input("please Write Something... : ")
    else:
        print("1: Login : ")
        print("2: Register : ")
        print("3: Quit : ")
        user_input = int(input("Please Enter in the Above Option's : "))
        if user_input == 1:
            username = input("Please Enter Username : ")
            password = input("Please Enter Password : ")
            if accounts[username] == password:
                print("User Access Granted")
                access = True
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

