# Program that allows user to create new students with their modules and grades
# Author: Andrew Scott

# A function that prints out the menu and takes in a menu choice
def menu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    userInput = input("Type one letter (a/v/q): ").strip()
    
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

# Main program 
students = []
while choice != "q":
    if choice == "a":
        doAdd(students)
    elif choice == "v":
        doView(students)
    elif choice != "q":
        print("\nPlease select either a, v, or q\n")
    choice = menu()
