
# for i in range(2):
#     input("Enter "+str(i)+" Value : ")
#     for j in range(4):
#         input("Enter Nested Loop "+str(j)+" value : ")

# print("End All Loop")

# lst = {}

# key = int(input("How Many Key's Do You Want to Add : "))

# users = int(input("How Many User's Column Do you Want To Add : "))

# for i in range(key):
#     users_data = []
#     for j in range(users):
#         users_data.append(input("Enter "+str(j)+" Value : "))
#     lst[i] = users_data        

# print(lst)


# for i in range(5):
#     for j in range(5):
#         print("*",end="")
#     print("")


# for i in range(10):
#     for j in range(i):
#         print("*",end="")
#     print("")

# for i in reversed(range(7)):
#     for j in range(i):
#         print("*",end="")
#     print("")

x = 1

for i in range(7):
    for j in reversed(range(i,7)):
        print(" ",end="")
    for j in range(x):
        print("*",end="")
    x += 1
    print("")

