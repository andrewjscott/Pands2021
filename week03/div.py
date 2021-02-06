# User is asked to enter two numbers and the output is the first number divided by the second
# Output is given as a whole number along with the remainder

# Asks the user to enter numbers, which are then converted from str to int so they can be divided
x = int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))

# Stores the answer of x divided by y to the nearest whole number
answer = x // y 
# Stores the remainder left over after x is divided by y
remainder = x % y

# Outputs the first user entered number divided by the second, converted to string so they can be printed in a sentence
print("{} divided by {} is {}, with a remainder of {}".format(x, y, answer, remainder))