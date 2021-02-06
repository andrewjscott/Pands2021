# Variables of the types int, float, boolean, str, and list
# Author: Andrew Scott

# Creates a variable with the types int, float, boolean, str, and list respectively
integer = 5
fltNumber = 5.555
trueOrFalse = False
string = "hygtrf"
myList = [5, 5.555, False, "hygtrf"]

# Outputs what the type and value of each variable is
# .format is used to inset values at each location curly brackets are used, in this case it insets a string, 
# the variable type, and the variable value at the location of the three curly brackets respectively 
print("Variable {} is of the type: {} and the value: {}".format('integer',type(integer),(integer)))
print("Variable {} is of the type: {} and the value: {}".format('fltNumber',type(fltNumber),(fltNumber)))
print("Variable {} is of the type: {} and the value: {}".format('trueOrNumber',type(trueOrFalse),(trueOrFalse)))
print("Variable {} is of the type: {} and the value: {}".format('string',type(string),(string)))
print("Variable {} is of the type: {} and the value: {}".format('myList',type(myList),(myList)))