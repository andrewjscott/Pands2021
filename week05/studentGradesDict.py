# Stores a student name and a list of her courses and grades in a dict,  then prints out her data
# Author: Andrew Scott

# Creates a dict for a student where their modules and grades are paired
student = {
    "name":"Mary",
    "modules": [
        {
            "courseName":"Programming",
            "grade": 45
        },
        {
            "courseName":"History",
            "grade":99
        }
    ]
}

# Prints out all the modules and grades stored for that student
print ("Student: {}".format(student["name"]))
for module in student["modules"]:
    print("\t {} \t: {}".format(module["courseName"], module["grade"]))