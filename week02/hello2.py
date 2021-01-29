# Reads in a person's name then outputs a greeting for that person
# Author: Andrew Scott

# Asks the user to enter their name, which is then stored in a variable called name
name = input("Enter your name: ")

# Outputs a greeting using the name entered by the user
# The space after Hello ensures there is a space in the output message
# Without it the output would be one word i.e. HelloName
print ("Hello " + name + "\nNice to meet you.")