import os
import pandas as pd
import matplotlib.pyplot as plt

e_key = "1234"

DF = pd.read_excel("CRM_data.xlsx")
crime_data = DF.to_dict('records')


def add_rec():
    global DF, crime_data
    print("\n\n")

    ID = int(input("Enter record ID: "))
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender (M/F): ")
    crime = input("Enter crime: ")
    rec = {"ID":ID, "Name":name, "Age":age, "Gender":gender, "Crime":crime}

    crime_data.append(rec)
    print("\nRecord added")
    DF = pd.DataFrame(crime_data)


def delete_rec(ID):
    global DF, crime_data
    for rec in crime_data:
        if rec["ID"] == ID:
            flag = True
            crime_data.remove(rec)
            print("\nDeletion successful")
            break
        else: 
            flag = False
    
    if not flag:
        print("\nDeletion failed")
        print("\nSorry, No record found")
    DF = pd.DataFrame(crime_data)


def find_rec(ID):
    global DF, crime_data
    for rec in crime_data:
        if rec["ID"] == ID:
            flag = True
            print("\nRecord Details")
            print("--------------\n")
            print("ID:     ", rec["ID"])
            print("Name:   ", rec["Name"])
            print("Age:    ", rec["Age"])
            print("Gender: ", rec["Gender"])
            print("Crime:  ", rec["Crime"])
            break
        else:
            flag = False
    
    if not flag: print("\nSorry, No record found")


def main_menu():
    print("\n\nCRIME RECORD MANAGER")
    print("--------------------")
    print("1. Add record")
    print("2. Delete record")
    print("3. Find record")
    print("4. Show registered records")
    print("5. Crime by gender plot")
    print("6. Crime proportion plot")
    print("7. Create csv file of records")
    print("8. Create excel file of records")
    print("9. Exit")

    print("\nEnter your choice: ", end ="")
    chs =int(input())
    os.system("cls")

    if chs == 1:
        add_rec()

    elif chs == 2:
        ID = int(input("Enter Record ID to delete: "))
        delete_rec(ID)

    elif chs == 3:
        ID = int(input("Enter Record ID to search: "))
        find_rec(ID)

    elif chs == 4:
        print("\n\n")
        print(DF.to_string(index=False))

    elif chs == 5:
        k = DF[["Gender"]].value_counts()
        k.plot(kind="bar")
        plt.show()

    elif chs == 6:
        k = DF[["Crime"]].value_counts()
        k.plot(kind="pie")
        plt.show()

    elif chs == 7:
        DF.to_csv("CRM_data.csv", index=False)

    elif chs == 8:
        DF.to_excel("CRM_data.xlsx", index=False)

    elif chs == 9:
        print("\nThank you for using our program")
        print("\nHope to see you soon...", end='')
        input()
        quit()

    else:
        print("\nInvalid Entry! Try again")

    print("\nPress ENTER to continue...", end="")
    input()
    os.system("cls")
    main_menu()


def login_menu():
    os.system("cls")

    print("\n\tUSER LOGIN")
    print("\t----------\n")

    entry = input("Enter Password: ")
    if entry == e_key:
        os.system("cls")
        main_menu()
    else:
        print("\nInvalid entry!, Please try again...", end="")
        input()
        os.system("cls")
        login_menu()


# Driver code

login_menu()
