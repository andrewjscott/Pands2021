# Attempts to answer the extra questions for lab 4.1
# Author: Andrew Scott

# I think the easiest method to ensure that grades get rounded up is to lower the range conditions
# of each if statement by 0.5. This ensures that, for example, a grade of 39.8 will not
# not output the message "Fail" as it is greater than 39.5. The value of 39.8 will however meet
# the conditions for the following elif statement as it is less than 49.5, so the input of 
# 39.8 will output the message "Pass"

percentage = float(input("Enter percentage: "))

if percentage < 0 or percentage > 100:
    print("Please enter a number between 0 and 100")
elif percentage < 39.5:
    print("Fail")
elif percentage < 49.5: 
    print("Pass")
elif percentage < 59.5:
    print("Merit2")
elif percentage < 69.5:
    print("Merit1")
else:
    print("Distinction")