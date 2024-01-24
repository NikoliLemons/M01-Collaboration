#Nikoli Lemons
#1/24/2024
#The program decides weather the student has made Dean's list or Honor Roll
lastname = input("Enter Student Last Name: ")
while lastname != "ZZZ":
    firstname = input("Enter Student First Name: ")
    gpa = float(input("Enter Student GPA: "))
    if gpa >= 3.5:
        print("{} {} has made the Dean's List.".format(firstname, lastname))
    else:
        if gpa >= 3.25:
            print("{} {} has made the Honor Roll.".format(firstname, lastname))
    lastname = input("\nEnter Student Last Name: ")