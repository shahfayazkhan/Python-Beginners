Students = {
    1: ["Shahfayaz Khan","Khail Badshah",24,10,"computer"],
    2: ["raza khan","Memzad gul",25,11,"English"]
}

Students[2][4] = "Urdu"

Students[3] = ["Obaid","Obaid Khan",26,9,"Pashto"]

for i in Students:
    print("Name : "+Students[i][0])
    print("Father Name : "+Students[i][1])
    print("Class : "+str(Students[i][2]))
    print("Age : "+str(Students[i][3]))
    print("Subject : "+Students[i][4])
    print("-----------------------------------------------")
