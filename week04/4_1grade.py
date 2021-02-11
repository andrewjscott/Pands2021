# User enters a student's percentage mark and the output is the corresponding grade
# Author: Andrew Scott

percentage = float(input("Enter percentage: "))

# this first line makes sure the user inputs a valid grade percentage between 0 and 100, returning a message 
# letting the user know about their error if they input a number outside that range
if percentage < 0 or percentage > 100:
    print("Please enter a number between 0 and 100")
elif percentage < 40: # This line is only run if the number is greater than zero so the lower range doesn't need to be specified again
    print("Fail")
elif percentage < 50: # Likewise each subsequent line of code is only run if the previous command was false
    print("Pass")
elif percentage < 60:
    print("Merit2")
elif percentage < 70:
    print("Merit1")
else:
    print("Distinction")