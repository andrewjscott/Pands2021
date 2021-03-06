# Program that allows user to create new students with their modules and grades
# Author: Andrew Scott

import json

# A function that prints out the menu and takes in a menu choice
def menu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(s) Save students")
    print("\t(l) Load students")
    print("\t(q) Quit")
    userInput = input("Type one letter (a/v/s/l/q): ").strip()
    
    return userInput

# A function to add a student's modules and grades
def enterModules():
    modules = []
    newModule = input("\t Enter the first module name (blank to quit): ").strip()
    while newModule != (""):
        module = {}
        module["name"] = newModule
        module["grade"] = int(input("\t\tEnter grade: "))
        modules.append(module)
        newModule = input("\t Enter the next module name (blank to quit): ").strip()
    return modules

# A function to add new students after the user selects this from the menu
def doAdd(students):
    studentName = {}
    studentName["name"] = input("Enter student name: ").strip()
    studentName["modules"] = enterModules()
    students.append(studentName)

    print(students)

# Functions to view the students and modules currently entered
def viewModules(modules):
    print ("\tName   \tGrade")
    for module in modules:
        print("\t{}  \t{}".format(module["name"], module["grade"]))

def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        viewModules(currentStudent["modules"])

choice = menu()

# A function to save the students currently entered
def doSave(students):
    filename = "students.json"
    with open(filename, "wt") as f:
        json.dump(students, f)
        print("Students saved")
    
# A function to load students that were previously saved
def doLoad(students):
    filename = "students.json"
    with open(filename) as f:
        return json.load(f)

# Main program 
students = []
while choice != "q":
    if choice == "a":
        doAdd(students)
    elif choice == "v":
        doView(students)
    elif choice == "s":
        doSave(students)
    elif choice == "l":
        students = doLoad(students)
    elif choice != "q":
        print("\nPlease select either a, v, or q\n")
    choice = menu()
