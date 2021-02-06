# Takes in a value in dollars and returns the absolute value in cents
# Author: Andrew Scott

# Asks the user to input a dollar value which is stored to a variable
dollars = float(input("Enter an amount in dollars: "))

# Stores the absolute of the value entered by the user 
absDollars = abs(dollars)

# Converts the number entered by the user to cents by multiplying by 100
cents = absDollars * 100

# rounds the cents value to a whole number
roundCents = round(cents)

# Outputs the rounded cents value
print("That amount in cents is " + str(roundCents))