# lst = ["khan","king","jan","fayaz","obaid","raza"]

# for i in lst:
#     if i == "raza":
#         print("Your Elgiable")
#     elif i == "obaid":
#         print("Your Younger")
#     elif i == "fayaz":
#         print("Programmer")
#     else:
#         print("Not Found")

ls = []

def add(val):
    ls.append(val)

for i in range(5):
    user = input("Please Enter Any Value : ")
    add(user)

print(ls)
