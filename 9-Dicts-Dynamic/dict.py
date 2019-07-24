students = {}


# id = int(input("Please Enter ID : "))
# name = input("Please Enter Name : ")
# age = int(input("Please Enter Age : "))
# clas = input("Please Enter Class : ")
# subject = input("Please Enter Subject : ")

# students[id] = [name,age,clas,subject]

# print(students[5])

x = 1
user = int(input("How Many Student's Do you Want Add in Dict : "))

for i in range(user):
    students[x] = [input("Please Enter Name : "),input("Father Name : "),
                input("Age : "),input("Subject : "),input("Marks : ")]
    x += 1

print(students)

search = int(input("Search Student by ID : "))

#print(students[search])
print("Name : "+students[search][0])
print("Father Name : "+students[search][1])
print("Age : "+students[search][2])
print("Subject : "+students[search][3])
print("Marks : "+students[search][4])
